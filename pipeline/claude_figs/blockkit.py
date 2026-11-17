"""Helpers for the Blockchain (c-block) hand-drawn figures, on top of kit.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *


def A(x1, y1, x2, y2, c=AC, w=2, dash=None, arrow='n'):
    """arrow"""
    return L(x1, y1, x2, y2, c, w, dash, arrow)


def node(x, y, label, r=24, fill=PANEL, stroke=AC, size=14, sub=None, subfill=MUT):
    o = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:{fill};stroke:{stroke};stroke-width:2"/>', T(x, y + size * 0.35, label, size, bold=True)]
    if sub: o.append(T(x, y + r + 17, sub, 13, fill=subfill))
    return ''.join(o)


def block(x, y, w, title, rows, fill=PANEL, stroke=AC, size=13, title_fill=None, row_fills=None, lh=19, mono=False):
    """a block drawn as a card: a title strip, then left-aligned field rows. Returns (svg, height)."""
    h = 30 + len(rows) * lh + 8
    o = [R(x, y, w, h, fill, stroke, 8), R(x, y, w, 28, title_fill or ACS, stroke, 8)]
    o.append(T(x + w / 2, y + 19, title, 14, bold=True))
    for i, r in enumerate(rows):
        f = (row_fills or {}).get(i, INK)
        o.append((TM if mono else T)(x + 10, y + 30 + (i + 1) * lh - 4, r, size, 'start', f))
    return ''.join(o), h


def cross(x, y, s=9, c=LV, w=3):
    return L(x - s, y - s, x + s, y + s, c, w) + L(x - s, y + s, x + s, y - s, c, w)


def tick(x, y, s=8, c=NX, w=3):
    return P([(x - s, y), (x - s / 3, y + s * 0.7), (x + s, y - s * 0.8)], c, w)
