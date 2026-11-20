"""Claude's hand-drawn figures for ec-circuits-u2 (Circuit Theory: mesh, nodal analysis and network theorems), one per
chapter, drawn from each chapter's own worked example and numbers. Colours are the shell's CSS variables only.
A small circuit kit (resistor, sources, dependent sources, L, C, mesh-current arrows) sits at the top."""
import os, sys, math
sys.path.insert(0, os.path.dirname(__file__))
from kit import *

FIG = {}
WC = INK          # wire colour


# ---------------- circuit kit ----------------
def wire(*pts, c=WC, w=2, dash=None):
    return P(list(pts), c, w, dash)


def dot(x, y, c=WC):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" style="fill:{c}"/>'


def term(x, y, name, dx=-14, dy=5):
    """an open terminal (small ring) with its name"""
    return (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" style="fill:var(--fig);stroke:{WC};stroke-width:2"/>'
            + T(x + dx, y + dy, name, 15, 'middle', INK, True))


def zig(x1, y1, x2, y2, n=6, amp=8):
    """zigzag between two points (the resistor body)"""
    pts = [(x1, y1)]
    dx, dy = (x2 - x1), (y2 - y1)
    ln = math.hypot(dx, dy); ux, uy = dx / ln, dy / ln; px, py = -uy, ux
    for k in range(n):
        t = (k + 0.5) / n
        s = amp if k % 2 == 0 else -amp
        pts.append((x1 + dx * t + px * s, y1 + dy * t + py * s))
    pts.append((x2, y2))
    return P(pts, WC, 2)


def res_h(x1, x2, y, lab, below=False, body=44, c=WC, lab_fill=INK):
    m = (x1 + x2) / 2
    o = [wire((x1, y), (m - body / 2, y)), zig(m - body / 2, y, m + body / 2, y), wire((m + body / 2, y), (x2, y))]
    o.append(T(m, y + 27 if below else y - 15, lab, 14, fill=lab_fill, bold=True))
    return ''.join(o)


def res_v(x, y1, y2, lab, left=False, body=44, lab_fill=INK, lab2=None):
    m = (y1 + y2) / 2
    o = [wire((x, y1), (x, m - body / 2)), zig(x, m - body / 2, x, m + body / 2), wire((x, m + body / 2), (x, y2))]
    if left:
        o.append(T(x - 14, m + 5, lab, 14, 'end', lab_fill, True))
        if lab2: o.append(T(x - 14, m + 23, lab2, 13, 'end', MUT))
    else:
        o.append(T(x + 14, m + 5, lab, 14, 'start', lab_fill, True))
        if lab2: o.append(T(x + 14, m + 23, lab2, 13, 'start', MUT))
    return ''.join(o)


def circ(x, y, r=17):
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" style="fill:var(--panel);stroke:{WC};stroke-width:2"/>'


def vsrc_v(x, y1, y2, lab, plus_top=True, left=True, r=17):
    m = (y1 + y2) / 2
    o = [wire((x, y1), (x, m - r)), wire((x, m + r), (x, y2)), circ(x, m, r)]
    a, b = ('+', '−') if plus_top else ('−', '+')
    o += [T(x, m - 3, a, 15, bold=True), T(x, m + 13, b, 15, bold=True)]
    o.append(T(x - r - 8, m + 5, lab, 14, 'end', INK, True) if left else T(x + r + 8, m + 5, lab, 14, 'start', INK, True))
    return ''.join(o)


def vsrc_h(x1, x2, y, lab, plus_left=True, r=17, above=True):
    m = (x1 + x2) / 2
    o = [wire((x1, y), (m - r, y)), wire((m + r, y), (x2, y)), circ(m, y, r)]
    a, b = ('+', '−') if plus_left else ('−', '+')
    o += [T(m - 8, y + 5, a, 15, bold=True), T(m + 8, y + 5, b, 15, bold=True)]
    o.append(T(m, y - r - 9 if above else y + r + 19, lab, 14, fill=INK, bold=True))
    return ''.join(o)


def isrc_v(x, y1, y2, lab, up=True, left=False, r=17, lab_fill=INK):
    m = (y1 + y2) / 2
    o = [wire((x, y1), (x, m - r)), wire((x, m + r), (x, y2)), circ(x, m, r)]
    o.append(L(x, m + 10 if up else m - 10, x, m - 8 if up else m + 8, WC, 2.2, arrow='m'))
    o.append(T(x - r - 8, m + 5, lab, 14, 'end', lab_fill, True) if left else T(x + r + 8, m + 5, lab, 14, 'start', lab_fill, True))
    return ''.join(o)


def diamond(x, y, r=19):
    pts = f'{x:.1f},{y - r:.1f} {x + r:.1f},{y:.1f} {x:.1f},{y + r:.1f} {x - r:.1f},{y:.1f}'
    return f'<polygon points="{pts}" style="fill:var(--panel);stroke:{WC};stroke-width:2"/>'


