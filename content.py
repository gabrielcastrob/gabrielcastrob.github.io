# -*- coding: utf-8 -*-
"""
==============================================================================
 CONTENIDO DEL PORTAFOLIO  ·  Gabriel Castro B.
==============================================================================
Este es el ÚNICO archivo que necesitas editar para cambiar los textos del sitio.
Después de editar, ejecuta:   python build.py
y se regenerará  index.html  con tus cambios.

Cada sección está claramente separada con comentarios. Edita los valores entre
comillas. Para añadir un elemento a una lista, copia un bloque { ... } existente.
==============================================================================
"""

# -----------------------------------------------------------------------------
# 1. DATOS GENERALES DEL SITIO  (cabecera del navegador, SEO, etc.)
# -----------------------------------------------------------------------------
SITE = {
    "title": "Gabriel Castro B. · Geo-information Scientist",
    "description": "Geographer & remote sensing researcher — MSc Geo-information "
                   "Science at Wageningen University & Research.",
    "author": "Gabriel Castro B.",
    # URL final del sitio (sitio de usuario de GitHub Pages):
    "url": "https://gabrielcastrob.github.io",
    "lang": "en",
}

# -----------------------------------------------------------------------------
# 2. SECCIÓN HERO  (lo primero que se ve al abrir la página)
# -----------------------------------------------------------------------------
HERO = {
    "name": "Gabriel Castro B.",
    "role": "Geographer · Remote Sensing Researcher",
    "subtitle": "MSc Geo-information Science — Wageningen University &amp; Research",
    "tagline": "Turning satellite, UAV and LiDAR data into insight about how "
               "landscapes change — from the drylands of Chile to the "
               "polders of the Netherlands.",
    # Botones de llamada a la acción del hero:
    "cta_primary": {"label": "Explore my work", "href": "#work"},
    "cta_secondary": {"label": "Get in touch", "href": "#contact"},
    # Imagen de fondo del hero (déjala vacía "" para usar el fondo animado por defecto).
    # Más adelante puedes poner: "assets/img/hero.jpg"
    "background_image": "",
}

# -----------------------------------------------------------------------------
# 3. SOBRE MÍ
# -----------------------------------------------------------------------------
ABOUT = {
    "heading": "About me",
    "profile": (
        "Geographer with 3+ years of research experience in land-surface "
        "phenology, land-use / land-cover change and climate analysis using "
        "optical remote sensing, UAV multispectral imagery and GIS across "
        "Chilean ecosystems. I am currently pursuing an MSc in Geo-information "
        "Science at Wageningen University &amp; Research, focusing on machine "
        "learning and deep learning methods for remote sensing applications."
    ),
    "interests": (
        "I am driven by applying machine learning and deep learning to "
        "real-world problems in the remote sensing domain — object detection, "
        "segmentation and classification of aerial and satellite imagery — and "
        "by communicating technical results clearly to specialist and "
        "non-specialist audiences alike."
    ),
    # Cifras destacadas (puedes editar número y etiqueta, o añadir/quitar):
    "stats": [
        {"value": "3+",   "label": "Years of research"},
        {"value": "3",    "label": "Peer-reviewed papers"},
        {"value": "4",    "label": "ANID-funded projects"},
        {"value": "100+", "label": "UAV flight hours"},
    ],
}

# -----------------------------------------------------------------------------
# 4. HABILIDADES  (tarjetas de competencias técnicas)
# -----------------------------------------------------------------------------
SKILLS = [
    {
        "icon": "satellite",
        "title": "Remote Sensing",
        "items": ["Sentinel-1 / 2", "Landsat", "MODIS", "UAV multispectral",
                  "LiDAR / point clouds"],
    },
    {
        "icon": "code",
        "title": "Software &amp; Programming",
        "items": ["Python (PyTorch, scikit-learn, pandas)", "R",
                  "Google Earth Engine (JS)", "ArcGIS Pro", "QGIS",
                  "CloudCompare", "Pix4D", "Agisoft Metashape"],
    },
    {
        "icon": "brain",
        "title": "Deep Learning",
        "items": ["CNNs", "YOLO", "R-CNN", "DETR", "Vision Transformers (ViT)"],
    },
    {
        "icon": "drone",
        "title": "UAV Operations",
        "items": ["Certified drone pilot (Chile)", "DJI M300 RTK",
                  "DJI Mini 4 Pro", "Mavic 2 Pro", "100+ flight hours"],
    },
]

# -----------------------------------------------------------------------------
# 5. EDUCACIÓN
# -----------------------------------------------------------------------------
EDUCATION = [
    {
        "period": "2025 – 2027",
        "degree": "MSc Geo-information Science",
        "place": "Wageningen University &amp; Research, Netherlands",
        "detail": "Advanced Earth Observation (GRS32306), Machine Learning "
                  "(FTE35306), Deep Learning (AIN31306).",
    },
    {
        "period": "2024",
        "degree": "Diploma in Data Science",
        "place": "Universidad de Santiago, Chile",
        "detail": "Python, statistics, machine learning and advanced ML methods.",
    },
    {
        "period": "2017 – 2021",
        "degree": "Bachelor in Geography",
        "place": "Pontifical Catholic University of Valparaíso, Chile",
        "detail": "Remote sensing, GIS I–III, spatial analysis.",
    },
]

