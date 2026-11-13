"""Builds entrance/exams.json, entrance/universal_topics.json and build/map_data.json
from topics_src.py and exams_src.py.
Run from this folder:  python3 build.py && python3 make_map.py
"""
import json, re, os, datetime, collections
import topics_src as T
import exams_src as E

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
ROOT = os.path.dirname(OUT)
TODAY = datetime.date(2026, 11, 13)

def slug(s):
    s = s.lower().replace("&", "and")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:64]

# ---------------------------------------------------------------- universal topics
subjects = []          # list of dict
topic_index = {}       # id -> topic dict
for sid, sname, src in T.SUBJECTS:
    units = []
    for line in [l for l in src.strip().splitlines() if l.strip()]:
        uname, cls, uflags, rest = [x.strip() for x in line.split("|", 3)]
        topics = []
        for t in [x.strip() for x in rest.split(";") if x.strip()]:
            m = re.match(r"^(.*)\{([A-Z]+)\}$", t)
            name, flags = (m.group(1).strip(), m.group(2)) if m else (t, uflags)
            tid = f"{sid}:{slug(uname)}:{slug(name)}"
            topic = {"id": tid, "name": name, "flags": flags, "cls": cls, "exams": []}
            topics.append(topic); topic_index[tid] = topic
        units.append({"id": f"{sid}:{slug(uname)}", "name": uname, "class": cls, "topics": topics})
    subjects.append({"id": sid, "name": sname, "units": units})
subj_by_id = {s["id"]: s for s in subjects}

# B.Tech block from the existing data pack
uni = json.load(open(os.path.join(ROOT, "pack", "universal.json")))
uni_sub = {s["id"]: s for s in uni["subjects"]}
bt_units = {}
def bt_unit(sub_id):
    if sub_id not in bt_units:
        s = uni_sub[sub_id]
        topics = []
        for u in s["units"]:
            tid = f"btech:{sub_id}:u{u['n']}"
            topic = {"id": tid, "name": u["name"], "flags": "B", "cls": "UG", "exams": [],
                     "btech_ref": {"subject": sub_id, "unit": u["n"], "subtopics": len(u["subtopics"])}}
            topics.append(topic); topic_index[tid] = topic
        bt_units[sub_id] = {"id": f"btech:{sub_id}", "name": s["name"], "class": "UG", "dept": s.get("dept"), "topics": topics}
    return bt_units[sub_id]

own_units = {}
def own_unit(name):
    if name not in own_units:
        tid = f"own:{slug(name)}"
        topic = {"id": tid, "name": name, "flags": "X", "cls": "-", "exams": []}
        topic_index[tid] = topic
        own_units[name] = {"id": tid, "name": name, "class": "-", "topics": [topic]}
    return own_units[name]

def pick(sid, sel):
    out = []
    for u in subj_by_id[sid]["units"]:
        for t in u["topics"]:
            if isinstance(sel, list):
                ok = u["name"] in sel
            elif sel == "*":
                ok = True
            elif sel == "C":
                ok = "N" in t["flags"] and "12" in t["cls"]
            else:
                ok = sel in t["flags"]
            if ok:
                out.append((subj_by_id[sid]["name"], u["name"], t))
    if isinstance(sel, list):
        missing = set(sel) - {u["name"] for u in subj_by_id[sid]["units"]}
        assert not missing, (sid, missing)
    return out

def gate_ids(code):
    if code == "ALL":
        ids = []
        for v in T.GATE_MAP.values():
            ids += v
    elif code == "ESE":
        ids = T.GATE_MAP["CE"] + T.GATE_MAP["ME"] + T.GATE_MAP["EE"] + T.GATE_MAP["EC"]
    else:
        ids = T.GATE_MAP[code]
    return list(dict.fromkeys(ids))

