# Source rows for exams.json. Research date: 13 November 2026.
#
# verified=True  : the figure was read this session from the page at the source URL.
# verified=False : carried from the latest official bulletin as remembered, or an estimate;
#                  the source URL is then the official site where it must be checked.

SRC = {
    # --- read this session ---
    "jm27": ("https://news.careers360.com/jee-main-2027-notification-out-registration-begins-jeemain-nta-nic-in-session-1-exam-dates-eligbility-registration-fee", 2026),
    "jm26": ("https://collegedunia.com/news/how-many-students-appeared-for-jee-main-2026-alertid-150907", 2026),
    "adv26": ("https://collegedunia.com/exams/jee-advanced", 2026),
    "adv27": ("https://msmunify.com/in/exams/jee-advanced", 2026),
    "neet26": ("https://news.careers360.com/neet-ug-2026-result-highlights-absentees-surge-qualifiers-fall-cut-offs-rise-toppers-list", 2026),
    "neet27": ("https://www.msmunify.com/in/exams/neet-ug", 2026),
    "neetseats": ("https://www.aspirantmitraa.com/exams/neet-ug", 2026),
    "cuet26": ("https://www.msmunify.com/in/exams/cuet-ug", 2026),
    "gate27": ("https://gate2027.iitm.ac.in/important_dates", 2026),
    "gate26": ("https://articles.findmycollege.com/news/gate-2026-statistical-report-out-19-6-pass-rate-cs-highest-density/", 2026),
    "cat26": ("https://www.collegedekho.com/amp/news/cat-2026-registrations-count-dipped-trends-80231/", 2026),
    "cat26d": ("https://www.imsindia.com/?p=16802", 2026),
    "clat27": ("https://consortiumofnlus.ac.in/clat-2026/notifications/Press_Release_CLAT_2027.pdf", 2026),
    "clat27b": ("https://law.careers360.com/articles/clat-2027-exam-date", 2026),
    "mhtpcm": ("https://cetcell.mahacet.org/wp-content/uploads/2026/06/Press-Note-MHT-CET-PCM-Group-1st-Attempt_-2026.pdf", 2026),
    "mhtpcb": ("https://cetcell.mahacet.org/wp-content/uploads/2026/06/Notification_PCB_1st-Attempt-Result.pdf", 2026),
    "mhall": ("https://news.careers360.com/maharashtra-cet-2026-records-highest-ever-participation-with-16-29-lakh-mat-pcm-pcb-mba-mms-20-entrance-exam-statistics", 2026),
    "tgeap": ("https://telanganatoday.com/medchal-girl-and-hyderabad-boy-top-tg-eapcet-2026-results", 2026),
    "apeap": ("https://news.careers360.com/ap-eacmet-toppers-2026-jonnala-roshan-manideep-reddy-btech-sambangi-jaswanth-naidu-bharm-bagri-eapcet-apsche", 2026),
    "kcet26": ("https://www.freepressjournal.in/education/kcet-ugcet-result-2026-out-female-candidates-outnumber-male-students-by-over-41000", 2026),
    "wbjee26": ("https://news.careers360.com/wbjee-toppers-list-2026-merit-list-out-wbjeeb-nic-in-shaswat-banerjee-tops-exam-btech-engineering-admissions-counselling", 2026),
    "gujcet26": ("https://www.freepressjournal.in/amp/education/gujcet-2026-result-out-1459-students-score-above-99-percentile-rank", 2026),
    "ntacal": ("https://www.careerpower.in/blog/wp-content/uploads/2026/09/16212531/NTA_Exam_Calendar.pdf", 2026),
    "ntarev": ("https://news.careers360.com/nta-revises-exam-calendar-jee-mains-session-1-dates-ugc-net-joint-csir-cuet-pg-cmat-neet", 2026),
    "upsc27": ("https://www.studyiq.com/articles/upsc-exam-calendar-2027/", 2026),
    "appoly": ("https://deccanchronicle.com/southern-states/andhra-pradesh/girls-outperform-boys-in-ap-polycet-exam-1954737", 2026),
    "aissee26": ("https://competitivecracker.com/blog/aissee-sainik-school-result-2026-out", 2026),
    "aisseeseats": ("https://sarkariresultforum.com/2025/sainik-schools-entrance-examination-2026", 2026),
    "cuetpg26": ("https://www.freepressjournal.in/education/cuet-pg-2026-result-out-over-345-lakh-candidates-appeared-in-exam-conducted-across-50-shifts", 2026),
    "nift26": ("https://pahaldesign.com/tag/nift-result-2026/", 2026),
    "nid23": ("https://design.careers360.com/articles/how-many-students-appeared-for-nid-dat-2026", 2023),
    "nidseats": ("https://design.careers360.com/articles/how-many-students-appeared-for-nid-bdes-studio-test-2026", 2026),
    "exams26": ("https://jeecounselling.in/exam-calendar", 2026),
    # --- official sites (for figures not re-read this session) ---
    "o_jm": ("https://jeemain.nta.nic.in/", None), "o_adv": ("https://jeeadv.ac.in/", None),
    "o_neet": ("https://neet.nta.nic.in/", None), "o_cuet": ("https://cuet.nta.nic.in/", None),
    "o_bits": ("https://www.bitsadmission.com/", None), "o_vit": ("https://viteee.vit.ac.in/", None),
    "o_srm": ("https://www.srmist.edu.in/admission-india/", None), "o_met": ("https://www.manipal.edu/", None),
    "o_comedk": ("https://www.comedk.org/", None), "o_kiit": ("https://kiitee.kiit.ac.in/", None),
    "o_amrita": ("https://www.amrita.edu/admissions/", None),
    "o_mh": ("https://cetcell.mahacet.org/", None), "o_kea": ("https://cetonline.karnataka.gov.in/kea/", None),
    "o_tgeap": ("https://eapcet.tgche.ac.in/", None), "o_apeap": ("https://cets.apsche.ap.gov.in/", None),
    "o_wbjee": ("https://wbjeeb.nic.in/", None), "o_keam": ("https://cee.kerala.gov.in/", None),
    "o_gujcet": ("https://gujcet.gseb.org/", None), "o_ojee": ("https://ojee.nic.in/", None),
    "o_cusat": ("https://admissions.cusat.ac.in/", None), "o_assam": ("https://astu.ac.in/", None),
    "o_jkcet": ("https://www.jkbopee.gov.in/", None), "o_cgpet": ("https://vyapamcg.cgstate.gov.in/", None),
    "o_goa": ("https://dte.goa.gov.in/", None), "o_tjee": ("https://tbjee.nic.in/", None),
    "o_bcece": ("https://bceceboard.bihar.gov.in/", None), "o_ipu": ("https://ipu.ac.in/", None),
    "o_amu": ("https://www.amucontrollerexams.com/", None),
    "o_clat": ("https://consortiumofnlus.ac.in/", None), "o_ailet": ("https://nationallawuniversitydelhi.in/", None),
    "o_slat": ("https://www.set-test.org/", None),
    "o_nid": ("https://admissions.nid.edu/", None), "o_nift": ("https://exams.nta.ac.in/NIFT/", None),
    "o_uceed": ("https://www.uceed.iitb.ac.in/", None), "o_nata": ("https://www.nata.in/", None),
    "o_ipmat": ("https://www.iimidr.ac.in/", None), "o_ipmr": ("https://www.iimrohtak.ac.in/", None),
    "o_jipmat": ("https://exams.nta.ac.in/JIPMAT/", None), "o_npat": ("https://www.nmims.edu/", None),
    "o_upsc": ("https://upsc.gov.in/", None), "o_nchm": ("https://exams.nta.ac.in/NCHM/", None),
    "o_icar": ("https://icar.org.in/", None), "o_nest": ("https://www.nestexam.in/", None),
    "o_iat": ("https://iiseradmission.in/", None), "o_isi": ("https://www.isical.ac.in/", None),
    "o_cmi": ("https://www.cmi.ac.in/admissions/", None), "o_icai": ("https://www.icai.org/", None),
    "o_ncet": ("https://exams.nta.ac.in/NCET/", None), "o_aiims": ("https://www.aiimsexams.ac.in/", None),
    "o_imu": ("https://www.imu.edu.in/", None),
    "o_appoly": ("https://polycetap.nic.in/", None), "o_tgpoly": ("https://www.polycet.sbtet.telangana.gov.in/", None),
    "o_jeecup": ("https://jeecup.admissions.nic.in/", None), "o_delhicet": ("https://tte.delhi.gov.in/", None),
    "o_jexpo": ("https://webscte.co.in/", None), "o_ubter": ("https://ubter.in/", None),
    "o_jceceb": ("https://jceceb.jharkhand.gov.in/", None), "o_dteassam": ("https://dte.assam.gov.in/", None),
    "o_hptsb": ("https://www.hptechboard.com/", None),
    "o_aissee": ("https://exams.nta.nic.in/sainik-school-society/", None),
    "o_rms": ("https://www.rashtriyamilitaryschools.edu.in/", None), "o_rimc": ("https://rimc.gov.in/", None),
    "o_ncert": ("https://ncert.nic.in/", None), "o_nvs": ("https://navodaya.gov.in/", None),
    "o_hbcse": ("https://olympiads.hbcse.tifr.res.in/", None), "o_scholar": ("https://scholarships.gov.in/", None),
    "o_cat": ("https://iimcat.ac.in/", None), "o_xat": ("https://xatonline.in/", None),
    "o_cmat": ("https://exams.nta.ac.in/CMAT/", None), "o_snap": ("https://www.snaptest.org/", None),
    "o_nmat": ("https://www.mba.com/exams/nmat", None), "o_mat": ("https://mat.aima.in/", None),
    "o_tancet": ("https://tancet.annauniv.edu/", None), "o_apicet": ("https://cets.apsche.ap.gov.in/", None),
    "o_tgicet": ("https://icet.tgche.ac.in/", None),
    "o_cuetpg": ("https://exams.nta.ac.in/CUET-PG/", None), "o_jam": ("https://jam.iitb.ac.in/", None),
    "o_nbe": ("https://natboard.edu.in/", None), "o_ugcnet": ("https://ugcnet.nta.ac.in/", None),
    "o_csir": ("https://csirnet.nta.ac.in/", None), "o_nimcet": ("https://www.nimcet.admissions.nic.in/", None),
    "o_ceed": ("https://www.ceed.iitb.ac.in/", None), "o_jest": ("https://www.jest.org.in/", None),
    "o_tifr": ("https://univ.tifr.res.in/", None), "o_gatb": ("https://exams.nta.ac.in/DBT/", None),
    "o_upbed": ("https://www.bujhansi.ac.in/", None), "o_ctet": ("https://ctet.nic.in/", None),
    "o_bci": ("https://www.barcouncilofindia.org/", None), "o_pgecet": ("https://cets.apsche.ap.gov.in/", None),
    "o_ssc": ("https://ssc.gov.in/", None), "o_ibps": ("https://www.ibps.in/", None),
    "o_sbi": ("https://sbi.co.in/web/careers", None), "o_rbi": ("https://opportunities.rbi.org.in/", None),
    "o_rrb": ("https://www.rrbcdg.gov.in/", None), "o_afcat": ("https://afcat.cdac.in/", None),
    "o_agni": ("https://joinindianarmy.nic.in/", None),
    "o_sat": ("https://satsuite.collegeboard.org/sat", None), "o_act": ("https://www.act.org/", None),
    "o_gre": ("https://www.ets.org/gre.html", None), "o_gmat": ("https://www.mba.com/exams/gmat-exam", None),
    "o_ielts": ("https://ielts.org/", None), "o_toefl": ("https://www.ets.org/toefl.html", None),
    "o_pte": ("https://www.pearsonpte.com/", None), "o_det": ("https://englishtest.duolingo.com/", None),
    "o_lsat": ("https://www.lsac.org/", None),
}

ROWS = []


def D(month, dates, status, target, src, basis=""):
    """2027 cycle date. status: announced | expected | year_round."""
    return {"month": month, "dates": dates, "status": status, "target": target, "src": src, "basis": basis}