# -----------------------------------------------------------------------------
# 6. EXPERIENCIA  (línea de tiempo: investigación + docencia)
#    type = "research"  o  "teaching"  (sólo cambia el color de la etiqueta)
# -----------------------------------------------------------------------------
EXPERIENCE = [
    {
        "type": "research",
        "period": "2023 – 2025",
        "title": "Research Assistant — FONDECYT Nº1201527",
        "org": "ANID, Chile · PI: Roberto O. Chávez",
        "detail": "A spatiotemporal assessment of major disturbances on Chilean "
                  "vegetation phenology, productivity and resilience using 40 "
                  "years of continuous remote sensing records.",
    },
    {
        "type": "research",
        "period": "2023 – 2025",
        "title": "Research Assistant — FONDEF IDEA ID:23I10058",
        "org": "ANID, Chile · PI: S. Fingerhuth &amp; I. Kopaitic",
        "detail": "Light pollution — validation of aerial methods for the "
                  "quantification and identification of pollution sources.",
    },
    {
        "type": "research",
        "period": "2022 – 2023",
        "title": "Research Assistant — FONDECYT N°1201714",
        "org": "ANID, Chile · PI: Ariel N. Muñoz",
        "detail": "Assessing historical changes of water extreme events and "
                  "their impacts on vegetation, water access and infrastructure "
                  "planning in Mediterranean and semi-arid basins of Chile.",
    },
    {
        "type": "teaching",
        "period": "2022 – 2024",
        "title": "Lecturer &amp; Training Instructor",
        "org": "PUCV — Institute of Geography",
        "detail": "Remote Sensing (GEO1053-1), GIS II (GEO1045-1), Diploma in "
                  "Geoinformation &amp; RS (120 h), Introduction to GIS &amp; "
                  "Spatial Analysis (30 h).",
    },
    {
        "type": "teaching",
        "period": "2018 – 2021",
        "title": "Teaching Assistant",
        "org": "PUCV — Institute of Geography",
        "detail": "Remote Sensing, GIS II, Geomorphology II, Physical Geography.",
    },
]

# -----------------------------------------------------------------------------
# 7. SCROLLYTELLING DE MAPA  (sección interactiva estilo ArcGIS Experience)
#    Cada "step" es un panel de texto que, al hacer scroll, cambia la vista del
#    mapa Leaflet (center = [lat, lon], zoom) y resalta una capa de datos.
#    Los datos GeoJSON ficticios están en  assets/data/  y se pueden reemplazar
#    por los tuyos reales más adelante (mismo nombre de archivo o cambia 'layer').
# -----------------------------------------------------------------------------
MAP_STORY = {
    "heading": "Research in the field",
    "intro": "A guided tour through the landscapes behind my work. "
             "Scroll to move across study sites — these layers are placeholder "
             "demos and will be replaced with real products soon.",
    "steps": [
        {
            "title": "Central Chile — the megadrought",
            "center": [-33.05, -71.40],
            "zoom": 9,
            "layer": "study_basins",          # -> assets/data/study_basins.geojson
            "text": "Since 2010, central Chile has endured an uninterrupted "
                    "megadrought. I mapped vegetation greenness and urban "
                    "greening dynamics across the Gran Valparaíso conurbation.",
        },
        {
            "title": "Petorca river basin — irrigation patterns",
            "center": [-32.25, -70.95],
            "zoom": 10,
            "layer": "ndvi_grid",             # -> assets/data/ndvi_grid.geojson
            "text": "Using MODIS EVI time series and hydro-climate records I "
                    "evaluated the spatio-temporal evolution of irrigation in "
                    "agricultural areas of the Petorca basin.",
        },
        {
            "title": "UAV multispectral campaigns",
            "center": [-32.78, -71.22],
            "zoom": 13,
            "layer": "flight_area",           # -> assets/data/flight_area.geojson
            "text": "I flew DJI M300 RTK and Mavic platforms to capture "
                    "high-resolution multispectral imagery, validating satellite "
                    "drought signals on the ground.",
        },
        {
            "title": "Wageningen — a new chapter",
            "center": [51.985, 5.665],
            "zoom": 12,
            "layer": "wageningen",            # -> assets/data/wageningen.geojson
            "text": "Now in the Netherlands, I apply deep learning to earth "
                    "observation — from point-cloud processing to object "
                    "detection on aerial imagery.",
        },
    ],
}