FAMILY = {"state-talent", "bed-entrance", "state-nursing", "state-agri", "poly-merit-states", "pgecet"}
S_CAP = {
    "cuet-pg": (0.35, "Only the science, commerce and computer papers are mapped; most of the 157 subject codes are not, so the computed share is capped"),
    "ugc-net": (0.35, "Paper 2 has 85 subjects; only commerce, management and computer science map to the pack, so the computed share is capped"),
    "csir-net": (0.50, "Chemical and Earth Sciences and much of Life Sciences are outside the pack, so the computed share is capped"),
}
exam_topics = {}
for r in E.ROWS:
    picked = []
    for key, sel in r["prof"].items():
        if key == "btech":
            ids = gate_ids(sel.split(":")[1]) if isinstance(sel, str) else sel
            for sub_id in ids:
                assert sub_id in uni_sub, (r["id"], sub_id)
                u = bt_unit(sub_id)
                picked += [("B.Tech and degree subjects", u["name"], t) for t in u["topics"]]
        elif key == "own":
            for name in sel:
                u = own_unit(name)
                picked += [("Exam-specific", u["name"], t) for t in u["topics"]]
        else:
            picked += pick(key, sel)
    exam_topics[r["id"]] = picked
    for _, _, t in picked:
        t["exams"].append(r["id"])

core_ids = {r["id"] for r in E.ROWS if r["group"] == "core"}

def ncert_info(sid, t):
    if "N" not in t["flags"]:
        if sid in ("physics", "chemistry", "maths", "biology"):
            return {"status": "out", "note": "Not in the current NCERT class 11-12 textbooks (dropped in the 2023 rationalisation or never included); still asked by the exams listed"}
        if sid in ("f_maths", "f_science"):
            return {"status": "out", "note": "NCERT class 8-10 level; outside the class 11-12 lessons"}
        return {"status": "not_applicable"}
    cls = t["cls"]
    classes = [c for c in ("11", "12") if c in cls]
    seen = [c for c in classes if (sid, c) in T.CBSE_SKILLS_SEEN]
    if len(seen) == len(classes):
        cov = "lesson skill seen for this class and subject"
    elif seen:
        cov = "class %s lesson skill seen; class %s assumed from the brief" % (", ".join(seen), ", ".join(c for c in classes if c not in seen))
    else:
        cov = "assumed from the brief; no lesson skill for this class and subject was seen in this workspace"
    return {"status": "in", "class": cls, "book": T.NCERT_BOOK.get(sid), "cbse_free_n_easy": cov}

def btech_info(sid, t):
    if "btech_ref" in t:
        r = t["btech_ref"]
        return {"status": "in", "subject": r["subject"], "unit": r["unit"], "subtopics": r["subtopics"],
                "book": f"{uni_sub[r['subject']].get('dept')}/{r['subject']}/{r['subject']}-u{r['unit']}.html"}
    if sid in ("quant", "reasoning"):
        return {"status": "partial", "subject": "h-aptitude", "note": "Aptitude and Soft Skills covers part of this at placement level"}
    if sid == "english":
        return {"status": "partial", "subject": "e-english", "note": "Communicative English covers grammar and comprehension"}
    if sid == "physics":
        return {"status": "partial", "subject": "s-physics", "note": "Engineering Physics starts above this level; not a substitute"}
    if sid == "chemistry":
        return {"status": "partial", "subject": "s-chem", "note": "Engineering Chemistry starts above this level; not a substitute"}
    if sid == "maths":
        return {"status": "partial", "subject": "m-calculus", "note": "Calculus, Linear Algebra and Probability re-teach parts at degree level"}
    return {"status": "none"}

def export_topic(sid, t):
    ex = sorted(set(t["exams"]))
    return {"id": t["id"], "name": t["name"], "exams": ex, "exam_count": len(ex),
            "core_exam_count": len([e for e in ex if e in core_ids]),
            "ncert_11_12": ncert_info(sid, t), "btech_pack": btech_info(sid, t)}

