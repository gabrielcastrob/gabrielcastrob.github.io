# Gabriel Castro B. — Portfolio

Interactive personal portfolio (geospatial / remote sensing) built with **Python + Jinja2**
and published on **GitHub Pages**. Dark "ArcGIS-style" theme with an interactive
Leaflet map scrollytelling section and Plotly charts.

🔗 **Live site:** https://gabrielcastrob.github.io

---

## 🧭 How it works

The site is a **static site generator**: you edit one content file in Python and a
build script renders the final HTML.

```
gabrielcastrob.github.io/
├── content.py          ← EDIT THIS: all text, publications, experience, etc.
├── build.py            ← run this to (re)generate the site
├── templates/
│   └── index.html      ← page structure (Jinja2 template)
├── assets/
│   ├── css/style.css   ← theme & colors (CSS variables at the top)
│   ├── js/main.js      ← maps, charts, animations
│   ├── data/*.geojson  ← demo geographic layers (replace with real ones)
│   └── img/            ← images
├── visualizations/     ← drop your REAL products here (see its README)
├── index.html          ← GENERATED output (served by GitHub Pages)
└── requirements.txt
```

## 🚀 Quick start

```bash
# 1. Install the only dependency
pip install -r requirements.txt

# 2. Edit your content
#    open content.py and change the text

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
| Map tour stops | `content.py` → `MAP_STORY` |
| Publications / conferences | `content.py` → `PUBLICATIONS`, `CONFERENCES` |
| Gallery products | `content.py` → `VISUALS` + files in `visualizations/` |
| Contact & social links | `content.py` → `CONTACT` |
| Colors / theme | `assets/css/style.css` → `:root` variables |
| Chart data | `assets/js/main.js` → `initCharts()` |

After **any** change to `content.py` or the template, run `python build.py` again.

## 🌐 Deployment (GitHub Pages)

This repo is named `gabrielcastrob.github.io`, so GitHub Pages serves the root of the
`main` branch automatically at https://gabrielcastrob.github.io. Just commit and push:

```bash
git add .
git commit -m "Update portfolio content"
git push
```

---

*Built with Python, Leaflet and Plotly.*
