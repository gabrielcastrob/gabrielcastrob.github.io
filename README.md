# Gabriel Castro B. — Portfolio

Interactive personal portfolio (geospatial / remote sensing) built with **Python + Jinja2**
and published on **GitHub Pages**. Clean light theme with an interactive **Leaflet map
scrollytelling** section (Esri physical basemap) that flies to each project and unfolds
its figures over the map.

🔗 **Live site:** https://gabrielcastrob.github.io/MGI_PortafolioVis/

> The live site only works after enabling GitHub Pages — see *Deployment* below.

---

## 🧭 How it works

The site is a **static site generator**: you edit one content file in Python and a
build script renders the final HTML.

```
MGI_PortafolioVis/
├── content.py          ← EDIT THIS: all text, projects, experience, etc.
├── build.py            ← run this to (re)generate the site
├── templates/
│   └── index.html      ← page structure (Jinja2 template)
├── assets/
│   ├── css/style.css   ← theme & colors (CSS variables at the top)
│   ├── js/main.js      ← map scrollytelling + animations
│   └── img/            ← images (papers / field / wageningen)
├── visualizations/     ← drop extra products here (see its README)
├── index.html          ← GENERATED output (served by GitHub Pages)
└── requirements.txt
```

## 🚀 Quick start

```bash
# 1. Install the only dependency
pip install -r requirements.txt

# 2. Edit your content
#    open content.py and change the text / add images

# 3. Build the site
python build.py

# 4. Preview locally (optional)
python build.py --serve
#    then open http://localhost:8000
```

## ✏️ Editing guide

| I want to change… | Edit… |
|---|---|
| Name, role, intro | `content.py` → `HERO`, `ABOUT` |
| Skills | `content.py` → `SKILLS` |
| Experience / education | `content.py` → `EXPERIENCE`, `EDUCATION` |
| Map tour stops (papers / field / Wageningen) | `content.py` → `WORK["steps"]` |
| Project figures | add files to `assets/img/...` and list them in each step's `images` |
| Contact & social links | `content.py` → `CONTACT` |
| Colors / theme | `assets/css/style.css` → `:root` variables |
| Map base layer / behaviour | `assets/js/main.js` → `initWorkMap()` |

After **any** change to `content.py` or the template, run `python build.py` again.

### Adding a real project figure
1. Copy your image to `assets/img/field/` or `assets/img/wageningen/`
   (paper figures already live in `assets/img/papers/`).
2. In `content.py`, find the matching step in `WORK["steps"]` and add the path to
   its `images` list, e.g. `"images": ["assets/img/field/patagonia.jpg"]`.
3. Run `python build.py` and commit.

## 🌐 Deployment (GitHub Pages)

1. On GitHub: **Settings → Pages**.
2. **Source:** *Deploy from a branch* · **Branch:** `main` · **Folder:** `/ (root)` · **Save**.
3. After ~1 minute the site is live at:
   **https://gabrielcastrob.github.io/MGI_PortafolioVis/**

To update the site afterwards, just rebuild and push:

```bash
python build.py
git add .
git commit -m "Update portfolio content"
git push
```

---

*Built with Python and Leaflet.*