uni_out = {"meta": {
    "built": str(TODAY),
    "what": "One merged syllabus per subject. Each topic lists the exams that use it and its overlap with (a) NCERT class 11-12, covered by CBSE Free N Easy, and (b) the B.Tech universal syllabus (pack/universal.json).",
    "depth": "School and aptitude subjects go subject > unit > topic. B.Tech and degree subjects go subject > B.Tech subject > unit, taken from pack/universal.json; their subtopics stay in that file.",
    "caution": "Exam-to-topic mapping is by syllabus family at unit level (see build/topics_src.py). Check it line by line against each 2027 bulletin before a book is written.",
    "gate_papers_not_in_btech_pack": T.GATE_UNMAPPED,
    "gate_paper_to_btech_subjects": T.GATE_MAP,
}, "subjects": []}
for s in subjects:
    uni_out["subjects"].append({"id": s["id"], "name": s["name"], "units": [
        {"id": u["id"], "name": u["name"], "class": u["class"], "topics": [export_topic(s["id"], t) for t in u["topics"]]}
        for u in s["units"]]})
uni_out["subjects"].append({"id": "btech", "name": "B.Tech and degree subjects (from the B.Tech data pack)", "units": [
    {"id": u["id"], "name": u["name"], "class": "UG", "dept": u["dept"], "topics": [export_topic("btech", t) for t in u["topics"]]}
    for u in sorted(bt_units.values(), key=lambda x: (x["dept"] or "", x["name"]))]})
uni_out["subjects"].append({"id": "own", "name": "Exam-specific subjects (no shared syllabus built yet)", "units": [
    {"id": u["id"], "name": u["name"], "class": "-", "topics": [export_topic("own", t) for t in u["topics"]]}
    for u in own_units.values()]})
n_topics = sum(len(u["topics"]) for s in uni_out["subjects"] for u in s["units"])
uni_out["meta"]["counts"] = {s["id"]: {"units": len(s["units"]), "topics": sum(len(u["topics"]) for u in s["units"])} for s in uni_out["subjects"]}
uni_out["meta"]["counts"]["total_topics"] = n_topics

# ---------------------------------------------------------------- exams
def src(key):
    url, yr = E.SRC[key]
    return {"url": url, "year": yr if yr else "latest bulletin; not re-read on 2026-11-13"}

def tfactor(target):
    if not target:
        return 0.8, None
    days = (datetime.date.fromisoformat(target) - TODAY).days
    if days < 45: f = 0.2
    elif days < 90: f = 0.6
    elif days <= 240: f = 1.0
    else: f = 0.8
    return f, days