def P(sections, neg, dur, src, note="", verified=False):
    import re
    secs = []
    for m in re.finditer(r"\s*(.+?):(\d*):([\d.]*)\s*(?:,|$)", sections):
        secs.append({"name": m.group(1).strip(),
                     "questions": int(m.group(2)) if m.group(2) else None,
                     "marks": float(m.group(3)) if m.group(3) else None})
    return {"sections": secs, "negative_marking": neg, "duration_minutes": dur, "src": src,
            "note": note, "verified": verified}


def C(reg, app, yr, src, note=""):
    return {"registered": reg, "appeared": app, "year": yr, "src": src, "verified": True, "note": note}


def EST(lakh, yr, src, note):
    return {"registered": None, "appeared": None, "year": yr, "src": src, "verified": False,
            "estimate_lakh": lakh, "note": note}


def SE(text, src, yr=None, verified=False, value=None):
    return {"text": text, "value": value, "year": yr, "src": src, "verified": verified}


def X(id, name, body, level, stream, scope, elig, d, mode, langs, pat, cand, seats, syl, pyq, U, prof,
      group="core", state=None, note=""):
    ROWS.append(dict(id=id, name=name, body=body, level=level, stream=stream, scope=scope, eligibility=elig,
                     d=d, mode=mode, languages=langs, pattern=pat, cand=cand, seats=seats, syllabus_src=syl,
                     pyq=pyq, U=U, prof=prof, group=group, state=state, note=note))


L13 = "13 languages (English, Hindi, Assamese, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Urdu)"
PCM12 = "Class 12 pass or appearing with Physics, Chemistry and Mathematics"
PCB12 = "Class 12 pass or appearing with Physics, Chemistry and Biology"
ANY12 = "Class 12 pass or appearing, any stream"
GRAD = "Bachelor's degree (final-year students may apply)"
C10 = "Class 10 pass or appearing"
PJ = {"physics": "J", "chemistry": "J", "maths": "J"}
PS = {"physics": "S", "chemistry": "S", "maths": "S"}
PSB = {"physics": "S", "chemistry": "S", "maths": "S", "biology": "S"}
APT = {"quant": "*", "reasoning": "*", "english": "*"}
APTG = {"quant": "*", "reasoning": "*", "english": "*", "gk": "*"}
POLY = {"f_maths": "*", "f_science": ["Physics (class 9-10)", "Chemistry (class 9-10)"]}

# ---------------------------------------------------------------- AFTER 12TH: ENGINEERING
X("jee-main", "JEE Main (Paper 1, B.E./B.Tech)", "National Testing Agency (NTA)", "12th", "Engineering", "national",
  PCM12 + "; no age limit; 3 consecutive years of attempts",
  D("January and April 2027", "Session 1: 20, 21, 22, 23, 24 and 28 January 2027 (announced). Session 2: April 2027 (in NTA's revised calendar; exact days not read this session)", "announced", "2027-04-05", "jm27",
    "NTA notification of 24 October 2026; 2026 Session 2 ran 2-8 April"),
  "Computer-based test", L13,
  P("Physics:25:100, Chemistry:25:100, Mathematics:25:100", "+4 / -1 (MCQ and numerical)", 180, "o_jm",
    "Each subject: 20 MCQ + 5 numerical, all compulsory (pattern since 2025)"),
  C(1604854, 1538468, 2026, "jm26", "Unique candidates over both sessions; Session 1 alone 13,55,293 registered"),
  SE("JoSAA 2026: 67,323 seats in 138 institutes (IITs, NITs, IIITs, GFTIs); also the base score for many state and private admissions", "adv26", 2026, True, 67323),
  "o_jm", (True, "NTA publishes question papers with answer keys after each session"), 0.30, PJ)

X("jee-main-p2", "JEE Main (Paper 2A B.Arch, 2B B.Planning)", "National Testing Agency (NTA)", "12th", "Design and Architecture", "national",
  "Class 12 with Mathematics (B.Planning) or with Physics, Chemistry and Mathematics (B.Arch)",
  D("January and April 2027", "With JEE Main sessions (January announced, April expected)", "announced", "2027-04-05", "jm27", "Runs with JEE Main"),
  "Computer-based test; drawing part on paper", L13,
  P("Mathematics:25:100, Aptitude:50:200, Drawing (2A) or Planning (2B):2:100", "+4 / -1", 180, "o_jm", "2A: 77 questions, 400 marks; 2B: 100 questions, 400 marks"),
  EST(0.55, 2026, "o_jm", "About 45,000 appeared for B.Arch in Session 1 of 2026 (secondary report); unique two-session total not read"),
  SE("B.Arch and B.Planning seats at NITs, SPAs and GFTIs through JoSAA", "o_jm"),
  "o_jm", (True, "Published by NTA"), 0.60, {"maths": "J", "design": ["Architecture Aptitude"]})

X("jee-adv", "JEE Advanced", "IITs (organising institute for 2027 expected: IIT Delhi)", "12th", "Engineering", "national",
  "Top 2,50,000 in JEE Main; 2 attempts in consecutive years",
  D("May 2027", "Not announced; expected mid to late May 2027", "expected", "2027-05-16", "adv27", "17 May 2026 and 18 May 2025"),
  "Computer-based test, two papers on one day", "English and Hindi",
  P("Paper 1 (Physics, Chemistry, Mathematics)::180, Paper 2 (Physics, Chemistry, Mathematics)::180", "Varies by question type; partial marking", 360, "o_adv",
    "360 marks in 2026; number and type of questions change each year"),
  C(187389, 179694, 2026, "adv26", "56,880 qualified"),
  SE("About 18,000 seats in 23 IITs", "adv26", 2026, False),
  "o_adv", (True, "All past papers and solutions on jeeadv.ac.in"), 0.30, {"physics": "A", "chemistry": "A", "maths": "A"})

X("bitsat", "BITSAT", "BITS Pilani", "12th", "Engineering", "private", PCM12 + " (PCB for B.Pharm), 75% aggregate",
  D("April and May 2027", "Not announced; expected mid April (Session 1) and late May (Session 2)", "expected", "2027-05-24", "exams26", "2026: 15-16 April and 24-26 May"),
  "Computer-based test", "English",
  P("Physics:30:90, Chemistry:30:90, English Proficiency:10:30, Logical Reasoning:20:60, Mathematics or Biology:40:120", "+3 / -1", 180, "o_bits"),
  EST(2.0, 2025, "o_bits", "BITS does not publish a count; press reports put it near 2 lakh"),
  SE("Pilani, Goa and Hyderabad campuses, about 3,000 first-degree seats", "o_bits"),
  "o_bits", (False, "No official papers; the test is not released"), 0.45, {**PS, "english": "*", "reasoning": "*"})

X("viteee", "VITEEE", "Vellore Institute of Technology", "12th", "Engineering", "private", PCM12 + " or PCB",
  D("April 2027", "Not announced; expected late April 2027", "expected", "2027-04-28", "exams26", "2026: 28 April to 3 May"),
  "Computer-based test", "English",
  P("Mathematics or Biology:40:40, Physics:35:35, Chemistry:35:35, Aptitude:10:10, English:5:5", "None", 150, "o_vit"),
  EST(2.5, 2025, "o_vit", "Not published; estimate"), SE("VIT Vellore, Chennai, AP and Bhopal campuses", "o_vit"),
  "o_vit", (False, "Sample papers only"), 0.50, {**PS, "english": "*", "quant": ["Arithmetic", "Data Interpretation"]})

X("srmjeee", "SRMJEEE", "SRM Institute of Science and Technology", "12th", "Engineering", "private", PCM12 + " or PCB",
  D("April to June 2027", "Not announced; phases expected April and June 2027", "expected", "2027-04-22", "exams26", "2026 phase 1 in April"),
  "Remote proctored online test", "English",
  P("Physics:35:35, Chemistry:35:35, Mathematics or Biology:40:40, English:5:5, Aptitude:10:10", "None", 150, "o_srm"),
  EST(1.5, 2025, "o_srm", "Not published; estimate"), SE("SRM campuses", "o_srm"),
  "o_srm", (False, "Model papers only"), 0.50, {**PS, "english": "*", "quant": ["Arithmetic"]})

X("met", "Manipal Entrance Test (MET)", "Manipal Academy of Higher Education", "12th", "Engineering", "private", PCM12,
  D("April and May 2027", "Not announced; expected April and May 2027", "expected", "2027-04-18", "exams26", "2026 in April"),
  "Computer-based test", "English", P("Physics:15:60, Chemistry:15:60, Mathematics:20:80, English:10:40", "+4 / -1 for MCQ", 120, "o_met"),
  EST(0.5, 2025, "o_met", "Not published; estimate"), SE("MIT Manipal, Bengaluru and other Manipal campuses", "o_met"),
  "o_met", (False, "Not published"), 0.50, {**PS, "english": "*"})

X("comedk", "COMEDK UGET", "Consortium of Medical, Engineering and Dental Colleges of Karnataka", "12th", "Engineering", "state", PCM12,
  D("May 2027", "Not announced; expected second Saturday of May 2027", "expected", "2027-05-08", "exams26", "9 May 2026"),
  "Computer-based test", "English", P("Physics:60:60, Chemistry:60:60, Mathematics:60:60", "None", 180, "o_comedk"),
  EST(1.3, 2025, "o_comedk", "About 1.3 lakh registered in 2025 as remembered; not re-read"),
  SE("About 150 private engineering colleges in Karnataka", "o_comedk"),
  "o_comedk", ("partial", "Question paper and key released after the test for objections"), 0.60, PS, state="Karnataka")

X("kiitee", "KIITEE", "KIIT University", "12th", "Engineering", "private", PCM12,
  D("April 2027", "Not announced; phase 1 expected April 2027", "expected", "2027-04-16", "exams26", "2026 in April"),
  "Computer-based test", "English", P("Physics:40:160, Chemistry:40:160, Mathematics:40:160", "+4 / -1", 180, "o_kiit"),
  EST(1.0, 2025, "o_kiit", "Not published; estimate"), SE("KIIT Bhubaneswar", "o_kiit"), "o_kiit", (False, "Not published"), 0.55, PS)

X("aeee", "Amrita AEEE", "Amrita Vishwa Vidyapeetham", "12th", "Engineering", "private", PCM12,
  D("January to May 2027", "Not announced; phases expected between January and May 2027", "expected", "2027-05-01", "o_amrita", "Earlier cycles"),
  "Computer-based test", "English", P("Mathematics:40:120, Physics:30:90, Chemistry:25:75, English:5:15", "+3 / -1", 150, "o_amrita"),
  EST(0.8, 2025, "o_amrita", "Not published; estimate"), SE("Amrita campuses", "o_amrita"), "o_amrita", (False, "Not published"), 0.55, {**PS, "english": "*"})

X("mht-cet", "MHT CET (PCM and PCB groups)", "State Common Entrance Test Cell, Maharashtra", "12th", "Engineering", "state",
  "Class 12 with PCM (engineering) or PCB (pharmacy, agriculture)",
  D("April and May 2027", "Not announced; expected April 2027 (first attempt) and May 2027 (second attempt)", "expected", "2027-04-12", "o_mh",
    "2026: PCM 11-20 April, PCB 21-26 April; second attempts 10-21 May"),
  "Computer-based test", "English, Marathi and Urdu (Mathematics in English only)",
  P("Mathematics or Biology:50:100, Physics:50:50, Chemistry:50:50", "None", 180, "o_mh", "20% class 11 and 80% class 12, Maharashtra board syllabus"),
  C(763395, 717282, 2026, "mhtpcm", "First attempt: PCM 4,79,332 registered (4,54,069 appeared) plus PCB 2,84,063 (2,63,213), from the CET Cell press notes; some candidates sit both groups"),
  SE("Engineering, pharmacy and agriculture degree seats in Maharashtra", "o_mh"),
  "o_mh", ("partial", "CET Cell shows each candidate's own paper and key for objections; no full archive"), 0.70, PSB, state="Maharashtra")

X("kcet", "KCET (UGCET)", "Karnataka Examinations Authority", "12th", "Engineering", "state", "2nd PUC or class 12 with PCM or PCB; Karnataka domicile rules",
  D("April 2027", "Not announced; expected mid to late April 2027", "expected", "2027-04-22", "o_kea", "23-24 April 2026"),
  "Pen and paper (OMR)", "English and Kannada",
  P("Physics:60:60, Chemistry:60:60, Mathematics:60:60, Biology:60:60", "None", 320, "o_kea", "80 minutes per paper; candidates take PCM, PCB or all four"),
  C(330479, 309014, 2026, "kcet26", "One report gives 3,30,646 registered"),
  SE("Engineering, pharmacy, agriculture, veterinary and allied seats in Karnataka", "o_kea"),
  "o_kea", (True, "KEA publishes papers and answer keys"), 0.70, PSB, state="Karnataka")