def dep_v(x, y1, y2, lab, kind='v', plus_top=True, up=True, left=False, r=19):
    """dependent source on a vertical wire: kind 'v' (signs) or 'i' (arrow)"""
    m = (y1 + y2) / 2
    o = [wire((x, y1), (x, m - r)), wire((x, m + r), (x, y2)), diamond(x, m, r)]
    if kind == 'v':
        a, b = ('+', '−') if plus_top else ('−', '+')
        o += [T(x, m - 3, a, 14, bold=True), T(x, m + 13, b, 14, bold=True)]
    else:
        o.append(L(x, m + 10 if up else m - 10, x, m - 8 if up else m + 8, WC, 2.2, arrow='m'))
    o.append(T(x - r - 8, m + 5, lab, 14, 'end', LV, True) if left else T(x + r + 8, m + 5, lab, 14, 'start', LV, True))
    return ''.join(o)


def cap_v(x, y1, y2, lab, left=False, gap=7, w=15):
    m = (y1 + y2) / 2
    o = [wire((x, y1), (x, m - gap)), wire((x, m + gap), (x, y2)),
         L(x - w, m - gap, x + w, m - gap, WC, 3), L(x - w, m + gap, x + w, m + gap, WC, 3)]
    o.append(T(x - w - 8, m + 5, lab, 14, 'end', INK, True) if left else T(x + w + 8, m + 5, lab, 14, 'start', INK, True))
    return ''.join(o)


def ind_v(x, y1, y2, lab, left=False, n=4, rr=7):
    m = (y1 + y2) / 2; h = n * 2 * rr; y0 = m - h / 2
    d = f'M{x:.1f},{y0:.1f} ' + ' '.join(f'a{rr},{rr} 0 0 1 0,{2 * rr}' for _ in range(n))
    o = [wire((x, y1), (x, y0)), wire((x, y0 + h), (x, y2)),
         f'<path d="{d}" style="fill:none;stroke:{WC};stroke-width:2"/>']
    o.append(T(x - 16, m + 5, lab, 14, 'end', INK, True) if left else T(x + 16, m + 5, lab, 14, 'start', INK, True))
    return ''.join(o)


def ind_h(x1, x2, y, lab, n=4, rr=7, below=False):
    m = (x1 + x2) / 2; w = n * 2 * rr; x0 = m - w / 2
    d = f'M{x0:.1f},{y:.1f} ' + ' '.join(f'a{rr},{rr} 0 0 1 {2 * rr},0' for _ in range(n))
    o = [wire((x1, y), (x0, y)), wire((x0 + w, y), (x2, y)), f'<path d="{d}" style="fill:none;stroke:{WC};stroke-width:2"/>']
    o.append(T(m, y + 27 if below else y - 15, lab, 14, fill=INK, bold=True))
    return ''.join(o)


def zbox_v(x, y1, y2, lab, left=False, h=40, w=22, lab2=None):
    m = (y1 + y2) / 2
    o = [wire((x, y1), (x, m - h / 2)), wire((x, m + h / 2), (x, y2)), R(x - w / 2, m - h / 2, w, h, 'var(--panel)', WC, 3)]
    o.append(T(x - w / 2 - 8, m + 5, lab, 14, 'end', INK, True) if left else T(x + w / 2 + 8, m + 5, lab, 14, 'start', INK, True))
    if lab2: o.append(T(x - w / 2 - 8, m + 23, lab2, 13, 'end', MUT) if left else T(x + w / 2 + 8, m + 23, lab2, 13, 'start', MUT))
    return ''.join(o)


def zbox_h(x1, x2, y, lab, w=44, h=20, below=False):
    m = (x1 + x2) / 2
    o = [wire((x1, y), (m - w / 2, y)), wire((m + w / 2, y), (x2, y)), R(m - w / 2, y - h / 2, w, h, 'var(--panel)', WC, 3)]
    o.append(T(m, y + 29 if below else y - 17, lab, 14, fill=INK, bold=True))
    return ''.join(o)


def mesh(cx, cy, r, lab, c=LV, val=None):
    """clockwise mesh-current arrow with its name (and value) in the middle"""
    a0, a1 = math.radians(150), math.radians(150 + 285)
    x1, y1 = cx + r * math.cos(a0), cy + r * math.sin(a0)
    x2, y2 = cx + r * math.cos(a1), cy + r * math.sin(a1)
    arr = {LV: 'l', NX: 'x', AC: 'n'}.get(c, 'l')
    o = [f'<path d="M{x1:.1f},{y1:.1f} A{r},{r} 0 1 1 {x2:.1f},{y2:.1f}" style="fill:none;stroke:{c};stroke-width:2.2" marker-end="url(#ar-UID-{arr})"/>']
    if val:
        o += [T(cx, cy - 2, lab, 15, fill=c, bold=True), T(cx, cy + 16, val, 13, fill=c, bold=True)]
    else:
        o.append(T(cx, cy + 5, lab, 15, fill=c, bold=True))
    return ''.join(o)


def note(x, y, s, size=13, anchor='start', fill=MUT, bold=False):
    t = T(x, y, s, size, anchor, fill, bold)
    return t.replace('<text ', '<text xml:space="preserve" ', 1) if '  ' in s else t


def title(x, y, s):
    return T(x, y, s, 14, 'start', INK, True)


