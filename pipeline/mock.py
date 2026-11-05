"""Offline stand-in for the model, used only to test the pipeline (python3 pipeline/run_unit.py <unit> --mock)."""
import re

WORDS = ('The idea is simple once the steps are clear. Each step uses only the values from the step before it, '
         'so a student can check the work line by line. Write the rule first, then apply it to the numbers, then say what the result means. ')

def para(topic, n=60):
    base = f'{topic} follows one rule that the examiner checks every time. ' + WORDS * 6
    return ' '.join(base.split()[:n]) + '.'

FIGS = [
    {'type': 'blocks', 'direction': 'down', 'nodes': [{'id': 'a', 'label': 'Input'}, {'id': 'b', 'label': 'Process', 'style': 'accent'}, {'id': 'c', 'label': 'Output', 'style': 'next'}], 'edges': [{'from': 'a', 'to': 'b'}, {'from': 'b', 'to': 'c', 'label': 'result'}]},
    {'type': 'gantt', 'unit': 'ms', 'lanes': [{'label': 'CPU', 'bars': [{'label': 'P1', 'start': 0, 'end': 6}, {'label': 'P2', 'start': 6, 'end': 10, 'style': 'live'}]}]},
    {'type': 'stack', 'items': [{'label': 'User programs'}, {'label': 'System calls', 'style': 'accent'}, {'label': 'Kernel'}, {'label': 'Hardware', 'style': 'muted'}]},
    {'type': 'sequence', 'actors': ['Process', 'Kernel', 'Disk'], 'messages': [{'from': 'Process', 'to': 'Kernel', 'label': 'read()'}, {'from': 'Kernel', 'to': 'Disk', 'label': 'request'}, {'from': 'Disk', 'to': 'Kernel', 'label': 'interrupt', 'dashed': True}, {'from': 'Kernel', 'to': 'Process', 'label': 'data'}]},
    {'type': 'array', 'rows': [{'label': 'Frames', 'cells': ['7', '0', '1'], 'marks': {'1': 'live'}}], 'pointers': [{'row': 0, 'cell': 1, 'label': 'victim'}]},
    {'type': 'plot', 'x': {'label': 'processes', 'min': 1, 'max': 20}, 'y': {'label': 'CPU use (%)'}, 'series': [{'name': 'utilisation', 'expr': '100*(1-0.8**x)'}]},
    {'type': 'tree', 'root': {'label': 'init', 'children': [{'label': 'sh', 'children': [{'label': 'ls'}]}, {'label': 'sshd'}]}},
    {'type': 'sets', 'mode': 'venn', 'sets': [{'label': 'Process', 'items': ['own memory']}, {'label': 'Thread', 'items': ['own stack']}], 'overlap': ['code']},
    {'type': 'graph', 'directed': True, 'nodes': [{'id': 'A', 'x': 0, 'y': 0}, {'id': 'B', 'x': 2, 'y': 0}, {'id': 'C', 'x': 1, 'y': 1}], 'edges': [{'from': 'A', 'to': 'B', 'label': '3'}, {'from': 'B', 'to': 'C'}, {'from': 'C', 'to': 'A'}]},
]

C_PROG = '#include <stdio.h>\nint main(void) {\n    int s = 0;\n    for (int i = 1; i <= 4; i++) s += i * i;\n    printf("sum = %d\\n", s);\n    return 0;\n}\n'

def answer(P):
    U = P['unit']
    def fn(task, prompt):
        if task == 'plan':
            return {'lead': f'This unit covers {U["name"].lower()}. After it you can explain each idea and solve the standard exam questions.',
                    'about': para('This unit', 110),
                    'chapters': [{'k': k, 'idea': s['t'], 'figure': 'blocks', 'example': 'a small numeric question', 'trap': 'a common slip'} for k, s in enumerate(U['subtopics'], 1)],
                    'links': [[k, k + 1, 'leads to'] for k in range(1, len(U['subtopics']))]}
        m = re.match(r'(ch|revise|resize|chfix)(\d+)', task)
        if m:
            k = int(m.group(2)); t = U['subtopics'][k - 1]['t']
            ex = {'question': f'A system runs 4 jobs of 3, 5, 2 and 6 ms. Find the average time for {t.lower()}.',
                  'steps': ['Add the times: 3 + 5 + 2 + 6 = 16 ms.', 'Divide by 4 jobs: 16 ÷ 4 = 4 ms.'],
                  'answer': 'The average is 4 ms.', 'check': 'print((3+5+2+6)/4)', 'values': [4]}
            if k == 2:
                ex['code'] = {'lang': 'c', 'code': C_PROG}; ex['output'] = 'sum = 30'
                ex['dry_run'] = {'head': ['i', 's'], 'rows': [['1', '1'], ['2', '5'], ['3', '14'], ['4', '30']]}
            secs = [{'h3': f'Part {i} of {t}', 'blocks': [{'type': 'p', 'text': para(t, 120)}, {'type': 'p', 'text': para('The <b>key term</b>', 90)},
                     {'type': 'steps', 'items': [para('Step', 18), para('Next', 18)]}]} for i in range(1, 4)]
            if k == 3:
                secs[1]['blocks'].append({'type': 'code', 'lang': 'python', 'code': 'print(sum(range(5)))', 'output': '10'})
                secs[2]['blocks'].append({'type': 'table', 'head': ['Call', 'Meaning'], 'rows': [['fork()', 'make a child process'], ['exec()', 'load a new program']]})
            return {'lead': para(t, 80), 'prereq': '', 'sections': secs,
                    'figure': {'after_section': 1, 'caption': f'How {t.lower()} works.', 'spec': dict(FIGS[(k - 1) % len(FIGS)], aria=f'Diagram of {t}')},
                    'examples': [ex], 'traps': [para('Trap', 20), para('Slip', 20), para('Look-alike', 20)],
                    'quiz': [{'level': l, 'q': f'{l.capitalize()} question about {t}?', 'marks': 2 + i % 3, 'a': para('Answer', 25)} for i, l in enumerate(['remember', 'understand', 'apply', 'analyze', 'apply', 'understand'])],
                    'beyond': 'Not for the exam. ' + para('Industry', 50)}
        if task.startswith('review'):
            return {'issues': [{'severity': 'low', 'where': 'section 1', 'problem': 'wording', 'fix': 'shorter'}]}
        if task == 'unit':
            return {'key_terms': [{'term': f'Term {i}', 'meaning': 'what it means', 'chapter': 1 + i % len(U['subtopics'])} for i in range(12)],
                    'takeaways': [para('Takeaway', 14) for _ in range(7)], 'bank_note': 'Most syllabi ask for the definition with a labelled diagram.',
                    'bank': [{'group': g, 'level': g.split('-')[0], 'q': f'Long question {i} ({g})', 'marks': 13, 'outline': ['point one', 'point two'], 'chapters': [1, 2] if i < 3 else [1]}
                             for i, g in enumerate(['remember-understand'] * 4 + ['apply'] * 4 + ['analyze-evaluate'] * 4)],
                    'glossary': [{'term': f'Word {i}', 'def': 'its meaning in one line'} for i in range(18)],
                    'textbooks': [{'title': 'Operating System Concepts', 'authors': 'Silberschatz, Galvin and Gagne', 'edition': '', 'pointer': ''}],
                    'web': []}
        if task.startswith(('figfix', 'spill')):
            return {'caption': 'Redrawn.', 'spec': FIGS[0]}
        raise ValueError(task)
    return fn