X("tg-eapcet", "TG EAPCET (TS EAMCET)", "JNTU Hyderabad for TGCHE", "12th", "Engineering", "state", "Intermediate with MPC (engineering) or BiPC (agriculture and pharmacy)",
  D("May 2027", "Not announced; expected early May 2027", "expected", "2027-05-05", "o_tgeap", "2026: A and P 4-5 May, Engineering 9-11 May"),
  "Computer-based test", "English with Telugu or Urdu",
  P("Mathematics or Biology:80:80, Physics:40:40, Chemistry:40:40", "None", 180, "o_tgeap"),
  C(301743, 282195, 2026, "tgeap", "Engineering 2,10,766 registered; Agriculture and Pharmacy 90,977"),
  SE("Engineering, agriculture and pharmacy seats in Telangana", "o_tgeap"),
  "o_tgeap", (True, "Master question papers and keys are released"), 0.70, PSB, state="Telangana")

X("ap-eapcet", "AP EAPCET (AP EAMCET)", "JNTU Kakinada for APSCHE", "12th", "Engineering", "state", "Intermediate with MPC (engineering) or BiPC (agriculture and pharmacy)",
  D("May 2027", "Not announced; expected mid May 2027", "expected", "2027-05-15", "o_apeap", "12-20 May 2026"),
  "Computer-based test", "English with Telugu or Urdu",
  P("Mathematics or Biology:80:80, Physics:40:40, Chemistry:40:40", "None", 180, "o_apeap"),
  C(355803, 329474, 2026, "apeap", "Engineering 2,76,572 registered (2,58,545 appeared); Agriculture and Pharmacy 79,231 (70,929)"),
  SE("Engineering, agriculture and pharmacy seats in Andhra Pradesh", "o_apeap"),
  "o_apeap", (True, "Master question papers and keys are released"), 0.70, PSB, state="Andhra Pradesh")

X("wbjee", "WBJEE", "West Bengal Joint Entrance Examinations Board", "12th", "Engineering", "state", PCM12,
  D("April or May 2027", "Not announced; expected late April or May 2027", "expected", "2027-04-25", "o_wbjee", "24 May 2026 and 27 April 2025"),
  "Pen and paper (OMR)", "English and Bengali",
  P("Mathematics:75:100, Physics:40:50, Chemistry:40:50", "Category 1: +1 / -0.25; category 2: +2 / -0.5; category 3: +2, no negative", 240, "o_wbjee", "Two papers of 2 hours each"),
  C(120857, 94901, 2026, "wbjee26", "92,753 qualified"), SE("Engineering and pharmacy seats in West Bengal", "o_wbjee"),
  "o_wbjee", (True, "WBJEEB publishes papers and keys"), 0.70, PS, state="West Bengal")

X("keam", "KEAM", "Commissioner for Entrance Examinations, Kerala", "12th", "Engineering", "state", PCM12,
  D("April 2027", "Not announced; expected late April 2027", "expected", "2027-04-24", "o_keam", "April in 2025 and 2026"),
  "Computer-based test", "English", P("Mathematics:75:300, Physics:45:180, Chemistry:30:120", "+4 / -1", 180, "o_keam"),
  EST(1.0, 2025, "o_keam", "Roughly 1 lakh applied in 2025 as remembered; not re-read"), SE("Engineering and pharmacy seats in Kerala", "o_keam"),
  "o_keam", (True, "CEE publishes papers and keys"), 0.70, PS, state="Kerala")

X("gujcet", "GUJCET", "Gujarat Secondary and Higher Secondary Education Board", "12th", "Engineering", "state", "Class 12 science, group A (Maths) or B (Biology)",
  D("March 2027", "Not announced; expected late March 2027", "expected", "2027-03-28", "o_gujcet", "March 2026"),
  "Pen and paper (OMR)", "Gujarati, English and Hindi",
  P("Physics:40:40, Chemistry:40:40, Mathematics or Biology:40:40", "+1 / -0.25", 180, "gujcet26", "120 questions and the marking scheme read this session; duration from the bulletin as remembered", True),
  C(136071, 132319, 2026, "gujcet26"), SE("Degree engineering and pharmacy seats in Gujarat (with board marks)", "o_gujcet"),
  "o_gujcet", (True, "GSEB publishes papers and keys"), 0.75, PSB, state="Gujarat")

for _id, _nm, _body, _st, _src, _mon, _tgt, _note in [
    ("ojee", "OJEE", "Odisha Joint Entrance Examination Committee", "Odisha", "o_ojee", "May 2027", "2027-05-05", "B.Pharm, lateral entry, MBA and MCA; B.Tech in Odisha is through JEE Main"),
    ("cusat-cat", "CUSAT CAT", "Cochin University of Science and Technology", "Kerala", "o_cusat", "May 2027", "2027-05-10", "University's own B.Tech and other programmes"),
    ("assam-cee", "Assam CEE", "Assam Science and Technology University", "Assam", "o_assam", "May or June 2027", "2027-05-30", "State engineering colleges of Assam"),
    ("jkcet", "JKCET", "J&K Board of Professional Entrance Examinations", "Jammu and Kashmir", "o_jkcet", "April or May 2027", "2027-05-01", "Engineering colleges of J&K"),
    ("cg-pet", "CG PET", "Chhattisgarh Professional Examination Board", "Chhattisgarh", "o_cgpet", "May 2027", "2027-05-10", "Engineering colleges of Chhattisgarh"),
    ("gcet", "Goa CET", "Directorate of Technical Education, Goa", "Goa", "o_goa", "May 2027", "2027-05-10", "Engineering and pharmacy in Goa"),
    ("tjee", "Tripura JEE", "Tripura Board of Joint Entrance Examination", "Tripura", "o_tjee", "April 2027", "2027-04-25", "Engineering, agriculture and allied seats in Tripura"),
    ("bcece", "BCECE", "Bihar Combined Entrance Competitive Examination Board", "Bihar", "o_bcece", "June or July 2027", "2027-06-20", "Pharmacy, agriculture and paramedical; Bihar engineering is through JEE Main"),
    ("ipu-cet", "IPU CET", "Guru Gobind Singh Indraprastha University", "Delhi", "o_ipu", "April or May 2027", "2027-05-01", "Many programmes; B.Tech is through JEE Main"),
    ("amueee", "AMU Engineering Entrance", "Aligarh Muslim University", "Uttar Pradesh", "o_amu", "May 2027", "2027-05-15", "AMU B.Tech"),
]:
    X(_id, _nm, _body, "12th", "Engineering", "state", "Class 12 with PCM or PCB as the course needs; state domicile rules",
      D(_mon, "Not announced; month from earlier cycles", "expected", _tgt, _src, "Earlier cycles; not re-read this session"),
      "See bulletin", "English (and state language where offered)",
      P("Physics, Chemistry, Mathematics or Biology::", "See bulletin", None, _src, "Pattern not researched this session"),
      EST(None, 2025, _src, "Candidate count not researched this session"), SE(_note, _src),
      _src, ("partial", "Not checked"), 0.70, PSB, state=_st, note=_note)

# ---------------------------------------------------------------- AFTER 12TH: MEDICAL AND ALLIED
X("neet-ug", "NEET UG", "National Testing Agency (NTA)", "12th", "Medical", "national", PCB12 + ", age 17 by 31 December of the admission year",
  D("May 2027", "Not announced as of 20 October 2026; expected first Sunday of May (2 May 2027)", "expected", "2027-05-02", "neet27",
    "4 May 2025 and 3 May 2026; the 2026 paper was cancelled and re-held on 21 June 2026. A move to computer-based mode in 2027 has been reported but not confirmed"),
  "Pen and paper (OMR) in 2026", L13,
  P("Physics:45:180, Chemistry:45:180, Biology:90:360", "+4 / -1", 180, "neet27", "Total marks, marking scheme and duration read this session; section split from the 2026 bulletin as remembered", True),
  C(2279743, 1999895, 2026, "neet26", "11,21,185 qualified"),
  SE("About 1,18,190 MBBS seats (secondary source), plus BDS, AYUSH, veterinary and B.Sc Nursing", "neetseats", 2026, True, 118190),
  "o_neet", (True, "NTA publishes question papers and answer keys"), 0.30, {"physics": "M", "chemistry": "M", "biology": "M"})

X("aiims-bsc-nursing", "AIIMS B.Sc (Hons) Nursing", "AIIMS, New Delhi", "12th", "Nursing and Paramedical", "national", PCB12 + " with English, 55%",
  D("June 2027", "Not announced; expected June 2027", "expected", "2027-06-15", "o_aiims", "Earlier cycles"),
  "Computer-based test, two stages", "English and Hindi", P("Physics:30:30, Chemistry:30:30, Biology:30:30, General Knowledge:10:10", "-1/3", 120, "o_aiims"),
  EST(0.5, 2025, "o_aiims", "Not published; estimate"), SE("B.Sc Nursing seats across AIIMS institutes", "o_aiims"),
  "o_aiims", (False, "Not published"), 0.60, {"physics": "M", "chemistry": "M", "biology": "M", "gk": "*"})

X("state-nursing", "State B.Sc Nursing CETs (Maharashtra, Karnataka, Uttar Pradesh, West Bengal and others)", "State CET cells and health universities", "12th", "Nursing and Paramedical", "state", PCB12,
  D("May to July 2027", "State-wise; not announced", "expected", "2027-06-01", "o_mh", "Earlier cycles"),
  "Varies by state", "English and state language", P("Physics, Chemistry, Biology, English, Nursing Aptitude::", "Varies", None, "o_mh", "Pattern varies by state; not researched"),
  EST(2.0, 2025, "o_mh", "Combined rough estimate across states; not researched"), SE("State B.Sc Nursing seats", "o_mh"),
  "o_mh", ("partial", "Varies by state"), 0.75, {"physics": "M", "chemistry": "M", "biology": "M", "english": "*"})

# ---------------------------------------------------------------- AFTER 12TH: UNIVERSITY, SCIENCE
X("cuet-ug", "CUET UG", "National Testing Agency (NTA)", "12th", "University (all streams)", "national", ANY12,
  D("May and June 2027", "Not announced; bulletin expected January 2027, exam expected May to June 2027", "expected", "2027-05-15", "cuet26",
    "2026: bulletin 3 January, exam 11-31 May with papers on 6-7 June"),
  "Computer-based test", L13,
  P("Each chosen subject (up to 5 of 37: 13 languages, 23 domain subjects, 1 General Aptitude Test):50:250", "+5 / -1", 60, "o_cuet", "60 minutes per subject; all 50 questions compulsory"),
  C(1568867, 1164098, 2026, "cuet26", "NTA press release of 23 June 2026"),
  SE("244 participating universities in 2026", "cuet26", 2026, True, 244),
  "o_cuet", (True, "NTA publishes papers and answer keys"), 0.50,
  {"physics": "C", "chemistry": "C", "maths": "C", "biology": "C", "commerce": "C", "humanities": "C", "quant": "*", "reasoning": "*", "english": "*", "gk": "*"})

X("iiser-iat", "IISER Aptitude Test (IAT)", "IISERs", "12th", "Science", "national", "Class 12 science, 60%",
  D("May or June 2027", "Not announced; expected late May or June 2027", "expected", "2027-05-30", "o_iat", "Earlier cycles"),
  "Computer-based test", "English and Hindi", P("Biology:15:60, Chemistry:15:60, Mathematics:15:60, Physics:15:60", "+4 / -1", 180, "o_iat"),
  EST(0.45, 2025, "o_iat", "Not re-read; estimate"), SE("BS-MS seats at 7 IISERs, IISc and IIT Madras BS programmes", "o_iat"),
  "o_iat", (True, "Past papers on the admission site"), 0.60, {"physics": "N", "chemistry": "N", "maths": "N", "biology": "N"})