def sub(s):
    return f'<tspan dy="4" font-size="11">{s}</tspan><tspan dy="-4"> </tspan>'


def ammeter(x, y1, y2, r=15):
    m = (y1 + y2) / 2
    return (wire((x, y1), (x, m - r)) + wire((x, m + r), (x, y2))
            + f'<circle cx="{x:.1f}" cy="{m:.1f}" r="{r}" style="fill:var(--panel);stroke:{LV};stroke-width:2.2"/>' + T(x, m + 5, 'A', 14, fill=LV, bold=True))


# ---------------- 2.1 mesh analysis: CCVS example and supermesh example ----------------
def f1():
    o = []
    # panel A: worked example 1
    o.append(title(20, 26, 'Worked example 1: mesh analysis with a dependent source'))
    xl, xm, xr, yt, yb = 110, 330, 550, 70, 230
    o.append(vsrc_v(xl, yt, yb, '24 V'))
    o.append(res_h(xl, xm, yt, '2 Ω'))
    o.append(res_h(xm, xr, yt, '2 Ω'))
    o.append(res_v(xm, yt, yb, '4 Ω', left=False))
    o.append(L(xm + 52, 128, xm + 52, 166, LV, 2, arrow='l')); o.append(T(xm + 60, 172, 'iₓ', 14, 'start', LV, True))
    o.append(dep_v(xr, yt, yb, '2iₓ (volts)', 'v', True))
    o.append(wire((xl, yb), (xr, yb)))
    o += [dot(xm, yt), dot(xm, yb)]
    o.append(mesh(222, 152, 36, 'i₁', LV, '6 A'))
    o.append(mesh(438, 152, 36, 'i₂', NX, '3 A'))
    o.append(note(600, 116, 'iₓ = i₁ − i₂', 13, 'start', LV, True))
    o.append(note(600, 136, '= 3 A', 13, 'start', LV))
    o.append(note(20, 262, 'Mesh 1: 6i₁ − 4i₂ = 24     Mesh 2: −2i₁ + 4i₂ = 0     →  i₁ = 6 A, i₂ = 3 A', 14, 'start', INK))
    # divider
    o.append(L(20, 286, 700, 286, LN, 1, '5 5'))
    # panel B: worked example 2, supermesh
    y0 = 300
    o.append(title(20, y0 + 26, 'Worked example 2: a 3 A source shared by both meshes (supermesh)'))
    yt, yb = y0 + 80, y0 + 250
    o.append(vsrc_v(xl, yt, yb, '24 V'))
    o.append(res_h(xl, xm, yt, '2 Ω'))
    o.append(res_h(xm, xr, yt, '3 Ω'))
    o.append(res_v(xm, yt, yt + 70, '5 Ω', left=False, body=36))
    o.append(isrc_v(xm, yt + 70, yb, '3 A', up=True, left=False))
    o.append(res_v(xr, yt, yb, '1 Ω', left=False))
    o.append(wire((xl, yb), (xr, yb)))
    o += [dot(xm, yt), dot(xm, yb)]
    # supermesh boundary: the outer loop, dashed
    o.append(R(xl + 28, yt + 14, xr - xl - 46, yb - yt - 28, 'none', NX, 10, dash='7 5'))
    o.append(mesh(225, (yt + yb) / 2, 34, 'i₁', LV, '2 A'))
    o.append(mesh(442, (yt + yb) / 2, 34, 'i₂', LV, '5 A'))
    o.append(note(xr + 46, yt + 30, 'supermesh', 13, 'start', NX, True))
    o.append(note(xr + 46, yt + 48, '(dashed loop)', 13, 'start', NX))
    o.append(note(xr + 46, yt + 92, 'source arrow up:', 13, 'start', MUT))
    o.append(note(xr + 46, yt + 110, 'i₂ − i₁ = 3 A', 14, 'start', NX, True))
    o.append(note(20, yb + 34, 'Supermesh KVL: 2i₁ + 3i₂ + 1i₂ = 24 (the 5 Ω is not on the loop)  →  i₁ = 2 A, i₂ = 5 A', 14, 'start', INK))
    return yb + 52, ''.join(o)


FIG[1] = (f1, 'Top: the two-mesh circuit of worked example 1; the controlled source 2iₓ depends on the current iₓ = i₁ − i₂ in the 4 Ω '
              'resistor, so the second mesh equation is not symmetric with the first. Bottom: worked example 2, where the 3 A source sits in '
              'the shared branch; one KVL around the dashed outer loop plus i₂ − i₁ = 3 A replaces the two mesh equations.',
          'Two circuits. Top: 24 V source, 2 ohm, shared 4 ohm, 2 ohm and a dependent voltage source 2 i x; mesh currents 6 A and 3 A. '
          'Bottom: 24 V source, 2 ohm, shared branch with 5 ohm and a 3 A current source pointing up, 3 ohm and 1 ohm; '
          'a dashed supermesh loop; mesh currents 2 A and 5 A.')


