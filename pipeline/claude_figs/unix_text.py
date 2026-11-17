"""Text clean-up shared by the c-unix drawing modules: the books name no universities and give no counts of them,
so 'only a few universities teach X' becomes 'only a few syllabi teach X'. Applied to every string of a chapter
except its figure; idempotent."""
import re

SUBS = [
    (re.compile(r'\b([Oo]nly a few) universities (teach)\b'), r'\1 syllabi \2'),
]


def clean(x):
    if isinstance(x, dict):
        return {k: (v if k == 'figure' else clean(v)) for k, v in x.items()}
    if isinstance(x, list):
        return [clean(v) for v in x]
    if isinstance(x, str):
        for a, b in SUBS:
            x = a.sub(b, x)
        return x
    return x