X("nest", "NEST", "NISER Bhubaneswar and UM-DAE CEBS", "12th", "Science", "national", "Class 12 science, 60%",
  D("June 2027", "Not announced; expected June 2027", "expected", "2027-06-20", "o_nest", "Earlier cycles"),
  "Computer-based test", "English", P("Biology:20:60, Chemistry:20:60, Mathematics:20:60, Physics:20:60", "Negative marking in MCQ", 210, "o_nest", "Best three of four sections count"),
  EST(0.35, 2025, "o_nest", "Not re-read; estimate"), SE("About 257 integrated M.Sc seats", "o_nest"),
  "o_nest", (True, "Past papers on nestexam.in"), 0.60, {"physics": "N", "chemistry": "N", "maths": "N", "biology": "N"})

X("isi", "ISI Admission Test (B.Stat, B.Math)", "Indian Statistical Institute", "12th", "Science", "national", "Class 12 with Mathematics and English",
  D("May 2027", "Not announced; expected second Sunday of May 2027", "expected", "2027-05-09", "o_isi", "Earlier cycles"),
  "Pen and paper", "English", P("UGA multiple choice:30:120, UGB descriptive:8:80", "UGA: +4 / -1", 240, "o_isi"),
  EST(0.15, 2025, "o_isi", "Not published; estimate"), SE("B.Stat, B.Math and other ISI programmes", "o_isi"),
  "o_isi", (True, "Past papers on the ISI site"), 0.70, {"maths": "A"})

X("cmi", "CMI Entrance", "Chennai Mathematical Institute", "12th", "Science", "national", ANY12,
  D("May 2027", "Not announced; expected May 2027", "expected", "2027-05-15", "o_cmi", "Earlier cycles"),
  "Pen and paper", "English", P("Part A short answer::, Part B proofs::", "None", 180, "o_cmi"),
  EST(0.05, 2025, "o_cmi", "Not published; estimate"), SE("B.Sc programmes at CMI", "o_cmi"),
  "o_cmi", (True, "Past papers on the CMI site"), 0.70, {"maths": "A"})

X("icar-ug", "ICAR UG admission (through CUET UG)", "NTA for ICAR", "12th", "Agriculture", "national", "Class 12 with PCB, PCM or agriculture",
  D("May and June 2027", "With CUET UG 2027 (expected May to June 2027)", "expected", "2027-05-15", "o_icar", "ICAR UG admission has used CUET UG scores since 2023"),
  "Computer-based test (CUET UG)", L13, P("CUET UG subjects (Physics, Chemistry, Biology or Mathematics or Agriculture)::", "+5 / -1", 60, "o_icar", "60 minutes per subject"),
  EST(0.9, 2025, "o_icar", "Share of CUET UG candidates opting for ICAR counselling; not re-read"),
  SE("20% all-India quota seats in agricultural universities", "o_icar"),
  "o_icar", (True, "CUET UG papers"), 0.65, {"physics": "C", "chemistry": "C", "biology": "C", "maths": "C", "own": ["Agriculture (class 12 level)"]})

X("state-agri", "State agriculture entrances (MP PAT, Rajasthan JET, UPCATET and others)", "State boards and agricultural universities", "12th", "Agriculture", "state", "Class 12 with PCB, PCM or agriculture",
  D("May to July 2027", "State-wise; not announced", "expected", "2027-06-10", "o_icar", "Earlier cycles"),
  "Varies by state", "Hindi and English", P("Physics, Chemistry, Biology or Mathematics or Agriculture::", "Varies", None, "o_icar", "Not researched"),
  EST(1.2, 2025, "o_icar", "Combined rough estimate; not researched"), SE("State agricultural university seats", "o_icar"),
  "o_icar", ("partial", "Varies"), 0.80, {"physics": "S", "chemistry": "S", "biology": "S", "own": ["Agriculture (class 12 level)"]})

# ---------------------------------------------------------------- AFTER 12TH: LAW
X("clat-ug", "CLAT UG", "Consortium of National Law Universities", "12th", "Law", "national", "Class 12 with 45% (40% SC/ST)",
  D("December 2026", "6 December 2026, 2 pm to 4 pm (this is CLAT 2027)", "announced", "2026-12-06", "clat27b", "Press release of 22 July 2026; CLAT 2028 expected December 2027"),
  "Pen and paper (OMR)", "English",
  P("English Language:24:24, Current Affairs including General Knowledge:30:30, Legal Reasoning:30:30, Logical Reasoning:24:24, Quantitative Techniques:12:12", "+1 / -0.25", 120, "o_clat", "Section sizes are approximate; 120 questions in all"),
  EST(0.75, 2025, "o_clat", "Not re-read this session; UG applications as remembered"), SE("About 3,500 UG seats in the NLUs", "o_clat"),
  "o_clat", (True, "Past papers on the Consortium site"), 0.50, {"english": "*", "gk": "*", "legal": "*", "reasoning": ["Critical Reasoning", "Analytical Reasoning"], "quant": ["Arithmetic", "Data Interpretation"]})

X("ailet", "AILET", "National Law University, Delhi", "12th", "Law", "national", "Class 12 with 45%",
  D("December 2026", "Not read this session; expected second Sunday of December 2026 (AILET 2027)", "expected", "2026-12-13", "o_ailet", "Earlier cycles"),
  "Pen and paper (OMR)", "English", P("English Language:50:50, Current Affairs and General Knowledge:30:30, Logical Reasoning:70:70", "+1 / -0.25", 120, "o_ailet"),
  EST(0.2, 2025, "o_ailet", "Not published in detail; estimate"), SE("About 120 B.A. LL.B seats at NLU Delhi", "o_ailet"),
  "o_ailet", (True, "Past papers on the NLU Delhi site"), 0.50, {"english": "*", "gk": "*", "reasoning": "*", "legal": "*"})

X("mh-cet-law", "MAH LL.B 5-year CET", "State CET Cell, Maharashtra", "12th", "Law", "state", "Class 12 with 45%",
  D("April or May 2027", "Not announced; expected April to May 2027", "expected", "2027-04-28", "o_mh", "Earlier cycles"),
  "Computer-based test", "English and Marathi", P("Legal Aptitude and Legal Reasoning:40:40, General Knowledge with Current Affairs:30:30, Logical and Analytical Reasoning:40:40, English:30:30, Basic Mathematics:10:10", "None", 120, "o_mh"),
  EST(0.35, 2025, "o_mh", "Not re-read; estimate"), SE("5-year LL.B seats in Maharashtra", "o_mh"),
  "o_mh", ("partial", "Candidate's own paper and key"), 0.65, {"english": "*", "gk": "*", "reasoning": "*", "legal": "*", "quant": ["Arithmetic"]}, state="Maharashtra")

X("slat", "SLAT", "Symbiosis International University", "12th", "Law", "private", "Class 12 with 45%",
  D("December 2026", "Not read this session; expected December 2026", "expected", "2026-12-20", "o_slat", "Earlier cycles"),
  "Computer-based test", "English", P("Logical Reasoning:12:12, Legal Reasoning:12:12, Analytical Reasoning:12:12, Reading Comprehension:12:12, General Knowledge:12:12", "None", 60, "o_slat"),
  EST(0.2, 2025, "o_slat", "Not published; estimate"), SE("Symbiosis Law Schools", "o_slat"), "o_slat", (False, "Not published"), 0.55,
  {"english": "*", "gk": "*", "reasoning": "*", "legal": "*"})

# ---------------------------------------------------------------- AFTER 12TH: DESIGN AND ARCHITECTURE
X("nid-dat", "NID DAT (B.Des)", "National Institute of Design", "12th", "Design and Architecture", "national", ANY12,
  D("December 2026", "Prelims not read this session; expected around 20 December 2026 (for 2027 admission)", "expected", "2026-12-20", "o_nid", "Prelims held 21 December 2025 for 2026 admission"),
  "Pen and paper prelims, then studio test", "English and Hindi", P("Design Aptitude Test prelims::100", "None", 180, "o_nid"),
  C(14075, 13467, 2023, "nid23", "B.Des figures for DAT 2023, the latest year in the source read"),
  SE("439 B.Des seats", "nidseats", 2026, True, 439), "o_nid", (True, "Past papers on the NID admissions site"), 0.70, {"design": ["Design Aptitude"], "gk": ["Current Affairs"], "reasoning": ["Non-Verbal Reasoning"]})

X("nift", "NIFT Entrance (B.Des, B.F.Tech)", "NTA for NIFT", "12th", "Design and Architecture", "national", ANY12 + " (PCM for B.F.Tech)",
  D("January 2027", "10 January 2027 (NTA calendar, tentative)", "announced", "2027-01-10", "ntarev", "NTA examination calendar of 16 September 2026, unchanged in the October revision"),
  "Computer-based GAT and paper-based CAT", "English and Hindi", P("General Ability Test:100:100, Creative Ability Test:3:100", "-0.25 in GAT", 300, "o_nift", "GAT 120 minutes, CAT 180 minutes"),
  C(21307, 18867, 2026, "nift26", "Unique candidates, stage 1, all programmes (figures as quoted by a coaching site from NTA's result note)"),
  SE("About 5,500 seats on 19 campuses", "o_nift"), "o_nift", (True, "NTA publishes papers and keys"), 0.70, {"design": ["Design Aptitude"], "quant": ["Arithmetic"], "english": "*", "reasoning": "*", "gk": "*"})

X("uceed", "UCEED", "IIT Bombay", "12th", "Design and Architecture", "national", ANY12 + "; 2 attempts in consecutive years",
  D("January 2027", "Not read this session; expected third Sunday of January 2027", "expected", "2027-01-17", "o_uceed", "Earlier cycles"),
  "Part A computer-based, Part B on paper", "English", P("Part A (numerical, multiple select, multiple choice):57:200, Part B (sketching and design aptitude):2:100", "Negative marking in parts of A", 180, "o_uceed"),
  EST(0.15, 2025, "o_uceed", "About 15,000 as remembered; not re-read"), SE("B.Des seats at IIT Bombay, Delhi, Guwahati, Hyderabad, Roorkee and IIITDM Jabalpur", "o_uceed"),
  "o_uceed", (True, "Past papers on the UCEED site"), 0.70, {"design": ["Design Aptitude"], "reasoning": ["Non-Verbal Reasoning", "Critical Reasoning"]})

X("nata", "NATA", "Council of Architecture", "12th", "Design and Architecture", "national", "Class 12 with PCM, or diploma with Mathematics",
  D("March to June 2027", "Not announced; several attempts expected between March and June 2027", "expected", "2027-04-10", "o_nata", "Earlier cycles"),
  "Part A drawing on paper, Part B online", "English and Hindi", P("Part A Drawing and Composition:3:80, Part B Multiple choice:50:120", "None", 180, "o_nata"),
  EST(0.3, 2025, "o_nata", "Not re-read; estimate"), SE("B.Arch seats in architecture colleges across India", "o_nata"),
  "o_nata", (False, "Sample questions only"), 0.70, {"design": "*", "maths": "J", "reasoning": ["Non-Verbal Reasoning"]})

# ---------------------------------------------------------------- AFTER 12TH: MANAGEMENT, COMMERCE, HOTEL
X("ipmat-indore", "IPMAT Indore", "IIM Indore", "12th", "Management", "national", "Class 12 with 60%, age up to 20",
  D("May 2027", "Not announced; expected May 2027", "expected", "2027-05-10", "o_ipmat", "Earlier cycles"),
  "Computer-based test", "English", P("Quantitative Ability (short answer):15:60, Quantitative Ability (MCQ):30:120, Verbal Ability:45:180", "+4 / -1 (none for short answer)", 120, "o_ipmat"),
  EST(0.3, 2025, "o_ipmat", "Not published in detail; estimate"), SE("150 seats at IIM Indore; score also used by IIM Ranchi, IIFT and others", "o_ipmat"),
  "o_ipmat", (False, "Not published"), 0.60, {"quant": "*", "english": "*", "maths": ["Matrices and Determinants", "Sets, Relations and Functions", "Permutations and Combinations", "Sequences and Series"]})

X("ipmat-rohtak", "IPM Aptitude Test, IIM Rohtak", "IIM Rohtak", "12th", "Management", "national", "Class 12 with 60%",
  D("May 2027", "Not announced; expected May 2027", "expected", "2027-05-15", "o_ipmr", "Earlier cycles"),
  "Computer-based test", "English", P("Quantitative Ability:40:160, Logical Reasoning:40:160, Verbal Ability:40:160", "+4 / -1", 120, "o_ipmr"),
  EST(0.15, 2025, "o_ipmr", "Not published; estimate"), SE("About 180 seats", "o_ipmr"), "o_ipmr", (False, "Not published"), 0.60, APT)