# ---------------- 2.2 nodal analysis: VCCS example and supernode example ----------------
def f2():
    o = []
    o.append(title(20, 26, 'Worked example 1: nodal analysis with a dependent source'))
    xa, x1, x2, xb, yt, yb = 90, 250, 450, 590, 95, 245
    o.append(isrc_v(xa, yt, yb, '2 A', up=True, left=True))
    o.append(wire((xa, yt), (x1, yt)))
    o.append(res_v(x1, yt, yb, '8 Ω'))
    o.append(res_h(x1, x2, yt, '2 Ω'))
    o.append(note(x1 + 22, yt + 22, '+', 15, 'middle', LV, True)); o.append(note(x2 - 22, yt + 22, '−', 15, 'middle', LV, True))
    o.append(note((x1 + x2) / 2, yt + 26, 'vₓ = v₁ − v₂', 13, 'middle', LV, True))
    o.append(res_v(x2, yt, yb, '3 Ω'))
    o.append(wire((x2, yt), (xb, yt)))
    o.append(dep_v(xb, yt, yb, '0.5vₓ (A)', 'i', up=True))
    o.append(wire((xa, yb), (xb, yb)))
    o += [dot(x1, yt), dot(x2, yt), dot(x1, yb), dot(x2, yb)]
    o.append(Tb(x1, yt - 22, 'v₁ = 8 V', 14, 'middle', AC, True)); o.append(Tb(x2, yt - 22, 'v₂ = 6 V', 14, 'middle', AC, True))
    o.append(note(xb - 80, yb + 26, 'reference node, 0 V', 13, 'start', MUT))
    o.append(note(20, yb + 52, 'Node 1: v₁/8 + (v₁ − v₂)/2 = 2     Node 2: (v₂ − v₁)/2 + v₂/3 = 0.5(v₁ − v₂)', 14, 'start', INK))
    o.append(L(20, yb + 74, 700, yb + 74, LN, 1, '5 5'))
    y0 = yb + 88
    o.append(title(20, y0 + 26, 'Worked example 2: a 6 V source between two nodes (supernode)'))
    xs, n1, n2, n3, xi, yt, yb = 70, 190, 360, 540, 650, y0 + 125, y0 + 275
    o.append(vsrc_v(xs, yt, yb, '12 V'))
    o.append(wire((xs, yt), (n1, yt)))
    o.append(res_h(n1, n2, yt, '2 Ω'))
    o.append(res_v(n2, yt, yb, '3 Ω', left=True))
    o.append(vsrc_h(n2, n3, yt, '6 V', plus_left=False))
    o.append(res_v(n3, yt, yb, '4 Ω'))
    o.append(wire((n3, yt), (xi, yt)))
    o.append(isrc_v(xi, yt, yb, '2 A', up=True))
    o.append(wire((xs, yb), (xi, yb)))
    o += [dot(n1, yt), dot(n2, yt), dot(n3, yt), dot(n2, yb), dot(n3, yb)]
    o.append(R(n2 - 26, yt - 56, n3 - n2 + 52, 96, 'none', NX, 14, dash='7 5'))
    o.append(note((n2 + n3) / 2, yt + 60, 'supernode', 13, 'middle', NX, True))
    o.append(Tb(n1, yt - 26, 'v₁ = 12 V', 14, 'middle', AC, True))
    o.append(Tb(n2 - 2, yt - 66, 'v₂ = 6 V', 14, 'middle', AC, True)); o.append(Tb(n3 + 2, yt - 66, 'v₃ = 12 V', 14, 'middle', AC, True))
    o.append(note(20, yb + 32, 'Supernode KCL: (v₂ − 12)/2 + v₂/3 + v₃/4 = 2   with   v₃ − v₂ = 6', 14, 'start', INK))
    return yb + 50, ''.join(o)


FIG[2] = (f2, 'Top: worked example 1; the controlled current 0.5vₓ depends on the voltage across the 2 Ω resistor, so it is written in '
              'node voltages, 0.5(v₁ − v₂). Bottom: worked example 2; the 12 V source fixes v₁ directly, and the floating 6 V source joins '
              'nodes 2 and 3 into one supernode (dashed) with one KCL plus the constraint v₃ − v₂ = 6 V.',
          'Two circuits. Top: a 2 A source into node 1, 8 ohm to ground, 2 ohm to node 2, 3 ohm to ground and a dependent current source 0.5 v x '
          'into node 2; v1 = 8 V, v2 = 6 V. Bottom: 12 V source to node 1, 2 ohm to node 2, 3 ohm to ground, a 6 V source from node 2 to node 3, '
          '4 ohm to ground and a 2 A source into node 3; a dashed supernode around nodes 2 and 3; v2 = 6 V, v3 = 12 V.')


