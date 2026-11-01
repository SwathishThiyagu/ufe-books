#!/usr/bin/env python3
"""Write the packet one unit-book writer needs.
usage: python3 make_packet.py <universal.json> <subject id> <unit number> <out.json>
       python3 make_packet.py <universal.json> --list [btech|other|<dept>]   (print the work list)"""
import sys, json

def main():
    U = json.load(open(sys.argv[1]))
    if sys.argv[2] == '--list':
        want = sys.argv[3] if len(sys.argv) > 3 else None
        for s in U['subjects']:
            if want and want not in (s['scope'], s['dept']) and want not in s['departments']: continue
            for un in s['units']:
                print(f"{s['id']}\t{un['n']}\t{s['dept']}\t{s['scope']}\t{s['name']} · Unit {un['n']}: {un['name']} ({len(un['subtopics'])} subtopics)")
        return
    sid, n, out = sys.argv[2], int(sys.argv[3]), sys.argv[4]
    s = next((x for x in U['subjects'] if x['id'] == sid), None)
    if not s: sys.exit(f'no subject {sid}')
    if not 1 <= n <= len(s['units']): sys.exit(f'{sid} has units 1..{len(s["units"])}')
    unit = s['units'][n - 1]
    others = [dict(n=u['n'], name=u['name'], subtopics=[x['t'] for x in u['subtopics']]) for u in s['units'] if u['n'] != n]
    subj = {k: v for k, v in s.items() if k != 'units'}
    pk = dict(universities=U['universities'], order=U['order'], departments={d: U['departments'][d] for d in s['departments'] + [s['dept']] if d in U['departments']},
              subject=subj, unit=unit, other_units=others,
              out=f"03_Books/{s['dept']}/{s['id']}/{s['id']}-u{n}.html")
    json.dump(pk, open(out, 'w'), ensure_ascii=False, indent=1)
    print(f"packet for {s['name']} · Unit {n}: {unit['name']} ({len(unit['subtopics'])} subtopics) -> {out}; book path {pk['out']}")

if __name__ == '__main__':
    main()