X("jipmat", "JIPMAT", "NTA for IIM Jammu and IIM Bodh Gaya", "12th", "Management", "national", "Class 12 with 60%",
  D("April to June 2027", "Not announced; expected between April and June 2027", "expected", "2027-05-20", "o_jipmat", "Earlier cycles"),
  "Computer-based test", "English", P("Quantitative Aptitude:33:132, Data Interpretation and Logical Reasoning:33:132, Verbal Ability and Reading Comprehension:34:136", "+4 / -1", 150, "o_jipmat"),
  EST(0.12, 2025, "o_jipmat", "Not re-read; estimate"), SE("IIM Jammu and IIM Bodh Gaya integrated programmes", "o_jipmat"), "o_jipmat", (True, "NTA publishes papers and keys"), 0.60, APT)

X("npat", "NMIMS NPAT", "NMIMS", "12th", "Management", "private", ANY12,
  D("January to May 2027", "Test window expected January to May 2027", "expected", "2027-04-01", "o_npat", "Earlier cycles"),
  "Computer-based test", "English", P("Quantitative and Numerical Ability:40:40, Reasoning and General Intelligence:40:40, Proficiency in English:40:40", "None", 100, "o_npat"),
  EST(0.5, 2025, "o_npat", "Not published; estimate"), SE("NMIMS BBA, B.Com and other programmes", "o_npat"), "o_npat", (False, "Not published"), 0.60, APT)

X("ca-foundation", "CA Foundation", "Institute of Chartered Accountants of India", "12th", "Commerce and Professional", "national", "Class 12 (can register after class 10)",
  D("January, May and September 2027", "Three sittings a year; dates per ICAI notice", "expected", "2027-05-15", "o_icai", "ICAI holds the Foundation exam three times a year since 2024"),
  "Pen and paper", "English and Hindi",
  P("Accounting::100, Business Laws::100, Quantitative Aptitude (maths, logical reasoning, statistics):100:100, Business Economics:100:100", "-0.25 in the two objective papers", 600, "o_icai", "Four papers; papers 1 and 2 of 3 hours, papers 3 and 4 of 2 hours"),
  EST(1.2, 2025, "o_icai", "About 1.2 lakh per sitting as remembered; not re-read"), SE("Entry to the CA Intermediate course; no seat limit", "o_icai"),
  "o_icai", (True, "ICAI publishes past papers and suggested answers"), 0.50,
  {"commerce": ["Accountancy", "Economics", "Business Laws (CA Foundation)"], "quant": ["Arithmetic", "Modern Maths", "Algebra (aptitude)"], "reasoning": ["Verbal Reasoning", "Analytical Reasoning"]})

X("nchm-jee", "NCHM JEE", "NTA for NCHMCT", "12th", "Hotel Management", "national", ANY12 + " with English",
  D("April or May 2027", "Not announced; expected late April or May 2027", "expected", "2027-04-25", "o_nchm", "Earlier cycles"),
  "Computer-based test", "English and Hindi", P("Numerical Ability and Analytical Aptitude:20:80, Reasoning and Logical Deduction:20:80, General Knowledge and Current Affairs:20:80, English Language:40:160, Aptitude for Service Sector:20:80", "+4 / -1", 180, "o_nchm"),
  EST(0.12, 2025, "o_nchm", "Not re-read; estimate"), SE("About 12,000 B.Sc Hospitality seats in IHMs", "o_nchm"), "o_nchm", (True, "NTA publishes papers and keys"), 0.70, {**APTG, "own": ["Aptitude for the service sector"]})

X("ncet", "NCET (4-year ITEP)", "National Testing Agency (NTA)", "12th", "Teaching", "national", ANY12,
  D("April to June 2027", "Not announced; expected between April and June 2027", "expected", "2027-05-01", "o_ncet", "Earlier cycles"),
  "Computer-based test", L13, P("Languages (2), Domain subjects (3), General Test, Teaching Aptitude:160:640", "+4 / -1", 180, "o_ncet"),
  EST(0.4, 2025, "o_ncet", "Not re-read; estimate"), SE("Integrated B.A./B.Sc/B.Com B.Ed seats in central and state universities, IITs, NITs and RIEs", "o_ncet"),
  "o_ncet", (True, "NTA publishes papers and keys"), 0.70, {"english": "*", "quant": "*", "reasoning": "*", "gk": "*", "teaching": ["Teaching and Research Aptitude"]})

# ---------------------------------------------------------------- AFTER 12TH: DEFENCE AND MARINE
X("nda", "NDA and NA Examination", "Union Public Service Commission", "12th", "Defence", "national", "Class 12 pass or appearing (PCM for Air Force and Navy); unmarried, age 16.5 to 19.5",
  D("April and September 2027", "NDA (I): 11 April 2027; NDA (II): 19 September 2027", "announced", "2027-04-11", "upsc27", "UPSC annual calendar 2027, released 20 May 2026; notification for (I) on 2 December 2026"),
  "Pen and paper (OMR), then SSB interview", "English and Hindi",
  P("Mathematics:120:300, General Ability Test (English 50, General Knowledge 100):150:600", "One third of the marks of the question", 300, "o_upsc", "Two papers of 2.5 hours each; SSB carries 900 marks"),
  EST(5.0, 2024, "o_upsc", "UPSC annual reports show roughly 5 to 6 lakh applicants per sitting; not re-read"),
  SE("About 400 vacancies per sitting", "o_upsc"), "o_upsc", (True, "UPSC publishes all past papers"), 0.50,
  {"maths": "D", "english": "*", "gk": "*", "f_science": ["Physics (class 9-10)", "Chemistry (class 9-10)", "Biology (class 9-10)"]})

X("imu-cet", "IMU CET", "Indian Maritime University", "12th", "Defence", "national", PCM12 + ", 60%",
  D("May or June 2027", "Not announced; expected May to June 2027", "expected", "2027-06-01", "o_imu", "Earlier cycles"),
  "Computer-based test", "English", P("English:25:25, General Aptitude:25:25, Physics:50:50, Mathematics:50:50, Chemistry:25:25, General Knowledge:25:25", "-0.25", 180, "o_imu"),
  EST(0.25, 2025, "o_imu", "Not published; estimate"), SE("B.Tech Marine Engineering, B.Sc Nautical Science and DNS seats", "o_imu"), "o_imu", (False, "Not published"), 0.70,
  {**PS, "english": "*", "gk": "*", "reasoning": ["Verbal Reasoning"]}, note="Merchant navy; grouped with Defence for want of a better stream")

# ---------------------------------------------------------------- AFTER 10TH (and school-stage)
X("ap-polycet", "AP POLYCET", "State Board of Technical Education and Training, Andhra Pradesh", "10th", "Polytechnic and Diploma", "state", C10 + " (SSC) with Mathematics",
  D("April 2027", "Not announced; expected late April 2027", "expected", "2027-04-25", "o_appoly", "25 April 2026"),
  "Pen and paper (OMR)", "English and Telugu", P("Mathematics:50:50, Physics:40:40, Chemistry:30:30", "None", 120, "o_appoly", "120 questions; one secondary source gives a 60/30/30 split, so confirm in the 2027 booklet"),
  C(177581, 163008, 2026, "appoly", "1,48,950 qualified"), SE("3-year diploma seats in AP polytechnics", "o_appoly"),
  "o_appoly", (True, "SBTET publishes papers and keys"), 0.90, POLY, state="Andhra Pradesh")

X("tg-polycet", "TG POLYCET", "State Board of Technical Education and Training, Telangana", "10th", "Polytechnic and Diploma", "state", C10 + " (SSC)",
  D("May 2027", "Not announced; expected mid May 2027", "expected", "2027-05-13", "o_tgpoly", "Earlier cycles"),
  "Pen and paper (OMR)", "English and Telugu", P("Mathematics:60:60, Physics:30:30, Chemistry:30:30, Biology:30:30", "None", 150, "o_tgpoly"),
  EST(1.1, 2025, "o_tgpoly", "About 1.06 lakh registered in 2025 as remembered; not re-read"), SE("Diploma seats in Telangana polytechnics; also agriculture and veterinary diplomas", "o_tgpoly"),
  "o_tgpoly", (True, "SBTET publishes papers and keys"), 0.90, {"f_maths": "*", "f_science": ["Physics (class 9-10)", "Chemistry (class 9-10)", "Biology (class 9-10)"]}, state="Telangana")

X("jeecup", "JEECUP (UP Polytechnic)", "Joint Entrance Examination Council, Uttar Pradesh", "10th", "Polytechnic and Diploma", "state", C10 + " for Group A; other groups need class 12, ITI or degree",
  D("May or June 2027", "Not announced; expected late May or June 2027", "expected", "2027-06-05", "o_jeecup", "June in 2025"),
  "Computer-based test", "English and Hindi", P("Mathematics:50:200, Physics:25:100, Chemistry:25:100", "+4 / -1", 150, "o_jeecup", "Group A (engineering diploma)"),
  EST(4.2, 2025, "o_jeecup", "About 4.2 lakh registered across groups in 2025 as remembered; not re-read"), SE("About 2.3 lakh diploma seats in UP government, aided and private polytechnics", "o_jeecup"),
  "o_jeecup", ("partial", "Response sheets and keys only"), 0.90, POLY, state="Uttar Pradesh")

for _id, _nm, _body, _st, _src, _mon, _tgt, _pat in [
    ("dcece", "Bihar DCECE (Polytechnic)", "Bihar Combined Entrance Competitive Examination Board", "Bihar", "o_bcece", "May or June 2027", "2027-06-01", "Physics:30:150, Chemistry:30:150, Mathematics:30:150"),
    ("delhi-cet", "Delhi CET (Polytechnic)", "Department of Training and Technical Education, Delhi", "Delhi", "o_delhicet", "June 2027", "2027-06-15", "Mathematics, Physics, Chemistry, Biology, English, General Awareness and Reasoning:150:600"),
    ("jexpo", "West Bengal JEXPO", "West Bengal State Council of Technical and Vocational Education", "West Bengal", "o_jexpo", "May 2027", "2027-05-10", "Mathematics:50:50, Physical Science:50:50"),
    ("jeep-uk", "Uttarakhand JEEP", "Uttarakhand Board of Technical Education", "Uttarakhand", "o_ubter", "May or June 2027", "2027-06-01", "Mathematics, Physics, Chemistry, English, General Knowledge::"),
    ("pece", "Jharkhand PECE", "Jharkhand Combined Entrance Competitive Examination Board", "Jharkhand", "o_jceceb", "May or June 2027", "2027-06-01", "Physics:50:50, Chemistry:50:50, Mathematics:50:50"),
    ("cg-ppt", "Chhattisgarh PPT", "Chhattisgarh Professional Examination Board", "Chhattisgarh", "o_cgpet", "May 2027", "2027-05-20", "Physics, Chemistry, Mathematics:150:150"),
    ("assam-pat", "Assam PAT", "Directorate of Technical Education, Assam", "Assam", "o_dteassam", "June 2027", "2027-06-15", "Mathematics, Science::"),
    ("hp-pat", "Himachal Pradesh PAT", "HP Takniki Shiksha Board", "Himachal Pradesh", "o_hptsb", "May 2027", "2027-05-20", "Physics:50:200, Chemistry:50:200, Mathematics:50:200"),
    ("jk-pet", "J&K Polytechnic Entrance Test", "J&K Board of Professional Entrance Examinations", "Jammu and Kashmir", "o_jkcet", "June 2027", "2027-06-15", "Physics, Chemistry, Mathematics::"),
]:
    X(_id, _nm, _body, "10th", "Polytechnic and Diploma", "state", C10,
      D(_mon, "Not announced; month from earlier cycles", "expected", _tgt, _src, "Earlier cycles; not re-read this session"),
      "See bulletin", "English and state language", P(_pat, "See bulletin", None, _src, "From earlier bulletins as remembered; confirm"),
      EST(None, 2025, _src, "Candidate count not researched this session"), SE("State polytechnic diploma seats", _src),
      _src, ("partial", "Not checked"), 0.90, POLY, state=_st)