# ---------------- 2.3 superposition: full circuit and the two single-source runs ----------------
def sp_circuit(x0, y0, vs=True, cs=True, lab_va=''):
    o = []
    xl, xa, xr, yt, yb = x0 + 50, x0 + 170, x0 + 270, y0, y0 + 140
    if vs: o.append(vsrc_v(xl, yt, yb, '12 V'))
    else:
        o.append(wire((xl, yt), (xl, yb), c=NX, w=3)); o.append(note(xl - 10, (yt + yb) / 2 + 5, 'short', 13, 'end', NX, True))
    o.append(res_h(xl, xa, yt, '2 Ω'))
    o.append(res_v(xa, yt, yb, '6 Ω', left=True))
    o.append(wire((xa, yt), (xr, yt)))
    if cs: o.append(isrc_v(xr, yt, yb, '6 A', up=True))
    else:
        o += [wire((xr, yt), (xr, yt + 50)), wire((xr, yb - 50), (xr, yb)), note(xr + 10, (yt + yb) / 2 + 5, 'open', 13, 'start', NX, True)]
    o.append(wire((xl, yb), (xr, yb)))
    o += [dot(xa, yt), dot(xa, yb)]
    o.append(T(xa, yt - 32, 'A', 15, bold=True))
    if lab_va: o.append(Tb(xa, yb + 26, lab_va, 14, 'middle', AC, True))
    return ''.join(o)


def f3():
    o = []
    o.append(title(20, 24, 'Both sources on'))
    o.append(sp_circuit(200, 80, True, True, 'V_A = 18 V'.replace('V_A', 'V' + sub('A'))))
    o.append(L(20, 270, 700, 270, LN, 1, '5 5'))
    o.append(title(20, 296, 'Run 1: 12 V alone (6 A source opened)'))
    o.append(title(380, 296, 'Run 2: 6 A alone (12 V source shorted)'))
    o.append(sp_circuit(20, 352, True, False, "V" + sub('A') + "′ = 9 V"))
    o.append(sp_circuit(370, 352, False, True, "V" + sub('A') + "″ = 9 V"))
    o.append(note(40, 548, 'I = 12/(2 + 6) = 1.5 A, so 1.5 × 6 = 9 V', 13, 'start', MUT))
    o.append(note(400, 548, '2 Ω ∥ 6 Ω = 1.5 Ω, so 6 × 1.5 = 9 V', 13, 'start', MUT))
    o.append(Tb(360, 586, 'Add the runs: 9 V + 9 V = 18 V.   Power: 18²/6 = 54 W, not 13.5 W + 13.5 W = 27 W', 14, 'middle', LV, True))
    return 604, ''.join(o)


FIG[3] = (f3, 'Worked example 1 split into its two single-source runs. A source that is switched off keeps its place: the 6 A source '
              'becomes an open circuit and the 12 V source becomes a short. The node voltages add (9 V + 9 V = 18 V); the powers do not.',
          'Top: a 12 V source with 2 ohm feeding node A, 6 ohm from A to ground, and a 6 A source into A; V A = 18 V. Bottom left: the 6 A '
          'source opened, V A = 9 V. Bottom right: the 12 V source shorted, V A = 9 V.')


# ---------------- 2.4 Thevenin and Norton of the worked-example network ----------------
def f4():
    o = []
    o.append(title(20, 24, 'The network of worked example 1'))
    xs, xn, xa, yt, yb = 70, 230, 370, 80, 230
    o.append(vsrc_v(xs, yt, yb, '32 V'))
    o.append(res_h(xs, xn, yt, '4 Ω'))
    o.append(res_v(xn, yt, yb, '12 Ω'))
    o.append(res_h(xn, xa, yt, '1 Ω'))
    o.append(wire((xs, yb), (xa, yb)))
    o += [dot(xn, yt), dot(xn, yb), term(xa, yt, 'a', 16, 5), term(xa, yb, 'b', 16, 5)]
    # steps box
    bx = 430
    o.append(R(bx, 52, 270, 196, 'var(--accent-soft)', AC, 10))
    o.append(T(bx + 14, 78, 'Three measurements at a-b', 14, 'start', INK, True))
    o.append(T(bx + 14, 106, 'Open: V' + sub('oc') + ' = 32 × 12/16 = 24 V', 13, 'start'))
    o.append(T(bx + 14, 132, 'Dead source: 4 ∥ 12 + 1 = 4 Ω', 13, 'start'))
    o.append(T(bx + 14, 158, 'Short: I' + sub('sc') + ' = 6 A', 13, 'start'))
    o.append(T(bx + 14, 186, 'Check: 24 V / 6 A = 4 Ω', 13, 'start', NX, True))
    o.append(T(bx + 14, 212, 'With an 8 Ω load:', 13, 'start', MUT))
    o.append(T(bx + 14, 232, 'I = 24/(4 + 8) = 2 A', 13, 'start', MUT))
    o.append(L(20, 268, 700, 268, LN, 1, '5 5'))
    # Thevenin form
    o.append(title(20, 294, 'Thevenin form'))
    xs, xa, yt, yb = 150, 330, 340, 480
    o.append(vsrc_v(xs, yt, yb, 'V' + sub('th') + ' = 24 V'))
    o.append(res_h(xs, xa, yt, 'R' + sub('th') + ' = 4 Ω'))
    o.append(wire((xs, yb), (xa, yb)))
    o += [term(xa, yt, 'a', 16, 5), term(xa, yb, 'b', 16, 5)]
    # Norton form
    o.append(title(380, 294, 'Norton form'))
    xi, xr, xa = 450, 560, 660
    o.append(isrc_v(xi, yt, yb, 'I' + sub('N') + ' = 6 A', up=True, left=True))
    o.append(res_v(xr, yt, yb, 'R' + sub('N') + ' = 4 Ω', left=False))
    o.append(wire((xi, yt), (xa, yt))); o.append(wire((xi, yb), (xa, yb)))
    o += [dot(xr, yt), dot(xr, yb), term(xa, yt, 'a', 16, 5), term(xa, yb, 'b', 16, 5)]
    o.append(note(360, 520, 'Same line at a-b: V = 24 − 4I.  Source transformation: 24 V = 6 A × 4 Ω', 14, 'middle', LV, True))
    return 540, ''.join(o)