# -----------------------------------------------------------------------------
# 8. VISUALIZACIONES / PRODUCTOS
#    'charts' = gráficos Plotly interactivos generados con datos ficticios
#    (edita los datos en assets/js/main.js si quieres cambiar las cifras).
#    'gallery' = tarjetas para tus productos reales. Cuando subas tu carpeta de
#    visualizaciones, apunta 'src' al archivo (imagen, .html de mapa, etc.).
# -----------------------------------------------------------------------------
VISUALS = {
    "heading": "Data products &amp; visualizations",
    "intro": "Selected outputs from my research and from the MSc Geo-information "
             "Science programme at Wageningen. The charts below are interactive "
             "demos; the gallery will host real products soon.",
    "gallery": [
        {
            "title": "NDVI anomaly map (demo)",
            "tag": "Remote sensing",
            "caption": "Vegetation greenness anomaly during a drought year. "
                       "Placeholder — replace with your real raster export.",
            "src": "",   # ej: "visualizations/ndvi_anomaly.png"
        },
        {
            "title": "Land-cover classification (demo)",
            "tag": "Machine learning",
            "caption": "Supervised LULC classification of a study basin. "
                       "Placeholder — replace with your real map.",
            "src": "",   # ej: "visualizations/lulc_2020.png"
        },
        {
            "title": "Point-cloud / DSM (demo)",
            "tag": "UAV · LiDAR",
            "caption": "Digital surface model derived from UAV photogrammetry. "
                       "Placeholder — replace with your real product.",
            "src": "",   # ej: "visualizations/dsm_hillshade.png"
        },
    ],
}

# -----------------------------------------------------------------------------
# 9. PUBLICACIONES CIENTÍFICAS
#    Para añadir una nueva, copia un bloque { ... } y rellena los campos.
#    'doi' se convierte automáticamente en enlace https://doi.org/...
# -----------------------------------------------------------------------------
PUBLICATIONS = [
    {
        "year": "2026",
        "title": "Above and belowground responses to prolonged drought: shrub "
                 "microsites accumulate soil nutrients while vegetation "
                 "greenness declines in semiarid ecosystems",
        "authors": "Henríquez-Gangas F., Carvallo G.O., <strong>Castro G.</strong>, "
                   "Díaz F.P.",
        "venue": "Journal of Arid Environments, 236, 105660",
        "doi": "10.1016/j.jaridenv.2026.105660",
    },
    {
        "year": "2025",
        "title": "Spatial inequality of urban greening dynamics in the Gran "
                 "Valparaíso during the Central Chile megadrought (2010–2023)",
        "authors": "De La Barra V., Chávez R.O., <strong>Castro G.</strong>, "
                   "Sarricolea P.",
        "venue": "Urban Forestry &amp; Urban Greening",
        "doi": "10.1016/j.ufug.2025.129080",
    },
    {
        "year": "2025",
        "title": "Hyper droughts in central Chile: drivers, impacts, and "
                 "projections",
        "authors": "Garreaud R., Boisier J.P., Alvarez-Garreton C., Christie D.A., "
                   "Carrasco-Escaff T., Vergara I., Chávez R.O., et al.",
        "venue": "Hydrology and Earth System Sciences (HESS)",
        "doi": "10.5194/hess-29-5347-2025",
    },
]

# -----------------------------------------------------------------------------
# 10. PRESENTACIONES EN CONGRESOS
# -----------------------------------------------------------------------------
CONFERENCES = [
    {
        "year": "2024",
        "title": "Evaluation of the effects of drought on vegetation in central "
                 "Chile using Landsat satellite images and high spatial "
                 "resolution multispectral images",
        "event": "XXX Annual Meeting of the Ecological Society of Chile, "
                 "La Serena — poster.",
    },
    {
        "year": "2023",
        "title": "Decadal changes in land use in six basins of central Chile "
                 "between 2000 and 2020 using Landsat images",
        "event": "SICyR International Symposium, Viña del Mar — poster.",
    },
    {
        "year": "2022",
        "title": "Spatio-temporal evaluation of irrigation patterns in "
                 "agricultural areas of the Petorca river basin from MODIS EVI "
                 "images and hydro-climate records",
        "event": "LXV Annual Meeting of the Society of Biology of Chile, "
                 "Pucón — poster.",
    },
]

# -----------------------------------------------------------------------------
# 11. CONTACTO Y ENLACES
#     Pon "" en cualquier enlace que no quieras mostrar y desaparecerá.
# -----------------------------------------------------------------------------
CONTACT = {
    "heading": "Let's connect",
    "blurb": "Open to collaborations in remote sensing, geospatial machine "
             "learning and earth observation. Feel free to reach out.",
    "email_primary": "gabriel.castro@wur.nl",
    "email_secondary": "gabriel.castro.b@pucv.cl",
    "phone": "+31 6 26236610",
    "location": "Wageningen, Netherlands",
    "links": {
        "github": "https://github.com/gabrielcastrob",
        "linkedin": "",          # ej: "https://linkedin.com/in/tu-perfil"
        "orcid": "",             # ej: "https://orcid.org/0000-0000-0000-0000"
        "google_scholar": "",    # ej: "https://scholar.google.com/citations?user=..."
        "researchgate": "",
    },
}

# -----------------------------------------------------------------------------
# 12. PIE DE PÁGINA
# -----------------------------------------------------------------------------
FOOTER = {
    "text": "Built with Python &amp; Leaflet · © 2026 Gabriel Castro B.",
}
