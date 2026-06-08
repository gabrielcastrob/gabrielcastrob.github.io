# -*- coding: utf-8 -*-
"""
==============================================================================
 build.py  ·  Generador del sitio  (Gabriel Castro B. — portafolio)
==============================================================================
Qué hace:
  1. Lee todo el contenido desde  content.py
  2. Renderiza  templates/index.html  con Jinja2
  3. Escribe el resultado en  ./index.html  (que GitHub Pages publica)

Uso:
    python build.py            # genera index.html
    python build.py --serve    # genera y lanza un servidor local en :8000

Sólo necesitas la librería Jinja2:
    pip install -r requirements.txt
==============================================================================
"""
import sys
import http.server
import socketserver
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

import content  # <-- tu archivo de contenido editable

ROOT = Path(__file__).parent
TEMPLATES_DIR = ROOT / "templates"
OUTPUT_FILE = ROOT / "index.html"
PORT = 8000


def build():
    """Renderiza la plantilla principal y la escribe en index.html."""
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = env.get_template("index.html")

    # Pasamos cada sección de content.py al contexto de la plantilla.
    html = template.render(
        site=content.SITE,
        hero=content.HERO,
        about=content.ABOUT,
        skills=content.SKILLS,
        education=content.EDUCATION,
        experience=content.EXPERIENCE,
        map_story=content.MAP_STORY,
        visuals=content.VISUALS,
        publications=content.PUBLICATIONS,
        conferences=content.CONFERENCES,
        contact=content.CONTACT,
        footer=content.FOOTER,
    )

    OUTPUT_FILE.write_text(html, encoding="utf-8")
    print(f"[OK] Sitio generado -> {OUTPUT_FILE}")


def serve():
    """Lanza un pequeño servidor local para previsualizar el sitio."""
    import os
    os.chdir(ROOT)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"[SERVE] http://localhost:{PORT}  (Ctrl+C para detener)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[SERVE] Servidor detenido.")


if __name__ == "__main__":
    build()
    if "--serve" in sys.argv:
        serve()