FIG[4] = (f4, 'Top: the network of worked example 1 and the three numbers found at its terminals. Bottom: the two equivalents; both give '
              '24 V on open circuit, 6 A on short circuit and 2 A in an 8 Ω load.',
          'Top: a 32 V source, 4 ohm series, 12 ohm shunt, 1 ohm series to terminal a; a box lists V oc = 24 V, R th = 4 ohm, I sc = 6 A. '
          'Bottom: Thevenin form, 24 V in series with 4 ohm; Norton form, 6 A in parallel with 4 ohm.')


# ---------------- 2.5 maximum power transfer: computed load-power curve ----------------
def f5():
    o = []
    x0, x1, y0, y1 = 80, 640, 60, 330
    rmax, pmax = 20, 40
    fx = lambda r: x0 + r / rmax * (x1 - x0)
    fy = lambda p: y1 - p / pmax * (y1 - y0)
    o.append(axes(x0, x1, y0, y1, [0, 4, 8, 12, 16, 20], [0, 10, 20, 30, 40], fx, fy, 'load resistance R' + sub('L') + ' (Ω)', 'load power P' + sub('L') + ' (W)'))
    pts = [(fx(r / 10), fy(24 ** 2 * (r / 10) / (4 + r / 10) ** 2)) for r in range(0, 201)]
    o.append(P(pts, AC, 2.8))
    # efficiency (right axis 0..100 %)
    fe = lambda e: y1 - e * (y1 - y0)
    o.append(P([(fx(r / 10), fe((r / 10) / (4 + r / 10))) for r in range(0, 201)], NX, 2.2, '7 5'))
    o.append(L(x1, y0, x1, y1, L2, 1.5))
    for e in (0, 0.5, 1):
        o += [L(x1, fe(e), x1 + 5, fe(e), L2, 1.5), T(x1 + 9, fe(e) + 4.5, f'{int(e * 100)} %', 13, 'start', NX)]
    o.append(T(x1, y0 - 12, 'efficiency η (dashed)', 13, 'end', NX))
    # marked points from the worked example table
    for r, p, lab, dx, dy in ((2, 32, '2 Ω: 32 W', 12, 28), (8, 32, '8 Ω: 32 W', 6, -14)):
        o.append(C(fx(r), fy(p), 5, LV))
        o.append(Tb(fx(r) + dx, fy(p) + dy, lab, 13, 'start', LV, True))
    o.append(L(fx(4), fy(36), fx(4), y1, LV, 1.5, '4 4'))
    o.append(C(fx(4), fy(36), 6, LV))
    o.append(Tb(fx(4) + 10, fy(36) - 22, 'peak: R' + sub('L') + ' = R' + sub('th') + ' = 4 Ω, P = 36 W', 14, 'start', LV, True))
    o.append(C(fx(4), fe(0.5), 5, NX)); o.append(Tb(fx(4) + 10, fe(0.5) + 20, 'η = 50 % at the peak', 13, 'start', NX, True))
    return 380, ''.join(o)


FIG[5] = (f5, 'Load power from the Thevenin source of worked example 1 (24 V, 4 Ω), computed for loads from 0 to 20 Ω. The power peaks '
              'at 36 W when the load equals 4 Ω, and 2 Ω and 8 Ω both give 32 W. The dashed curve is the efficiency of the equivalent '
              'circuit, only 50 % at the peak and rising towards 100 % for large loads.',
          'A curve of load power against load resistance rising from 0 to a peak of 36 W at 4 ohm and falling to 23 W at 16 ohm; points at '
          '2 ohm and 8 ohm, both 32 W; a dashed efficiency curve rising from 0 through 50 percent at 4 ohm.')


