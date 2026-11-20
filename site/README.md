# University Free N Easy website

The public site: free lessons and notes, found by **degree → department → subject → topic → lesson**.
This folder builds it as plain static files. No frameworks, no packages to install.

## Build

From the repo root:

```
python3 site/build.py
```

It writes the whole site to `site/dist/` (ignored by git). Python 3.8 or newer, standard library only.

The build stops if any page shows a college name, a unit number or a lesson number. Topics and lessons are shown
by name only. The numbers live only inside the notes PDF file names, which must never change.

## What is in here

| Path | What it is |
|---|---|
| `build.py` | The generator. Reads the syllabus and the data files, writes every page, the search index and the sitemap. |
| `data/site.json` | The degrees shown (primary degrees only), department names and addresses, the notes address, the site address. |
| `data/lessons.json` | The lessons of each topic: title, chapters, minutes, YouTube id. Same shape as the data pack's `videos.json`. |
| `templates/home.html` | The home page (the approved design with its scroll scenes). `build.py` fills in the numbers, the degree directory and the featured lessons. |
| `assets/` | `site.css` (inner pages), `home.js` (home scroll scenes), `site.js` (tap-to-play, mark as done, search), logo, campus picture. |
| `tools/import_lessons.py` | Adds lessons from `videos.json` or a subject's `upload_sheet.json`. |
| `vendor/make_site.py` | The data pack's site script (v46). `build.py` reuses its chapter helpers and its college-name pattern. |

The syllabus itself comes from `pack/universal.json`.

## Adding lessons and video links

1. Run the importer on the lesson pipeline's files, as many as you like:

   ```
   python3 site/tools/import_lessons.py path/to/videos.json path/to/upload_sheet.json
   ```

2. For a lesson that is on YouTube, put its id (the part after `v=`) in `"video"` in `data/lessons.json`.
   A lesson with no id shows "The video for this lesson is on its way".
3. Build again and deploy.

A lesson marked `"notes": false` hides its notes PDF link. It is used for lessons whose place in the topic is not
confirmed yet; the importer removes the mark when the real entry arrives.

## Notes PDFs

The site does not hold the notes PDFs. It links to `https://ufe-notes.pages.dev/<lesson key>.pdf`, the address already
in every YouTube description. The `ufe-notes` Cloudflare project is never touched by this site, so those links cannot break here.

## Deploying on Cloudflare Pages (free plan)

**Quick way, by upload** (the same way `ufe-notes` is deployed):

1. Build, or unzip the `ufe-site-dist.zip` sent in chat.
2. Cloudflare dashboard → Workers & Pages → Create → Pages → Upload assets.
3. Name the project (it becomes `<name>.pages.dev`), drag the `dist` folder in, Deploy.

**Automatic way, from GitHub** (needed for phase 2; every push then deploys itself):

1. Workers & Pages → Create → Pages → Connect to Git → pick `SwathishThiyagu/ufe-books`.
2. Production branch: `main`. Framework preset: None. Build command: `python3 site/build.py`. Build output directory: `site/dist`.
3. After the project exists, open its Settings → Builds:
   - Branch control: preview branches = Custom, include `website`. The repo has hundreds of book branches; without this each push to one would use up a build.
   - Build watch paths: include `site/*` and `pack/universal.json`, so book commits do not rebuild the site.
4. The `website` branch then gets its own preview address. `main` goes live once the site is merged there.
   Until then the production build on `main` fails, because `main` has no `site/` folder yet. That is expected.

If a build cannot find Python, add the environment variable `PYTHON_VERSION` = `3.11` in the project's settings.

When the site has its final address, put it in `site_url` in `data/site.json` and rebuild: the sitemap and canonical links are written only then.

## Phase 2 (not built yet)

Free Google sign-in for full topic books, a D1 database (name, email, sign-up date only), a delete-my-account button,
a privacy page for it, and an owner-only admin page. No key or secret ever goes in this repo, because the repo is public.