X("poly-merit-states", "Polytechnic admission without an entrance test (Maharashtra, Tamil Nadu, Karnataka, Kerala, Gujarat, Rajasthan, Madhya Pradesh, Odisha, Haryana, Punjab)", "State directorates of technical education", "10th", "Polytechnic and Diploma", "state", C10,
  D("May to July 2027", "Admission on class 10 marks; no exam", "expected", None, "o_mh", "These states admit on merit, so no entrance content is needed"),
  "No test", "-", P("No test::", "-", None, "o_mh"), EST(None, 2025, "o_mh", "No entrance exam"), SE("Diploma seats filled on class 10 merit", "o_mh"),
  "o_mh", (False, "No exam"), 0.0, {}, note="Listed so the map does not suggest an exam exists; check each state's 2027 rules")

X("aissee", "AISSEE (Sainik Schools, class 6 and class 9 entry)", "National Testing Agency (NTA)", "10th", "School-stage", "national", "Class 5 (age 10 to 12) or class 8 (age 13 to 15)",
  D("January 2027", "31 January 2027 (NTA calendar, tentative)", "announced", "2027-01-31", "ntarev", "NTA examination calendar of 16 September 2026, unchanged in the October revision"),
  "Pen and paper (OMR)", "Class 6: English, Hindi and regional languages; class 9: English",
  P("Class 9: Mathematics:50:200, Intelligence:25:50, English:25:50, General Science:25:50, Social Science:25:50", "None", 180, "o_aissee", "Class 6 paper: 125 questions, 300 marks, 150 minutes"),
  C(None, 178022, 2026, "aissee26", "Appeared: class 6 1,34,100 and class 9 43,922 (secondary source)"),
  SE("13,932 seats (12,527 in class 6, 1,405 in class 9) in Sainik and new Sainik schools, per a secondary source", "aisseeseats", 2026, True, 13932),
  "o_aissee", (True, "NTA publishes papers and keys"), 0.70, {"f_maths": "*", "f_science": "*", "english": ["Grammar and Usage", "Vocabulary", "Reading Comprehension"], "reasoning": ["Verbal Reasoning", "Non-Verbal Reasoning"]},
  note="Entry is at class 6 and class 9, before class 10; listed here because the brief groups it with after-10th exams")

X("rms-cet", "Rashtriya Military Schools CET (class 6 and 9)", "NTA for the Rashtriya Military Schools", "10th", "School-stage", "national", "Class 5 or class 8",
  D("December 2026", "13 December 2026 (NTA calendar, tentative; for 2027-28 admission)", "announced", "2026-12-13", "ntarev", "NTA examination calendar"),
  "Pen and paper (OMR)", "English and Hindi", P("Class 9: English:50:50, Hindi:20:20, Social Science:30:30, Mathematics:50:50, Science:50:50", "None", 150, "o_rms", "As remembered; confirm"),
  EST(0.6, 2025, "o_rms", "Not published; estimate"), SE("5 Rashtriya Military Schools, a few hundred seats", "o_rms"), "o_rms", (False, "Not published"), 0.70,
  {"f_maths": "*", "f_science": "*", "english": ["Grammar and Usage", "Vocabulary"], "reasoning": ["Verbal Reasoning"]})

X("rimc", "RIMC Entrance (class 8 entry)", "Rashtriya Indian Military College, Dehradun", "10th", "School-stage", "national", "Class 7, age 11.5 to 13",
  D("December 2026 and June 2027", "6 December 2026 (NTA calendar, tentative); next sitting expected June 2027", "announced", "2027-06-05", "ntarev", "Held twice a year"),
  "Pen and paper, then viva", "English and Hindi", P("English::125, Mathematics::200, General Knowledge::75", "None", 270, "o_rimc"),
  EST(0.1, 2025, "o_rimc", "Not published; estimate"), SE("About 25 cadets per term", "o_rimc"), "o_rimc", (False, "Sample papers sold by the college"), 0.60,
  {"f_maths": "*", "english": ["Grammar and Usage", "Vocabulary"], "gk": "*"})

X("jnvst-11", "JNV lateral entry test (class 9 and class 11)", "Navodaya Vidyalaya Samiti", "10th", "School-stage", "national", "Class 8 or class 10 in the same district",
  D("February 2027", "Not read this session; expected February 2027", "expected", "2027-02-07", "o_nvs", "Earlier cycles"),
  "Pen and paper (OMR)", "English and Hindi", P("Mental Ability:20:20, English:20:20, Science:20:20, Social Science:20:20, Mathematics:20:20", "None", 150, "o_nvs", "Class 11 lateral entry pattern as remembered"),
  EST(1.0, 2025, "o_nvs", "Not published for lateral entry; estimate"), SE("Vacant seats in Jawahar Navodaya Vidyalayas", "o_nvs"), "o_nvs", (False, "Model papers only"), 0.80,
  {"f_maths": "*", "f_science": "*", "english": ["Grammar and Usage", "Reading Comprehension"], "reasoning": ["Verbal Reasoning", "Non-Verbal Reasoning"]})

X("ntse", "NTSE (National Talent Search, class 10)", "NCERT", "10th", "School-stage", "national", "Class 10",
  D("Suspended", "The scheme has been on hold since 2021; no 2027 exam announced", "expected", None, "o_ncert", "NCERT notice of 2022 put the scheme on hold"),
  "Pen and paper (OMR) when held", "English, Hindi and regional languages", P("Mental Ability Test:100:100, Scholastic Aptitude Test:100:100", "None", 240, "o_ncert"),
  EST(None, 2021, "o_ncert", "Not running"), SE("2,000 scholarships when it ran", "o_ncert"), "o_ncert", (True, "Old papers exist"), 0.0,
  {"f_maths": "*", "f_science": "*", "reasoning": ["Verbal Reasoning", "Non-Verbal Reasoning"]}, note="Keep on the list; restart it if NCERT revives the scheme")

X("state-talent", "State talent and scholarship tests (NMMS for class 8, Rajasthan STSE, Tamil Nadu talent tests, Maharashtra scholarship exams and similar)", "State education departments and SCERTs", "10th", "School-stage", "state", "Class 8 to class 10, by scheme",
  D("November 2026 to February 2027", "State-wise; most are held between November and February", "expected", "2027-01-15", "o_scholar", "Earlier cycles; each state sets its own date"),
  "Pen and paper (OMR)", "State language and English", P("Mental Ability Test:90:90, Scholastic Aptitude Test:90:90", "None", 180, "o_scholar", "NMMS pattern; others differ"),
  EST(20.0, 2024, "o_scholar", "NMMS alone draws roughly 15 to 20 lakh class 8 students across states; rough figure, not re-read"),
  SE("1 lakh NMMS scholarships a year, plus state awards", "o_scholar"), "o_scholar", ("partial", "State SCERTs publish some papers"), 0.80,
  {"f_maths": "*", "f_science": "*", "reasoning": ["Verbal Reasoning", "Non-Verbal Reasoning"]},
  note="A family of exams, not one exam; needs its own state-by-state pass before any content is planned")

X("olympiads", "Science and Mathematics Olympiads (IOQM, NSE stage)", "HBCSE with MTA(I) and IAPT", "10th", "School-stage", "national", "Class 8 to 12 by subject",
  D("September to November 2027", "IOQM expected September 2027; NSEs expected November 2027", "expected", "2027-09-05", "o_hbcse", "Earlier cycles"),
  "Pen and paper", "English and Hindi", P("IOQM:30:100", "None", 180, "o_hbcse"),
  EST(2.0, 2025, "o_hbcse", "Rough combined figure; not re-read"), SE("Training camps and the international teams; no seats", "o_hbcse"), "o_hbcse", (True, "HBCSE and the teacher associations publish past papers"), 0.60,
  {"maths": "A", "f_maths": "*"})

# ---------------------------------------------------------------- AFTER UG: ENGINEERING AND SCIENCE
_GATE_NOTE = "Paper-wise 2026: CS 2,59,922; EC 1,15,448; CE 97,486; DA 91,764; EE 81,947; ME 76,823; XL 50,732; CY 30,775; BT 26,808; PH 24,225"
X("gate", "GATE", "IIT Madras for IISc and the IITs (2027)", "UG", "Engineering", "national", "Third year or higher of a bachelor's degree in engineering, science, commerce or arts; no age limit",
  D("February 2027", "6, 7, 13, 14, 20 and 21 February 2027; result 19 March 2027", "announced", "2027-02-06", "gate27", "Official important-dates page"),
  "Computer-based test", "English",
  P("General Aptitude:10:15, Subject paper (with Engineering Mathematics):55:85", "MCQ: -1/3 for 1-mark, -2/3 for 2-mark; none for MSQ and numerical", 180, "gate27", "65 questions, 100 marks; 30 papers plus a new Robotics and Automation paper reported for 2027"),
  C(1011719, 797434, 2026, "gate26", "Sum over papers from IIT Guwahati's statistical report; 1,56,318 qualified. " + _GATE_NOTE),
  SE("M.Tech and PhD admission at IITs, NITs and IISc with scholarship, and PSU recruitment", "gate27"),
  "gate27", (True, "All past papers and keys on the GATE sites"), 0.50,
  {"btech": "gate:ALL", "quant": "*", "reasoning": ["Verbal Reasoning", "Analytical Reasoning", "Non-Verbal Reasoning"], "english": "*"})

X("iit-jam", "IIT JAM", "IITs (organising IIT for 2027 not read this session)", "UG", "Science", "national", "Bachelor's degree with the relevant subjects",
  D("February 2027", "Not read this session; expected mid February 2027", "expected", "2027-02-14", "o_jam", "15 February 2026"),
  "Computer-based test", "English", P("Section A (MCQ):30:50, Section B (MSQ):10:20, Section C (numerical):20:30", "Section A only: -1/3 and -2/3", 180, "o_jam", "7 papers: Biotechnology, Chemistry, Economics, Geology, Mathematics, Mathematical Statistics, Physics"),
  EST(0.65, 2025, "o_jam", "About 65,000 as remembered; not re-read"), SE("About 3,000 M.Sc and joint M.Sc-PhD seats at IITs, plus NITs and IISERs through CCMN", "o_jam"),
  "o_jam", (True, "Past papers on the JAM site"), 0.70,
  {"btech": ["m-calculus", "m-linalg", "m-de", "sc-real", "sc-algebra", "m-prob", "sc-mech", "sc-em", "sc-quantum", "sc-thermal", "sc-optics", "sc-modern", "sc-mathphys", "nm-solid", "sc-organic", "sc-analytical", "bt-biochem", "bt-mol", "bt-cell", "bt-micro", "b-micro", "b-macro"]})

X("cuet-pg", "CUET PG", "National Testing Agency (NTA)", "UG", "University (all streams)", "national", GRAD,
  D("March 2027", "2-5, 8-9, 12, 15-19, 24-25 and 29-31 March 2027 (NTA revised calendar, tentative)", "announced", "2027-03-15", "ntarev", "Revised NTA calendar reported 26 October 2026"),
  "Computer-based test", "English and Hindi (language papers in the language)", P("One paper per subject code:75:300", "+4 / -1", 90, "o_cuetpg", "157 subjects and 90-minute shifts in 2026 (read this session); 75 questions and marking from the bulletin as remembered"),
  C(411366, 345220, 2026, "cuetpg26", "Unique candidates"), SE("198 universities accepted the 2026 score (secondary source)", "cuetpg26", 2026, False),
  "o_cuetpg", (True, "NTA publishes papers and keys"), 0.80,
  {"btech": ["m-calculus", "m-linalg", "m-prob", "sc-real", "sc-algebra", "sc-mech", "sc-em", "sc-quantum", "sc-thermal", "sc-organic", "bt-biochem", "bt-mol", "bt-cell", "bt-micro", "b-finacc", "b-corpacc", "b-cost", "b-tax", "b-audit", "b-pom", "b-mkt", "b-hrm", "b-fm", "b-micro", "b-macro", "b-stats", "c-ds", "c-os", "c-dbms", "c-cn", "c-fund"],
   "quant": "*", "reasoning": "*", "english": "*", "gk": "*", "own": ["Humanities and social science PG papers", "Language PG papers", "Education (B.Ed, M.Ed) papers", "Law, library science and other papers"]})