# ---------------- 2.6 Millman (worked example 1) and reciprocity (worked example 2) ----------------
def f6():
    o = []
    o.append(title(20, 24, 'Worked example 1: Millman’s theorem'))
    yA, yB = 70, 230
    xs = [90, 230, 370]
    o.append(wire((xs[0], yA), (500, yA))); o.append(wire((xs[0], yB), (500, yB)))
    for x, (v, r) in zip(xs, [('12 V', '3 Ω'), ('24 V', '6 Ω'), (None, '2 Ω')]):
        if v:
            o.append(res_v(x, yA, yA + 70, r, body=34))
            o.append(vsrc_v(x, yA + 70, yB, v, plus_top=True, left=False, r=16))
        else:
            o.append(res_v(x, yA, yB, r))
        o += [dot(x, yA), dot(x, yB)]
    o.append(term(500, yA, 'A', 18, 5)); o.append(term(500, yB, 'B', 18, 5))
    o.append(L(540, 150, 580, 150, MUT, 2, arrow='m'))
    o.append(R(590, 80, 120, 140, 'var(--accent-soft)', AC, 10))
    o.append(T(650, 112, 'V' + sub('AB') + ' = 8 / 1', 14, bold=True)); o.append(T(650, 136, '= 8 V', 14, fill=AC, bold=True))
    o.append(T(650, 166, 'R = 1/ΣG', 13)); o.append(T(650, 188, '= 1 Ω', 13, fill=AC, bold=True))
    o.append(note(20, 262, 'ΣV/R = 4 + 4 + 0 = 8 A     ΣG = 1/3 + 1/6 + 1/2 = 1 S     currents into A: 1.33 A, 2.67 A, −4 A (sum 0)', 13, 'start', INK))
    o.append(L(20, 282, 700, 282, LN, 1, '5 5'))
    o.append(title(20, 308, 'Worked example 2: reciprocity in a T network'))
    for k, (x0, src_left) in enumerate(((20, True), (370, False))):
        yt, yb = 360, 480
        xl, xm, xr = x0 + 40, x0 + 165, x0 + 290
        o.append(res_h(xl, xm, yt, '2 Ω')); o.append(res_h(xm, xr, yt, '3 Ω'))
        o.append(res_v(xm, yt, yb, '6 Ω', left=False))
        o.append(wire((xl, yb), (xr, yb))); o += [dot(xm, yt), dot(xm, yb)]
        if src_left:
            o.append(vsrc_v(xl, yt, yb, '24 V'))
            o.append(ammeter(xr, yt, yb)); o.append(T(xr - 26, yt + 66, '4 A', 14, 'end', LV, True))
            o.append(note(x0 + 165, yb + 30, 'source left, ammeter right', 13, 'middle', MUT))
        else:
            o.append(vsrc_v(xr, yt, yb, '24 V', left=False))
            o.append(ammeter(xl, yt, yb)); o.append(T(xl + 26, yt + 66, '4 A', 14, 'start', LV, True))
            o.append(note(x0 + 165, yb + 30, 'swapped: the same 4 A', 13, 'middle', MUT))
    return 528, ''.join(o)


FIG[6] = (f6, 'Top: the three branches of worked example 1 collapse to one source of 8 V behind 1 Ω. Bottom: worked example 2; the '
              '24 V source and the ammeter trade places in the T network and the ammeter reads 4 A both times.',
          'Top: three parallel branches between A and B, 12 V with 3 ohm, 24 V with 6 ohm, and 2 ohm, giving V AB = 8 V and 1 ohm. '
          'Bottom: a T network of 2 ohm, 6 ohm and 3 ohm; a 24 V source on one side and an ammeter reading 4 A on the other, then swapped.')


# ---------------- 2.7 compensation theorem ----------------
def comp_circ(x0, y0, rlab, ilab, show_src=True, vc=None):
    o = []
    xs, xn, xr, yt, yb = x0 + 50, x0 + 170, x0 + 290, y0, y0 + 140
    if show_src: o.append(vsrc_v(xs, yt, yb, '30 V'))
    else:
        o.append(wire((xs, yt), (xs, yb), c=NX, w=3)); o.append(note(xs - 10, (yt + yb) / 2 + 5, 'short', 13, 'end', NX, True))
    o.append(res_h(xs, xn, yt, '2 Ω'))
    o.append(res_v(xn, yt, yb, '6 Ω', left=True))
    o.append(wire((xn, yt), (xr, yt)))
    if vc:
        o.append(res_v(xr, yt, yt + 62, rlab, body=32))
        o.append(vsrc_v(xr, yt + 62, yb, vc, plus_top=True, left=False, r=16))
    else:
        o.append(res_v(xr, yt, yb, rlab))
    o.append(wire((xs, yb), (xr, yb)))
    o += [dot(xn, yt), dot(xn, yb)]
    if vc: o.append(L(xr - 22, yt + 90, xr - 22, yt + 40, LV, 2, arrow='l'))
    else: o.append(L(xr - 22, yt + 40, xr - 22, yt + 90, LV, 2, arrow='l'))
    o.append(T(xr - 28, yt + 70, ilab, 14, 'end', LV, True))
    return ''.join(o)


def f7():
    o = []
    o.append(title(20, 24, '(a) Original: 3 Ω branch'))
    o.append(title(380, 24, '(b) Changed: 3 Ω becomes 4 Ω'))
    o.append(comp_circ(10, 70, '3 Ω', 'I = 5 A'))
    o.append(comp_circ(370, 70, '4 Ω', '4.091 A'))
    o.append(L(20, 252, 700, 252, LN, 1, '5 5'))
    o.append(title(20, 278, '(c) Compensation network: sources dead, V' + sub('c') + ' = IΔR = 5 × 1 = 5 V opposing I'))
    o.append(comp_circ(10, 330, '4 Ω', '0.909 A', show_src=False, vc='5 V'))
    bx = 370
    o.append(R(bx, 318, 330, 150, 'var(--accent-soft)', AC, 10))
    o.append(T(bx + 14, 344, 'ΔI = 5/(4 + 2 ∥ 6) = 5/5.5', 13, 'start'))
    o.append(T(bx + 14, 366, '= 0.909 A against I', 13, 'start', LV, True))
    o.append(T(bx + 14, 392, 'New current: 5 − 0.909 = 4.091 A', 13, 'start', INK, True))
    o.append(T(bx + 14, 418, 'In 6 Ω: +0.227 A (2.5 → 2.727 A)', 13, 'start'))
    o.append(T(bx + 14, 442, 'In 2 Ω: −0.682 A (7.5 → 6.818 A)', 13, 'start'))
    o.append(note(20, 498, 'Check by solving (b) directly: 30/(2 + 6 ∥ 4) = 6.818 A from the source, 6.818 × 6/10 = 4.091 A in the 4 Ω.', 13, 'start', MUT))
    return 514, ''.join(o)


