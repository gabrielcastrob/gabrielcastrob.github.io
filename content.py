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
    # URL final del sitio (GitHub Pages, repo de proyecto):
    "url": "https://gabrielcastrob.github.io/MGI_PortafolioVis/",
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
# 7. SECCIÓN "WORK" — SCROLLYTELLING DE MAPA
# -----------------------------------------------------------------------------
#  Es un mapa interactivo (base FÍSICA de Esri) que ocupa la pantalla y, al hacer
#  scroll, VUELA a la ubicación de cada proyecto y despliega sus FIGURAS sobre el
#  mapa. Reúne los 3 tipos de trabajo en un solo recorrido.
#
#  Cada paso ("step"):
#     group    -> "papers" | "field" | "wageningen"  (color del marcador/etiqueta)
#     tag      -> etiqueta corta (revista/año, curso, tipo de trabajo...)
#     title    -> título del proyecto
#     center   -> [lat, lon] a donde vuela el mapa
#     zoom     -> nivel de zoom (mayor = más cerca)
#     images   -> lista de figuras O VIDEOS que se despliegan sobre el mapa.
#                 - Imágenes: .png .jpg .jpeg .gif .webp  (se muestran y son clicables)
#                 - Videos:   .mp4 .webm .ogg  (se muestran con reproductor integrado)
#                 Guarda los videos en assets/img/video/ (o donde prefieras) y pon
#                 aquí su ruta, p. ej. "assets/img/video/dron_terreno.mp4".
#                 Deja [] si aún no tienes nada; aparecerá un marcador de posición.
#     summary  -> resumen breve
#     results  -> resultado/hallazgo principal
#     doi      -> (opcional) DOI; se convierte en enlace
#
#  Para añadir un proyecto: copia un bloque { ... } y rellénalo.
#  Para cambiar el mapa base, edita la URL del tileLayer en assets/js/main.js.
# -----------------------------------------------------------------------------
WORK = {
    "heading": "Work &amp; field",
    "intro": "Scroll to travel across the sites behind my work — peer-reviewed "
             "research in Chile, UAV field campaigns, and MSc projects at "
             "Wageningen. Each stop reveals its figures over the map.",

    # Vista inicial del mapa (antes de empezar a hacer scroll):
    "map": {"center": [-20.0, -25.0], "zoom": 3},

    "steps": [
        # ======================= PAPERS (Chile) =======================
        {
            "group": "papers",
            "tag": "Journal of Arid Environments · 2026",
            "title": "Shrub microsites &amp; prolonged drought in semiarid "
                     "ecosystems",
            "center": [-32.50, -71.00],
            "zoom": 7,
            "images": ["assets/img/papers/aridenv_drought.png"],
            "summary": "Vegetation greenness (NDVI), shrub cover and annual "
                       "precipitation across three semiarid sites (Papudo, Lampa, "
                       "Rapel) compared between the pre-megadrought (2000–2009) "
                       "and megadrought (2010–2023) periods.",
            "results": "Greenness and shrub cover declined significantly under the "
                       "megadrought, yet soil nutrients accumulated within shrub "
                       "microsites — a decoupling of above- and below-ground "
                       "responses.",
            "doi": "10.1016/j.jaridenv.2026.105660",
        },
        {
            "group": "papers",
            "tag": "Urban Forestry &amp; Urban Greening · 2025",
            "title": "Spatial inequality of urban greening in the Gran Valparaíso",
            "center": [-33.05, -71.45],
            "zoom": 9,
            "images": [
                "assets/img/papers/greening_studyarea.png",
                "assets/img/papers/greening_anomaly.png",
                "assets/img/papers/greening_timeseries.png",
            ],
            "summary": "Mapping of public, peri-urban and urban green areas across "
                       "the Gran Valparaíso conurbation and their NDVI anomalies "
                       "before and during the Central Chile megadrought.",
            "results": "Urban greening loss was spatially unequal: peri-urban and "
                       "public green spaces deteriorated most, exposing "
                       "environmental inequality between neighbourhoods.",
            "doi": "10.1016/j.ufug.2025.129080",
        },
        {
            "group": "papers",
            "tag": "Hydrology &amp; Earth System Sciences · 2025",
            "title": "Hyper-droughts in central Chile: drivers, impacts &amp; "
                     "projections",
            "center": [-34.50, -70.80],
            "zoom": 6,
            "images": [
                "assets/img/papers/hyperdrought_sst.png",
                "assets/img/papers/hyperdrought_hydro.png",
                "assets/img/papers/hyperdrought_ndvi.png",
            ],
            "summary": "Central Chile's hyper-droughts linked to ocean–atmosphere "
                       "drivers (SST &amp; sea-level pressure), and their effects "
                       "on precipitation, river discharge, snowpack and vegetation "
                       "(Landsat NDVI) over more than a century.",
            "results": "Recent droughts are unprecedented in the instrumental "
                       "record, with compounding deficits in rainfall, streamflow "
                       "and snow water equivalent, and lasting vegetation impacts.",
            "doi": "10.5194/hess-29-5347-2025",
        },

        # ======================= FIELD WORK =======================
        {
            "group": "field",
            "tag": "Fieldwork · Aysén, Chile",
            "title": "Patagonia field campaign",
            "center": [-46.50, -72.30],
            "zoom": 7,
            "images": [
                "assets/img/field/patagonia_bosque1.jpg",
                "assets/img/field/patagonia_bosque2.jpg",
                "assets/img/video/patagonia_dron.mp4",
            ],
            "summary": "Ground data collection and landscape survey in the native "
                       "forests of Chilean Patagonia (Aysén), combining field "
                       "photography with UAV aerial footage of the canopy.",
            "results": "Documented forest structure and condition on the ground, "
                       "with drone imagery providing a complementary low-altitude "
                       "view to link field observations with remote sensing.",
            "doi": "",
        },

        # ===================== WAGENINGEN (MGI) =====================
        # Orden: Advanced Earth Observation -> Machine Learning ->
        #        Deep Learning -> Extended Realities
        {
            "group": "wageningen",
            "tag": "GRS32306 · Advanced Earth Observation",
            "title": "Advanced Earth Observation",
            "center": [51.985, 5.665],
            "zoom": 8,
            "images": [
                "assets/img/wageningen/aeo_paper.png",
            ],
            "summary": "Scientific-paper-style project analysing land-surface "
                       "dynamics from dense multi-sensor satellite time series. "
                       "The work combined optical observations to detect and "
                       "characterise vegetation change, framed and written up as a "
                       "short research article.",
            "results": "Produced a reproducible time-series workflow and a "
                       "paper-format figure summarising the observed land-surface "
                       "trends.",
            "doi": "",
        },
        {
            "group": "wageningen",
            "tag": "FTE35306 · Machine Learning",
            "title": "Machine Learning — classification challenge",
            "center": [51.985, 5.665],
            "zoom": 8,
            "images": [
                "assets/img/wageningen/ml_map.png",
                "assets/img/wageningen/ml_charts.png",
            ],
            "summary": "Supervised land-cover classification challenge (with "
                       "N. Groenhart): feature engineering on a remote sensing "
                       "dataset, comparison of several classifiers, and "
                       "hyper-parameter tuning with cross-validation to maximise "
                       "predictive performance.",
            "results": "Delivered a tuned classification pipeline; the resulting "
                       "thematic map and accuracy/feature-importance charts are "
                       "shown above.",
            "doi": "",
        },
        {
            "group": "wageningen",
            "tag": "AIN31306 · Deep Learning",
            "title": "Deep Learning — group project",
            "center": [51.985, 5.665],
            "zoom": 8,
            "images": [
                "assets/img/wageningen/dl_detection.png",
                "assets/img/wageningen/dl_plot.png",
            ],
            "summary": "Group project (with Abel) applying deep neural networks "
                       "to aerial imagery: building, training and evaluating a "
                       "convolutional model for object detection / segmentation, "
                       "including data preparation and monitoring of the training "
                       "process.",
            "results": "Trained and evaluated the model end-to-end; detection "
                       "outputs and the training/validation curves are shown above.",
            "doi": "",
        },
        {
            "group": "wageningen",
            "tag": "MSc course · Extended Realities",
            "title": "Extended Realities — the future of communication",
            "center": [51.985, 5.665],
            "zoom": 8,
            "images": [
                "assets/img/wageningen/xr_unity.png",
            ],
            "summary": "Group project building an immersive 3D geovisualization in "
                       "Unity: a LiDAR point-cloud scene set up for interactive, "
                       "first-person exploration, exploring augmented and virtual "
                       "reality as the future of spatial communication.",
            "results": "Delivered an interactive Unity application; the editor view "
                       "of the LiDAR environment is shown above.",
            "doi": "",
        },
    ],
}

# -----------------------------------------------------------------------------
# 8. CONTACTO Y ENLACES
#    Pon "" en cualquier enlace que no quieras mostrar y desaparecerá.
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
# 9. PIE DE PÁGINA
# -----------------------------------------------------------------------------
FOOTER = {
    "text": "Built with Python &amp; Leaflet · © 2026 Gabriel Castro B.",
}
