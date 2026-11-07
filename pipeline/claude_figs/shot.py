import sys
from playwright.sync_api import sync_playwright
src, out = sys.argv[1], sys.argv[2]; scale = float(sys.argv[3]) if len(sys.argv) > 3 else 1
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 820, 'height': 1000}, device_scale_factor=scale)
    pg.goto('file://' + src); pg.wait_for_timeout(500)
    for f in pg.query_selector_all('figure.fig'):
        cap = f.inner_text()
        import re
        m = re.search(r'Figure \d+\.(\d+)\.1', cap)
        if m: f.screenshot(path=f'{out}-{m.group(1)}.png')
    b.close()