exams = []
for r in E.ROWS:
    picked = exam_topics[r["id"]]
    ids = [t["id"] for _, _, t in picked]
    n = len(ids)
    def info(t):
        sid = t["id"].split(":")[0]
        return sid, t
    covered = shared1 = shared3 = n_ncert = n_bt = 0
    for _, _, t in picked:
        sid = t["id"].split(":")[0]
        others = [e for e in set(t["exams"]) if e != r["id"] and e in core_ids]
        nc = sid not in ("btech", "own") and ncert_info(sid, t)["status"] == "in"
        bt = "btech_ref" in t
        n_ncert += nc; n_bt += bt
        covered += (nc or bt)
        shared1 += (len(others) >= 1)
        shared3 += (len(others) >= 3)
    S = round(0.5 * covered / n + 0.5 * shared3 / n, 3) if n else 0.0
    c = r["cand"]
    c_lakh = (c["registered"] or c["appeared"]) / 1e5 if c.get("verified") else c.get("estimate_lakh")
    Tf, days = tfactor(r["d"]["target"])
    cap = S_CAP.get(r["id"])
    S_raw = S
    if cap is not None and S > cap[0]:
        S = cap[0]
    family = r["id"] in FAMILY
    score = None if (c_lakh is None or family) else round(c_lakh * r["U"] * S * Tf, 2)
    tree = collections.OrderedDict()
    for sname, uname, t in picked:
        tree.setdefault(sname, collections.OrderedDict()).setdefault(uname, []).append(t["name"])
    d = r["d"]; p = r["pattern"]
    tq = sum(x["questions"] for x in p["sections"] if x["questions"]) or None
    tm = sum(x["marks"] for x in p["sections"] if x["marks"]) or None
    cand = {k: c[k] for k in ("registered", "appeared", "year", "verified", "note")}
    if "estimate_lakh" in c: cand["estimate_lakh"] = c["estimate_lakh"]
    cand["source"] = src(c["src"])
    exams.append({
        "id": r["id"], "name": r["name"], "conducting_body": r["body"],
        "group": r["group"], "level": r["level"], "stream": r["stream"], "scope": r["scope"], "state": r["state"],
        "eligibility": r["eligibility"],
        "dates_2027": {"month": d["month"], "dates": d["dates"], "status": d["status"], "basis": d["basis"],
                       "target_date_for_scoring": d["target"], "days_from_2026_11_13": days, "source": src(d["src"])},
        "mode": r["mode"], "languages": r["languages"],
        "pattern": {"sections": p["sections"], "total_questions": tq, "total_marks": tm,
                    "negative_marking": p["negative_marking"], "duration_minutes": p["duration_minutes"],
                    "note": p["note"], "verified": p["verified"], "source": src(p["src"])},
        "candidates": cand,
        "seats": {"text": r["seats"]["text"], "value": r["seats"]["value"], "year": r["seats"]["year"],
                  "verified": r["seats"]["verified"], "source": src(r["seats"]["src"])},
        "syllabus": {"official_link": E.SRC[r["syllabus_src"]][0],
                     "topic_count": n, "tree": tree},
        "previous_papers_official": {"published": r["pyq"][0], "note": r["pyq"][1]},
        "overlap": {"topics": n, "shared_with_another_core_exam": shared1, "shared_with_3_or_more_core_exams": shared3,
                    "in_ncert_11_12": n_ncert, "in_btech_pack": n_bt},
        "priority": {"candidates_lakh": None if c_lakh is None else round(c_lakh, 2),
                     "candidates_basis": "read this session" if c.get("verified") else ("estimate" if c_lakh is not None else "not researched"),
                     "underserved_0_to_1": r["U"], "shared_0_to_1": S, "shared_before_cap": S_raw,
                     "shared_cap_reason": cap[1] if cap else None, "time_factor": Tf, "score": score,
                     "not_scored_reason": ("a family of state exams; needs a state-by-state pass first" if family else ("candidate count not researched" if c_lakh is None else None))},
        "note": r["note"],
    })

core_all = [e for e in exams if e["group"] == "core"]
core = sorted([e for e in core_all if e["priority"]["score"] is not None], key=lambda e: -e["priority"]["score"])
for i, e in enumerate(core, 1):
    e["priority"]["rank_in_core"] = i
for g in ("optional_govt_jobs", "optional_study_abroad"):
    for i, e in enumerate(sorted([e for e in exams if e["group"] == g and e["priority"]["score"] is not None], key=lambda e: -e["priority"]["score"]), 1):
        e["priority"]["rank_in_group"] = i

exams_out = {"meta": {
    "built": str(TODAY), "exam_count": len(exams),
    "groups": {"core": "Entrance exams for admission", "optional_govt_jobs": "Optional group: government job exams", "optional_study_abroad": "Optional group: study-abroad tests"},
    "levels": {"10th": "After class 10 (and school-stage tests the brief groups here)", "12th": "After class 12", "UG": "After a bachelor's degree"},
    "how_to_read_sources": "Every number carries a source URL and its year. verified=true means the figure was read from that page on 13 November 2026. verified=false means it comes from the latest bulletin as remembered or is an estimate; the URL is then the official site where it must be checked.",
    "date_status": {"announced": "date published by the conducting body (often marked tentative)", "expected": "not announced; inferred from the last two cycles", "year_round": "offered through the year"},
    "priority_formula": "score = candidates (lakh) x underserved (0-1, editorial estimate) x shared (0-1, computed) x time factor. shared = half the share of the exam's topics already in NCERT 11-12 or the B.Tech pack, plus half the share used by 3 or more other core exams. time factor from days between 13 November 2026 and the last sitting of the 2027 cycle: under 45 days 0.2, 45-89 days 0.6, 90-240 days 1.0, over 240 days 0.8.",
}, "exams": exams}

