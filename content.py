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
# 7. SECCIÓN "WORK" — trabajos divididos en 3 pestañas:
#       1) papers      -> figuras y resultados de tus publicaciones
#       2) field       -> trabajo de campo (dron, terreno Patagonia, etc.)
#       3) wageningen  -> proyectos de los cursos del máster MGI
#
#    Incluye un MAPA INTERACTIVO con base física de Esri (no satélite) que
#    muestra los sitios de trabajo. Edita 'map.markers' para añadir/mover puntos.
#
#    Cada item de las pestañas:
#       title    -> título del trabajo
#       tag      -> etiqueta corta (revista/año, tipo de trabajo, curso...)
#       images   -> lista de rutas a imágenes (se muestran en la tarjeta)
#       summary  -> resumen breve
#       results  -> resultado/hallazgo principal
#       doi      -> (opcional) DOI; se convierte en enlace
# -----------------------------------------------------------------------------
WORK = {
    "heading": "Work &amp; field",
    "intro": "From peer-reviewed research in Chilean drylands to UAV field "
             "campaigns and MSc projects at Wageningen. The map shows the main "
             "sites behind this work; switch tabs to explore each strand.",

    # --- Mapa con base física de Esri (World Physical Map) ---
    "map": {
        "center": [-20.0, -40.0],   # vista que abarca Chile y Europa
        "zoom": 3,
        "markers": [
            {"name": "Gran Valparaíso, Chile — urban greening study",
             "coords": [-33.05, -71.45], "group": "papers"},
            {"name": "Petorca / Papudo, Chile — drought & phenology",
             "coords": [-32.30, -71.00], "group": "papers"},
            {"name": "Central Chile — hyper-droughts",
             "coords": [-34.50, -70.80], "group": "papers"},
            {"name": "Chilean Patagonia — field campaign",
             "coords": [-46.50, -72.30], "group": "field"},
            {"name": "Wageningen, Netherlands — MSc Geo-information Science",
             "coords": [51.985, 5.665], "group": "wageningen"},
        ],
    },

    # --- Pestañas ---
    "tabs": [
        # ===================== 1) TRABAJOS DE PAPER =====================
        {
            "id": "papers",
            "label": "Paper work",
            "intro": "Selected figures and key results from my peer-reviewed "
                     "publications on drought, vegetation and land change in Chile.",
            "items": [
                {
                    "title": "Shrub microsites &amp; prolonged drought in "
                             "semiarid ecosystems",
                    "tag": "Journal of Arid Environments · 2026",
                    "images": ["assets/img/papers/aridenv_drought.png"],
                    "summary": "Comparison of vegetation greenness (NDVI), shrub "
                               "cover and annual precipitation across three "
                               "semiarid sites (Papudo, Lampa, Rapel) between the "
                               "pre-megadrought (2000–2009) and megadrought "
                               "(2010–2023) periods.",
                    "results": "Greenness and shrub cover declined significantly "
                               "under the megadrought, yet soil nutrients "
                               "accumulated within shrub microsites — revealing a "
                               "decoupling of above- and below-ground responses.",
                    "doi": "10.1016/j.jaridenv.2026.105660",
                },
                {
                    "title": "Spatial inequality of urban greening in the Gran "
                             "Valparaíso",
                    "tag": "Urban Forestry &amp; Urban Greening · 2025",
                    "images": [
                        "assets/img/papers/greening_studyarea.png",
                        "assets/img/papers/greening_anomaly.png",
                        "assets/img/papers/greening_timeseries.png",
                    ],
                    "summary": "Mapping of public, peri-urban and urban green "
                               "areas across the Gran Valparaíso conurbation and "
                               "their NDVI anomalies before and during the "
                               "Central Chile megadrought (2010–2023).",
                    "results": "Urban greening loss was spatially unequal: "
                               "peri-urban and public green spaces deteriorated "
                               "most, exposing environmental inequality between "
                               "neighbourhoods.",
                    "doi": "10.1016/j.ufug.2025.129080",
                },
                {
                    "title": "Hyper-droughts in central Chile: drivers, impacts "
                             "&amp; projections",
                    "tag": "Hydrology &amp; Earth System Sciences · 2025",
                    "images": [
                        "assets/img/papers/hyperdrought_sst.png",
                        "assets/img/papers/hyperdrought_hydro.png",
                        "assets/img/papers/hyperdrought_ndvi.png",
                    ],
                    "summary": "Characterisation of central Chile's hyper-droughts "
                               "linking ocean–atmosphere drivers (SST &amp; "
                               "sea-level pressure) to precipitation, river "
                               "discharge, snowpack and vegetation responses "
                               "(Landsat NDVI) over more than a century.",
                    "results": "Recent droughts are unprecedented in the "
                               "instrumental record, with compounding deficits in "
                               "rainfall, streamflow and snow water equivalent and "
                               "lasting impacts on natural and irrigated vegetation.",
                    "doi": "10.5194/hess-29-5347-2025",
                },
            ],
        },

        # ===================== 2) TRABAJO DE CAMPO =====================
        {
            "id": "field",
            "label": "Field work",
            "intro": "UAV surveys, ground-truthing and field campaigns — from "
                     "central Chile to Patagonia. (Upload your photos to "
                     "assets/img/field/ and link them below.)",
            "items": [
                {
                    "title": "UAV multispectral survey (demo)",
                    "tag": "Drone · DJI M300 RTK",
                    "images": [],   # ej: ["assets/img/field/drone_survey.jpg"]
                    "summary": "High-resolution multispectral flights to validate "
                               "satellite drought signals on the ground.",
                    "results": "Placeholder — add your photos and a short note "
                               "about the campaign.",
                    "doi": "",
                },
                {
                    "title": "Patagonia field campaign (demo)",
                    "tag": "Fieldwork · Aysén, Chile",
                    "images": [],   # ej: ["assets/img/field/patagonia.jpg"]
                    "summary": "Ground data collection and landscape survey in "
                               "Chilean Patagonia.",
                    "results": "Placeholder — add your photos and a short note "
                               "about the campaign.",
                    "doi": "",
                },
            ],
        },

        # ================= 3) PROYECTOS WAGENINGEN (MGI) =================
        {
            "id": "wageningen",
            "label": "Wageningen projects",
            "intro": "Products from my MSc Geo-information Science courses — "
                     "advanced earth observation, machine learning and deep "
                     "learning. (Add your course outputs to "
                     "assets/img/wageningen/.)",
            "items": [
                {
                    "title": "Deep learning for object detection (demo)",
                    "tag": "AIN31306 · Deep Learning",
                    "images": [],
                    "summary": "CNN / transformer models for detecting and "
                               "segmenting objects in aerial imagery.",
                    "results": "Placeholder — add your project figure and a short "
                               "description of the method and outcome.",
                    "doi": "",
                },
                {
                    "title": "Advanced earth observation (demo)",
                    "tag": "GRS32306 · Advanced Earth Observation",
                    "images": [],
                    "summary": "Point-cloud processing and time-series analysis of "
                               "multi-sensor satellite data.",
                    "results": "Placeholder — add your project figure and a short "
                               "description of the method and outcome.",
                    "doi": "",
                },
            ],
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
