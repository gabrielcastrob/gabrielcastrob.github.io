# Carpeta de visualizaciones reales

Aquí subirás tus productos reales (mapas, figuras, modelos, mapas web exportados, etc.).

## Cómo conectar una visualización al sitio

### Opción A — Imagen estática (PNG/JPG)
1. Copia tu imagen aquí, por ejemplo: `visualizations/ndvi_anomaly.png`
2. Abre `content.py`, sección **8. VISUALIZACIONES**, y en `gallery` pon:
   ```python
   "src": "visualizations/ndvi_anomaly.png",
   ```
3. Ejecuta `python build.py`.

### Opción B — Mapa interactivo de Leaflet (capa GeoJSON real)
1. Exporta tu capa a GeoJSON y guárdala en `assets/data/` con el mismo nombre
   que usa un paso del mapa (p. ej. `study_basins.geojson`), **o** cambia el
   campo `"layer"` del paso en `content.py` (sección 7) por el nombre de tu archivo.
2. Ejecuta `python build.py`.

### Opción C — Mapa o dashboard HTML completo (p. ej. exportado de Folium/Kepler)
1. Copia el `.html` aquí, por ejemplo `visualizations/mapa_drought.html`.
2. Enlázalo desde la galería editando `content.py` (`"src"`), o pídeme que lo
   incruste como `<iframe>` en una sección.

> Los archivos de demostración actuales en `assets/data/*.geojson` son **ficticios**
> y puedes borrarlos o sobrescribirlos cuando tengas los reales.
