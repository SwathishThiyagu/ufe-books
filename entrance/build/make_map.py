"""Writes entrance/map/index.html from map_template.html and map_data.json."""
import os
here = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(here, "map_template.html")).read()
d = open(os.path.join(here, "map_data.json")).read().replace("</", "<\\/")
os.makedirs(os.path.join(here, "..", "map"), exist_ok=True)
open(os.path.join(here, "..", "map", "index.html"), "w").write(t.replace("__DATA__", d))
print("map written")