X("csir-net", "Joint CSIR-UGC NET", "NTA for CSIR", "UG", "Research and Lectureship", "national", "M.Sc or equivalent, or 4-year bachelor's degree, 55%",
  D("December 2026 and mid 2027", "19, 22 and 27 December 2026 (revised NTA calendar); June cycle expected mid 2027", "announced", "2027-07-01", "ntarev", "Two cycles a year"),
  "Computer-based test", "English and Hindi", P("Part A General Aptitude:20:30, Part B subject:40:70, Part C subject:60:100", "Varies by subject", 180, "o_csir", "Five subjects: Chemical, Earth, Life, Mathematical and Physical Sciences; question counts differ by subject"),
  EST(2.4, 2025, "o_csir", "About 2.4 lakh per cycle as remembered; not re-read"), SE("JRF fellowships and eligibility for assistant professor and PhD", "o_csir"),
  "o_csir", (True, "NTA publishes papers and keys"), 0.70,
  {"btech": ["sc-real", "sc-algebra", "m-complex", "m-de", "m-linalg", "m-prob", "sc-mech", "sc-em", "sc-quantum", "sc-thermal", "sc-modern", "sc-mathphys", "nm-solid", "sc-organic", "sc-analytical", "bt-biochem", "bt-mol", "bt-cell", "bt-gen", "bt-immuno", "bt-dev", "bt-micro"], "quant": ["Arithmetic", "Data Interpretation"], "reasoning": ["Verbal Reasoning"]})

for _id, _nm, _body, _src, _mon, _tgt, _est, _prof in [
    ("jest", "JEST", "Science and Engineering Research Board institutes", "o_jest", "February or March 2027", "2027-03-01", 0.1, ["sc-mech", "sc-em", "sc-quantum", "sc-thermal", "sc-mathphys", "sc-modern", "nm-solid"]),
    ("tifr-gs", "TIFR GS", "Tata Institute of Fundamental Research", "o_tifr", "December 2026", "2026-12-13", 0.15, ["sc-mech", "sc-em", "sc-quantum", "sc-thermal", "sc-real", "sc-algebra", "bt-biochem", "bt-mol"]),
    ("gat-b", "GAT-B", "NTA for the Department of Biotechnology", "o_gatb", "April 2027", "2027-04-20", 0.1, ["bt-biochem", "bt-mol", "bt-cell", "bt-micro", "bt-gen", "bt-immuno", "bt-gene", "bt-bioproc"]),
    ("pgecet", "State PG engineering CETs (AP PGECET, TG PGECET, Karnataka PGCET, TANCET/CEETA)", "State councils and universities", "o_pgecet", "March to July 2027", "2027-06-01", 1.0, ["m-linalg", "m-calculus", "m-de", "m-prob", "c-ds", "c-algo", "c-os", "c-dbms", "c-cn", "ec-circuits", "ec-signals", "ec-analog", "ee-machines", "ee-psys", "me-thermo", "me-som", "me-fluid", "ce-struct", "ce-geo"]),
]:
    X(_id, _nm, _body, "UG", "Science" if _id in ("jest", "tifr-gs", "gat-b") else "Engineering", "national" if _id != "pgecet" else "state", "Bachelor's or master's degree in the subject",
      D(_mon, "Not read this session; month from earlier cycles", "expected", _tgt, _src, "Earlier cycles"),
      "Computer-based test", "English", P("Subject paper::", "See bulletin", 180, _src, "Not researched this session"),
      EST(_est, 2025, _src, "Estimate; not researched"), SE("PG and PhD seats at the member institutes", _src), _src, ("partial", "Past papers on some sites"), 0.70, {"btech": _prof})

# ---------------------------------------------------------------- AFTER UG: MANAGEMENT AND COMPUTER APPLICATIONS
X("cat", "CAT", "IIM Indore (CAT 2026)", "UG", "Management", "national", "Bachelor's degree with 50% (45% SC/ST/PwD)",
  D("November 2026", "29 November 2026, three sessions (for 2027 admission); CAT 2027 expected late November 2027", "announced", "2026-11-29", "cat26d", "Notification of 26 July 2026"),
  "Computer-based test", "English", P("Verbal Ability and Reading Comprehension:24:72, Data Interpretation and Logical Reasoning:22:66, Quantitative Ability:22:66", "+3 / -1 (none for type-in answers)", 120, "o_cat", "68 questions and 204 marks in 2025; 40 minutes per section"),
  C(284000, None, 2026, "cat26", "2.84 lakh registrations reported from IIM Indore's release; 2.95 lakh in 2025"),
  SE("21 IIMs and over 1,000 other institutes accept the score", "o_cat"), "o_cat", (True, "IIMs release each year's paper and key"), 0.30, APT)

for _id, _nm, _body, _src, _mon, _dt, _stat, _dsrc, _tgt, _pat, _dur, _est, _prof, _u in [
    ("xat", "XAT", "XLRI Jamshedpur", "o_xat", "January 2027", "Not read this session; expected first Sunday of January 2027", "expected", "o_xat", "2027-01-03", "Verbal and Logical Ability:26:26, Decision Making:21:21, Quantitative Ability and Data Interpretation:28:28, General Knowledge:20:20", 180, 1.3, {**APTG, "own": ["Decision making caselets"]}, 0.35),
    ("cmat", "CMAT", "National Testing Agency (NTA)", "o_cmat", "February 2027", "7 February 2027 (NTA calendar, tentative)", "announced", "ntarev", "2027-02-07", "Quantitative Techniques and Data Interpretation:20:80, Logical Reasoning:20:80, Language Comprehension:20:80, General Awareness:20:80, Innovation and Entrepreneurship:20:80", 180, 0.75, {**APTG, "own": ["Innovation and entrepreneurship"]}, 0.45),
    ("snap", "SNAP", "Symbiosis International University", "o_snap", "December 2026", "Not read this session; three tests expected in December 2026", "expected", "o_snap", "2026-12-20", "General English:15:15, Analytical and Logical Reasoning:25:25, Quantitative, Data Interpretation and Data Sufficiency:20:20", 60, 1.2, APT, 0.40),
    ("nmat", "NMAT by GMAC", "Graduate Management Admission Council", "o_nmat", "November and December 2026", "Test window expected to run into December 2026", "expected", "o_nmat", "2026-12-15", "Language Skills:36:, Quantitative Skills:36:, Logical Reasoning:36:", 120, 0.7, APT, 0.40),
    ("mat", "MAT", "All India Management Association", "o_mat", "February, May, September and December 2027", "Several sittings a year", "expected", "o_mat", "2027-02-20", "Language Comprehension:30:, Intelligence and Critical Reasoning:30:, Data Analysis and Sufficiency:30:, Mathematical Skills:30:, Economic and Business Environment:30:", 120, 0.6, APTG, 0.45),
    ("mah-mba-cet", "MAH MBA/MMS CET", "State CET Cell, Maharashtra", "o_mh", "April 2027", "Not announced; expected April 2027 with a second attempt in May", "expected", "o_mh", "2027-04-03", "Logical Reasoning:75:75, Abstract Reasoning:25:25, Quantitative Aptitude:50:50, Verbal Ability and Reading Comprehension:50:50", 150, None, APT, 0.50),
    ("tancet", "TANCET (MBA, MCA)", "Anna University", "o_tancet", "March 2027", "Not announced; expected March 2027", "expected", "o_tancet", "2027-03-20", "Quantitative Aptitude, Analytical Reasoning, Logical Reasoning, Computer Awareness, English:100:100", 120, 0.4, {**APT, "computer": "*"}, 0.65),
    ("ap-icet", "AP ICET", "APSCHE", "o_apicet", "May 2027", "Not announced; expected May 2027", "expected", "o_apicet", "2027-05-08", "Analytical Ability:75:75, Mathematical Ability:75:75, Communication Ability:50:50", 150, 0.45, APT, 0.70),
    ("tg-icet", "TG ICET", "TGCHE", "o_tgicet", "June 2027", "Not announced; expected June 2027", "expected", "o_tgicet", "2027-06-08", "Analytical Ability:75:75, Mathematical Ability:75:75, Communication Ability:50:50", 150, 0.8, APT, 0.70),
]:
    _c = C(186769, 157637, 2026, "mhall", "Registrations across both attempts") if _id == "mah-mba-cet" else EST(_est, 2025, _src, "As remembered or estimated; not re-read")
    X(_id, _nm, _body, "UG", "Management", "state" if _id in ("mah-mba-cet", "tancet", "ap-icet", "tg-icet") else ("national" if _id in ("cmat", "mat") else "private"), GRAD + ", 50%",
      D(_mon, _dt, _stat, _tgt, _dsrc, "Earlier cycles" if _stat == "expected" else "NTA examination calendar"),
      "Computer-based test", "English", P(_pat, "See bulletin (CMAT: +4 / -1)", _dur, _src), _c,
      SE("MBA and PGDM seats at accepting institutes", _src), _src, (True if _id == "cmat" else False, "NTA publishes CMAT papers; most others do not release papers"), _u, _prof)

X("nimcet", "NIMCET", "NITs (by rotation)", "UG", "Computer Applications", "national", "Bachelor's degree with Mathematics or Statistics, 60%",
  D("June 2027", "Not announced; expected June 2027", "expected", "2027-06-08", "o_nimcet", "Earlier cycles"),
  "Computer-based test", "English", P("Mathematics:50:600, Analytical Ability and Logical Reasoning:40:240, Computer Awareness:20:120, General English:10:40", "Negative marking applies", 120, "o_nimcet", "1,000 marks"),
  EST(0.35, 2025, "o_nimcet", "Not re-read; estimate"), SE("About 1,000 MCA seats in NITs and IIITs", "o_nimcet"), "o_nimcet", ("partial", "Keys released; papers not archived"), 0.65,
  {"maths": "J", "reasoning": "*", "computer": "*", "english": "*"})