FIG[7] = (f7, 'Worked example 1: the 3 Ω branch carrying 5 A becomes 4 Ω. The compensation network (c) has the 30 V source shorted '
              'and a 5 V source (5 A × 1 Ω) in the changed branch; the currents it drives are exactly the changes from (a) to (b).',
          'Three circuits. (a) 30 V source, 2 ohm, 6 ohm shunt and a 3 ohm branch carrying 5 A. (b) The branch changed to 4 ohm, carrying '
          '4.091 A. (c) The source shorted and a 5 V compensating source in series with the 4 ohm branch, driving a change of 0.909 A.')


# ---------------- 2.8 AC: phasor mesh circuit and its Thevenin equivalent ----------------
def f8():
    o = []
    o.append(title(20, 24, 'Worked example 1: phasor mesh analysis (RMS)'))
    xl, xm, xr, yt, yb = 90, 250, 450, 80, 250
    o.append(vsrc_v(xl, yt, yb, '20∠0° V'))
    o.append(res_h(xl, xm, yt, '4 Ω'))
    o.append(cap_v(xm, yt, yb, '−j4 Ω'))
    o.append(wire((xm, yt), (xr, yt)))
    o.append(res_v(xr, yt, yt + 80, '4 Ω', body=36))
    o.append(ind_v(xr, yt + 80, yb, 'j4 Ω'))
    o.append(wire((xl, yb), (xr, yb)))
    o += [dot(xm, yt), dot(xm, yb)]
    o.append(mesh(172, 168, 34, 'I₁', LV))
    o.append(mesh(360, 168, 34, 'I₂', NX))
    o.append(note(xr + 64, 120, 'load', 13, 'start', MUT))
    o.append(note(xr + 64, 138, '4 + j4 Ω', 13, 'start', MUT, True))
    o.append(note(20, 288, 'I₁ = 2 + j1 A = 2.236∠26.6° A      I₂ = 1 − j2 A = 2.236∠−63.4° A', 14, 'start', INK))
    o.append(L(20, 310, 700, 310, LN, 1, '5 5'))
    o.append(title(20, 336, 'Worked example 2: the same circuit seen from the load'))
    xs, xa, yt, yb = 190, 380, 390, 520
    o.append(vsrc_v(xs, yt, yb, 'V' + sub('th') + ' = 10 − j10 V'))
    o.append(zbox_h(xs, xa, yt, 'Z' + sub('th') + ' = 2 − j2 Ω'))
    o.append(wire((xs, yb), (xa, yb)))
    o += [term(xa, yt, 'a', 0, -12), term(xa, yb, 'b', 0, 26)]
    o.append(wire((xa, yt), (450, yt))); o.append(wire((xa, yb), (450, yb)))
    o.append(zbox_v(450, yt, yb, 'Z' + sub('L') + ' = 2 + j2 Ω', lab2='(conjugate match)'))
    o.append(R(592, 380, 118, 120, 'var(--accent-soft)', AC, 10))
    o.append(T(651, 406, 'P' + sub('max'), 14, bold=True))
    o.append(T(651, 428, '14.14²/(4 × 2)', 13))
    o.append(T(651, 452, '= 25 W', 15, fill=AC, bold=True))
    o.append(T(651, 480, '4 + j4 Ω: 20 W', 13, fill=MUT))
    return 552, ''.join(o)


FIG[8] = (f8, 'Top: the phasor circuit of worked example 1, with the 4 + j4 Ω load in the right mesh. Bottom: worked example 2 replaces '
              'everything left of the load by V_th = 10 − j10 V behind Z_th = 2 − j2 Ω; the conjugate load 2 + j2 Ω takes 25 W, '
              'against 20 W for the original 4 + j4 Ω load.'.replace('V_th', 'V<sub>th</sub>').replace('Z_th', 'Z<sub>th</sub>'),
          'Top: a 20 V RMS source, 4 ohm, a shared capacitor of minus j4 ohm, and a load of 4 ohm with j4 ohm; mesh currents I1 = 2 + j1 A and '
          'I2 = 1 − j2 A. Bottom: the Thevenin equivalent 10 − j10 V behind 2 − j2 ohm, with a conjugate load 2 + j2 ohm taking 25 W.')


spec = make_spec(FIG)


def text_fixes(k):
    return []