json.dump(exams_out, open(os.path.join(OUT, "exams.json"), "w"), indent=1, ensure_ascii=False)
json.dump(uni_out, open(os.path.join(OUT, "universal_topics.json"), "w"), indent=1, ensure_ascii=False)

# compact data for the map page
mapdata = [{
    "id": e["id"], "n": e["name"], "b": e["conducting_body"], "g": e["group"], "l": e["level"], "s": e["stream"], "sc": e["scope"], "st": e["state"],
    "m": e["dates_2027"]["month"], "d": e["dates_2027"]["dates"], "ds": e["dates_2027"]["status"], "du": e["dates_2027"]["source"]["url"],
    "c": e["priority"]["candidates_lakh"], "cv": e["candidates"]["verified"], "cy": e["candidates"]["year"], "cn": e["candidates"]["note"], "cu": e["candidates"]["source"]["url"],
    "t": e["overlap"]["topics"], "sh": e["overlap"]["shared_with_another_core_exam"], "nc": e["overlap"]["in_ncert_11_12"], "bt": e["overlap"]["in_btech_pack"],
    "U": e["priority"]["underserved_0_to_1"], "S": e["priority"]["shared_0_to_1"], "T": e["priority"]["time_factor"], "p": e["priority"]["score"],
    "r": e["priority"].get("rank_in_core"), "sy": e["syllabus"]["official_link"], "py": e["previous_papers_official"]["published"],
    "pt": {"q": e["pattern"]["total_questions"], "mk": e["pattern"]["total_marks"], "du": e["pattern"]["duration_minutes"], "ng": e["pattern"]["negative_marking"]},
    "md": e["mode"],
} for e in exams]
json.dump(mapdata, open(os.path.join(HERE, "map_data.json"), "w"), ensure_ascii=False, separators=(",", ":"))

# ---------------------------------------------------------------- console summary
print("exams", len(exams), "core", len(core_all), "scored core", len(core), "| topics", n_topics)
print("counts", {k: v for k, v in uni_out["meta"]["counts"].items()})
print("verified candidate counts:", sum(1 for e in exams if e["candidates"]["verified"]))
print("announced dates:", sum(1 for e in exams if e["dates_2027"]["status"] == "announced"))
print("\nTOP 25 core by score")
for e in core[:25]:
    p = e["priority"]; o = e["overlap"]
    print(f"{p['rank_in_core']:>2} {e['id']:<16} C={p['candidates_lakh']:>6} U={p['underserved_0_to_1']} S={p['shared_0_to_1']} T={p['time_factor']} score={p['score']:>5} topics={o['topics']} shared={o['shared_with_another_core_exam']} ncert={o['in_ncert_11_12']} bt={o['in_btech_pack']} {'ok' if e['candidates']['verified'] else 'EST'}")

top10 = [e["id"] for e in core[:10]]
print("\ntop10", top10)
# production counts for the report
def stat(sid, used_by):
    s = [x for x in uni_out["subjects"] if x["id"] == sid][0]
    units = topics = out = 0
    for u in s["units"]:
        tt = [t for t in u["topics"] if set(t["exams"]) & set(used_by)]
        if tt: units += 1
        topics += len(tt)
        out += len([t for t in tt if t["ncert_11_12"].get("status") == "out"])
    return units, topics, out
for sid in ("physics", "chemistry", "maths", "biology", "f_maths", "f_science", "quant", "reasoning", "english", "gk", "commerce", "humanities"):
    print(sid, "units/topics/outside-NCERT used by top10:", stat(sid, top10))
unm = {"AG":2985,"AR":10673,"EY":3659,"GE":3582,"GG":5647+668,"MN":8415,"NM":548,"PE":1428,"TF":1549,"XH":4166+5350+383+800+8858+2643}
print("GATE unmapped registrations", sum(unm.values()), round(100*sum(unm.values())/1011719,1), "%")
print("optional:", [(e["id"], e["priority"]["score"]) for e in exams if e["group"]!="core"])