# ---------------------------------------------------------------- AFTER UG: MEDICAL, PHARMACY, LAW, DESIGN, TEACHING
for _id, _nm, _body, _stream, _src, _mon, _dt, _tgt, _pat, _neg, _dur, _est, _own, _u, _elig in [
    ("neet-pg", "NEET PG", "National Board of Examinations in Medical Sciences", "Medical", "o_nbe", "Mid 2027", "Not announced; expected between June and August 2027", "2027-07-15", "Pre-clinical, para-clinical and clinical subjects:200:800", "+4 / -1", 210, 2.4,
     ["Pre-clinical subjects (anatomy, physiology, biochemistry)", "Para-clinical subjects (pathology, pharmacology, microbiology, forensic medicine, community medicine)", "Clinical subjects (medicine, surgery, obstetrics and gynaecology, paediatrics and allied)"], 0.30, "MBBS with internship"),
    ("ini-cet", "INI CET", "AIIMS, New Delhi", "Medical", "o_aiims", "May and November 2027", "Two sessions a year; dates not announced", "2027-05-15", "MBBS subjects:200:200", "+1 / -1/3", 180, 0.8,
     ["Pre-clinical subjects (anatomy, physiology, biochemistry)", "Para-clinical subjects (pathology, pharmacology, microbiology, forensic medicine, community medicine)", "Clinical subjects (medicine, surgery, obstetrics and gynaecology, paediatrics and allied)"], 0.30, "MBBS with internship"),
    ("neet-mds", "NEET MDS", "National Board of Examinations in Medical Sciences", "Medical", "o_nbe", "February to April 2027", "Not announced", "2027-03-15", "BDS subjects:240:960", "+4 / -1", 180, 0.25, ["BDS subjects"], 0.40, "BDS with internship"),
    ("fmge", "FMGE", "National Board of Examinations in Medical Sciences", "Medical", "o_nbe", "June and December 2027", "Two sessions a year; dates not announced", "2027-06-20", "MBBS subjects:300:300", "None", 300, 0.9,
     ["Pre-clinical subjects (anatomy, physiology, biochemistry)", "Para-clinical subjects (pathology, pharmacology, microbiology, forensic medicine, community medicine)", "Clinical subjects (medicine, surgery, obstetrics and gynaecology, paediatrics and allied)"], 0.40, "Foreign medical degree (licensing test)"),
    ("gpat", "GPAT", "National Board of Examinations in Medical Sciences", "Pharmacy", "o_nbe", "May or June 2027", "Not announced", "2027-06-01", "Pharmaceutics, Pharmaceutical Chemistry, Pharmacology, Pharmacognosy and others:125:500", "+4 / -1", 180, 0.5, ["B.Pharm subjects"], 0.60, "B.Pharm"),
    ("clat-pg", "CLAT PG", "Consortium of National Law Universities", "Law", "o_clat", "December 2026", "6 December 2026 (announced, with CLAT UG)", "2026-12-06", "Constitutional law, jurisprudence and other law subjects:120:120", "+1 / -0.25", 120, 0.15, ["LL.B subjects"], 0.55, "LL.B with 50%"),
    ("aibe", "All India Bar Examination", "Bar Council of India", "Law", "o_bci", "Usually once a year", "Not announced", "2027-06-01", "LL.B subjects:100:100", "None", 180, 2.0, ["LL.B subjects"], 0.55, "LL.B (licensing test)"),
    ("ceed", "CEED", "IIT Bombay", "Design and Architecture", "o_ceed", "January 2027", "Not read this session; expected third Sunday of January 2027", "2027-01-17", "Part A (computer-based)::150, Part B (drawing and design)::100", "Negative marking in parts of A", 180, 0.06, [], 0.70, GRAD),
    ("icar-pg", "ICAR AIEEA PG and AICE JRF/SRF", "NTA for ICAR", "Agriculture", "o_icar", "June or July 2027", "Not announced", "2027-06-25", "Subject paper:120:480", "+4 / -1", 120, 0.4, ["Agriculture and allied degree subjects"], 0.75, "Bachelor's degree in agriculture or allied science"),
]:
    _p = {"own": _own} if _own else {"design": ["Design Aptitude"], "reasoning": ["Non-Verbal Reasoning"]}
    X(_id, _nm, _body, "UG", _stream, "national", _elig,
      D(_mon, _dt, "announced" if _id == "clat-pg" else "expected", _tgt, "clat27b" if _id == "clat-pg" else _src, "Earlier cycles" if _id != "clat-pg" else "Press release of 22 July 2026"),
      "Computer-based test" if _id not in ("clat-pg", "aibe") else "Pen and paper", "English", P(_pat, _neg, _dur, _src), EST(_est, 2025, _src, "As remembered or estimated; not re-read"),
      SE("PG seats or licence, per the bulletin", _src), _src, ("partial", "Varies; NBEMS does not release papers, the Consortium and IIT Bombay do"), _u, _p)

X("ugc-net", "UGC NET", "National Testing Agency (NTA)", "UG", "Research and Lectureship", "national", "Master's degree with 55%, or 4-year bachelor's degree with 75%",
  D("December 2026 and June 2027", "14-18 and 21 December 2026 (revised NTA calendar); June 2027 cycle expected", "announced", "2027-06-25", "ntarev", "Two cycles a year"),
  "Computer-based test", "English and Hindi (language subjects in the language)", P("Paper 1 Teaching and Research Aptitude:50:100, Paper 2 subject (85 subjects):100:200", "None", 180, "o_ugcnet"),
  C(550048, None, 2026, "ntarev", "December 2026 cycle, registrations as on 25 October 2026 with the window still open; 3,73,419 had paid"),
  SE("JRF, eligibility for assistant professor and PhD admission", "o_ugcnet"), "o_ugcnet", (True, "NTA publishes papers and keys"), 0.50,
  {"teaching": "*", "btech": ["b-finacc", "b-corpacc", "b-cost", "b-tax", "b-audit", "b-pom", "b-mkt", "b-hrm", "b-fm", "b-micro", "b-macro", "b-stats", "b-law", "b-bank", "b-invest", "b-strat", "b-research", "c-ds", "c-os", "c-dbms", "c-cn", "c-toc", "c-compiler", "c-se", "c-ai"],
   "own": ["Paper 2 in 85 subjects (commerce, management and computer science map to the B.Tech/B.Com pack; the rest do not)"]})

X("bed-entrance", "State B.Ed entrance tests (UP B.Ed JEE, Bihar B.Ed CET, Rajasthan PTET, MAH B.Ed CET and others)", "State universities", "UG", "Teaching", "state", GRAD + ", 50%",
  D("April to July 2027", "State-wise; not announced", "expected", "2027-06-01", "o_upbed", "Earlier cycles"),
  "Pen and paper in most states", "Hindi and English", P("General Knowledge, Language, General Aptitude, Subject Ability:200:400", "Varies (UP: -1/3)", 360, "o_upbed", "UP B.Ed JEE pattern, two papers of 3 hours"),
  EST(8.0, 2025, "o_upbed", "Combined rough figure for the large states; not researched"), SE("B.Ed seats in state colleges", "o_upbed"), "o_upbed", ("partial", "Varies"), 0.60,
  {"gk": "*", "english": "*", "reasoning": "*", "quant": ["Arithmetic"], "teaching": ["Teaching and Research Aptitude"]})

X("ctet", "CTET (and state TETs)", "Central Board of Secondary Education", "UG", "Government jobs", "national", "D.El.Ed or B.Ed (qualifying test for school teachers)",
  D("Two sittings in 2027", "Not announced", "expected", "2027-07-05", "o_ctet", "Earlier cycles"),
  "Pen and paper (OMR)", "20 languages", P("Child Development and Pedagogy:30:30, Language I:30:30, Language II:30:30, Mathematics and Science or Social Studies:60:60", "None", 150, "o_ctet", "Paper 2; Paper 1 has five sections of 30"),
  EST(20.0, 2024, "o_ctet", "Roughly 20 lakh or more per sitting as remembered; not re-read"), SE("Eligibility certificate; no seats", "o_ctet"), "o_ctet", (True, "CBSE publishes papers and keys"), 0.40,
  {"f_maths": "*", "f_science": "*", "english": ["Grammar and Usage", "Reading Comprehension"], "own": ["Child development and pedagogy"]},
  group="optional_govt_jobs", note="A qualifying test for school-teacher jobs, so it sits in the optional government-jobs group")

# ---------------------------------------------------------------- OPTIONAL: GOVERNMENT JOB EXAMS
for _id, _nm, _body, _lvl, _src, _mon, _dt, _stat, _dsrc, _tgt, _est, _prof in [
    ("upsc-cse", "UPSC Civil Services (Prelims)", "Union Public Service Commission", "UG", "o_upsc", "May 2027", "23 May 2027; Mains from 20 August 2027", "announced", "upsc27", "2027-05-23", 11.0, {"gk": "*", "quant": ["Arithmetic", "Data Interpretation"], "reasoning": "*", "english": ["Reading Comprehension"]}),
    ("upsc-cds", "UPSC CDS", "Union Public Service Commission", "UG", "o_upsc", "April and September 2027", "CDS (I): 11 April 2027; CDS (II): 19 September 2027", "announced", "upsc27", "2027-04-11", 5.0, {"gk": "*", "english": "*", "f_maths": "*"}),
    ("upsc-ese", "UPSC Engineering Services (Prelims)", "Union Public Service Commission", "UG", "o_upsc", "January 2027", "31 January 2027", "announced", "upsc27", "2027-01-31", 1.5, {"btech": "gate:ESE", "gk": ["Current Affairs"], "quant": ["Arithmetic"]}),
    ("ssc-cgl", "SSC CGL", "Staff Selection Commission", "UG", "o_ssc", "Mid 2027", "Per the SSC calendar; not read this session", "expected", "o_ssc", "2027-08-15", 28.0, APTG),
    ("ssc-chsl", "SSC CHSL", "Staff Selection Commission", "12th", "o_ssc", "Mid 2027", "Per the SSC calendar; not read this session", "expected", "o_ssc", "2027-08-01", 30.0, APTG),
    ("ssc-mts-gd", "SSC MTS and SSC GD Constable", "Staff Selection Commission", "10th", "o_ssc", "Through 2027", "Per the SSC calendar; not read this session", "expected", "o_ssc", "2027-09-01", 50.0, APTG),
    ("ibps-po-clerk", "IBPS PO, Clerk and RRB", "Institute of Banking Personnel Selection", "UG", "o_ibps", "August to December 2027", "Per the IBPS calendar; not read this session", "expected", "o_ibps", "2027-10-01", 25.0, {**APTG, "computer": "*"}),
    ("sbi-po-clerk", "SBI PO and SBI Clerk", "State Bank of India", "UG", "o_sbi", "Through 2027", "Per SBI notices", "expected", "o_sbi", "2027-09-01", 20.0, {**APTG, "computer": "*"}),
    ("rbi-grade-b", "RBI Grade B", "Reserve Bank of India", "UG", "o_rbi", "Mid 2027", "Per the RBI notice", "expected", "o_rbi", "2027-07-15", 2.0, APTG),
    ("rrb-ntpc", "RRB NTPC, Group D, ALP and JE", "Railway Recruitment Boards", "12th", "o_rrb", "No fixed annual date", "Per each recruitment notice", "expected", "o_rrb", "2027-06-01", 120.0, {**APTG, "f_maths": "*", "f_science": "*"}),
    ("afcat", "AFCAT", "Indian Air Force", "UG", "o_afcat", "February and August 2027", "Two sittings a year", "expected", "o_afcat", "2027-02-20", 2.5, APTG),
    ("agniveer", "Agniveer (Army, Navy, Air Force)", "Indian Armed Forces", "10th", "o_agni", "Through 2027", "Per each service's notice", "expected", "o_agni", "2027-06-15", 15.0, {"f_maths": "*", "f_science": "*", "gk": "*", "reasoning": ["Verbal Reasoning"], "english": ["Grammar and Usage"]}),
]:
    X(_id, _nm, _body, _lvl, "Government jobs", "national", "Per the recruitment notice",
      D(_mon, _dt, _stat, _tgt, _dsrc, "UPSC annual calendar 2027" if _stat == "announced" else "Earlier cycles"),
      "Computer-based or OMR, by exam", "English and Hindi (regional languages in some)", P("See notice::", "Usually one quarter or one third per wrong answer", None, _src, "Patterns not researched; optional group"),
      EST(_est, 2025, _src, "Order-of-magnitude figure as remembered; not researched"), SE("Vacancies vary by year", _src), _src, (True if "upsc" in _id else "partial", "UPSC publishes papers; SSC, IBPS and RRB release response sheets"), 0.20, _prof, group="optional_govt_jobs")

# ---------------------------------------------------------------- OPTIONAL: STUDY ABROAD
for _id, _nm, _body, _lvl, _src, _prof in [
    ("sat", "SAT", "College Board", "12th", "o_sat", {"english": "*", "quant": ["Algebra (aptitude)", "Geometry and Mensuration (aptitude)", "Data Interpretation"]}),
    ("act", "ACT", "ACT Inc.", "12th", "o_act", {"english": "*", "quant": ["Algebra (aptitude)", "Geometry and Mensuration (aptitude)"]}),
    ("ielts", "IELTS", "British Council, IDP and Cambridge", "12th", "o_ielts", {"english": "*"}),
    ("toefl", "TOEFL iBT", "ETS", "12th", "o_toefl", {"english": "*"}),
    ("pte-det", "PTE Academic and Duolingo English Test", "Pearson; Duolingo", "12th", "o_pte", {"english": "*"}),
    ("gre", "GRE General Test", "ETS", "UG", "o_gre", {"english": "*", "quant": "*"}),
    ("gmat", "GMAT", "Graduate Management Admission Council", "UG", "o_gmat", {"english": "*", "quant": "*", "reasoning": ["Critical Reasoning"]}),
    ("lsat", "LSAT", "Law School Admission Council", "UG", "o_lsat", {"english": ["Reading Comprehension"], "reasoning": ["Critical Reasoning", "Analytical Reasoning"]}),
]:
    X(_id, _nm, _body, _lvl, "Study abroad", "international", "Open; set by the receiving university",
      D("All year", "Test dates through the year; book on the official site", "year_round", None, _src, "Offered year-round"),
      "Computer-based (IELTS also on paper)", "English", P("See official site::", "None", None, _src, "Not researched; optional group"),
      EST(None, 2025, _src, "India-specific counts are not published in a usable form; left blank"), SE("Not applicable", _src), _src, ("partial", "Official practice tests, not past papers"), 0.20, _prof, group="optional_study_abroad")
