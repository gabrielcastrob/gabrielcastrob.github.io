/* ==========================================================================
   main.js · Lógica interactiva del portafolio
   --------------------------------------------------------------------------
   Contiene 5 bloques independientes y bien separados:
     1) Navbar (scroll + menú móvil)
     2) Animaciones de aparición (IntersectionObserver)
     3) Fondo animado del hero (canvas: red de puntos)
     4) Scrollytelling de mapa (Leaflet)
     5) Gráficos interactivos (Plotly)  — DATOS DEMO, edítalos abajo.
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  initNavbar();
  initReveal();
  initHeroCanvas();
  initStoryMap();
  initCharts();
});

/* -------------------------------------------------------------------------
   1) NAVBAR
   ------------------------------------------------------------------------- */
function initNavbar() {
  const nav = document.getElementById("nav");
  const toggle = document.querySelector(".nav__toggle");
  const links = document.querySelector(".nav__links");

  window.addEventListener("scroll", () => {
    nav.classList.toggle("scrolled", window.scrollY > 40);
  });

  if (toggle) {
    toggle.addEventListener("click", () => links.classList.toggle("open"));
    links.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => links.classList.remove("open"))
    );
  }
}

/* -------------------------------------------------------------------------
   2) ANIMACIONES DE APARICIÓN
   ------------------------------------------------------------------------- */
function initReveal() {
  const obs = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) {
          e.target.classList.add("is-visible");
          obs.unobserve(e.target);
        }
      });
    },
    { threshold: 0.15 }
  );
  document.querySelectorAll(".reveal").forEach((el) => obs.observe(el));
}

/* -------------------------------------------------------------------------
   3) FONDO ANIMADO DEL HERO (red de puntos tipo "constelación de datos")
   ------------------------------------------------------------------------- */
function initHeroCanvas() {
  const canvas = document.getElementById("hero-canvas");
  if (!canvas) return;
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  const ctx = canvas.getContext("2d");
  let w, h, pts;

  function resize() {
    w = canvas.width = canvas.offsetWidth;
    h = canvas.height = canvas.offsetHeight;
    const count = Math.min(90, Math.floor((w * h) / 16000));
    pts = Array.from({ length: count }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4,
    }));
  }

  function frame() {
    ctx.clearRect(0, 0, w, h);
    for (let i = 0; i < pts.length; i++) {
      const p = pts[i];
      p.x += p.vx; p.y += p.vy;
      if (p.x < 0 || p.x > w) p.vx *= -1;
      if (p.y < 0 || p.y > h) p.vy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, 1.6, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(56,225,196,0.7)";
      ctx.fill();

      for (let j = i + 1; j < pts.length; j++) {
        const q = pts[j];
        const d = Math.hypot(p.x - q.x, p.y - q.y);
        if (d < 130) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = `rgba(59,158,255,${0.12 * (1 - d / 130)})`;
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(frame);
  }

  resize();
  window.addEventListener("resize", resize);
  frame();
}

/* -------------------------------------------------------------------------
   4) SCROLLYTELLING DE MAPA (Leaflet)
   --------------------------------------------------------------------------
   Lee los "steps" inyectados desde content.py (vía build.py) y, al hacer
   scroll, vuela a cada ubicación y carga su capa GeoJSON desde assets/data/.
   ------------------------------------------------------------------------- */
function initStoryMap() {
  const mapEl = document.getElementById("story-map");
  if (!mapEl || typeof L === "undefined") return;

  const steps = JSON.parse(
    document.getElementById("map-story-data").textContent || "[]"
  );
  if (!steps.length) return;

  const map = L.map("story-map", {
    zoomControl: true,
    scrollWheelZoom: false,
    attributionControl: true,
  }).setView(steps[0].center, steps[0].zoom);

  // Mapa base oscuro (CARTO Dark Matter)
  L.tileLayer(
    "https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png",
    {
      attribution:
        '&copy; <a href="https://openstreetmap.org">OpenStreetMap</a> &copy; <a href="https://carto.com/attributions">CARTO</a>',
      maxZoom: 19,
    }
  ).addTo(map);

  // Estilo de las capas GeoJSON
  const layerStyle = {
    color: "#38e1c4",
    weight: 2,
    fillColor: "#3b9eff",
    fillOpacity: 0.18,
  };

  // Cargamos cada capa una sola vez y la guardamos en caché.
  const layerCache = {};
  let activeLayer = null;

  function showLayer(name) {
    if (activeLayer) { map.removeLayer(activeLayer); activeLayer = null; }
    if (!name) return;

    if (layerCache[name]) {
      activeLayer = layerCache[name].addTo(map);
      return;
    }
    fetch(`assets/data/${name}.geojson`)
      .then((r) => (r.ok ? r.json() : null))
      .then((geo) => {
        if (!geo) return;
        const lyr = L.geoJSON(geo, {
          style: layerStyle,
          pointToLayer: (f, latlng) =>
            L.circleMarker(latlng, {
              radius: 7,
              color: "#38e1c4",
              fillColor: "#38e1c4",
              fillOpacity: 0.9,
            }),
          onEachFeature: (f, l) => {
            if (f.properties && f.properties.name) {
              l.bindPopup(`<strong>${f.properties.name}</strong>`);
            }
          },
        });
        layerCache[name] = lyr;
        activeLayer = lyr.addTo(map);
      })
      .catch(() => {});
  }

  // Observamos los paneles de texto para activar cada paso al centrarse.
  let current = -1;
  function activate(i) {
    if (i === current) return;
    current = i;
    const s = steps[i];
    map.flyTo(s.center, s.zoom, { duration: 1.4 });
    showLayer(s.layer);

    document.querySelectorAll(".story-step").forEach((el, idx) =>
      el.classList.toggle("is-active", idx === i)
    );
  }

  const stepEls = document.querySelectorAll(".story-step");
  const obs = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) activate(Number(e.target.dataset.index));
      });
    },
    { threshold: 0.6 }
  );
  stepEls.forEach((el) => obs.observe(el));

  // Estado inicial
  activate(0);
}

/* -------------------------------------------------------------------------
   5) GRÁFICOS INTERACTIVOS (Plotly)
   --------------------------------------------------------------------------
   *** DATOS DEMO ***  Cambia los arrays de abajo por tus datos reales.
   ------------------------------------------------------------------------- */
function initCharts() {
  if (typeof Plotly === "undefined") return;

  const FONT = { family: "Inter, sans-serif", color: "#93a3bb" };
  const baseLayout = {
    paper_bgcolor: "rgba(0,0,0,0)",
    plot_bgcolor: "rgba(0,0,0,0)",
    font: FONT,
    margin: { l: 48, r: 18, t: 10, b: 40 },
    xaxis: { gridcolor: "#243349", zerolinecolor: "#243349" },
    yaxis: { gridcolor: "#243349", zerolinecolor: "#243349" },
    legend: { orientation: "h", y: -0.25 },
  };
  const config = { displayModeBar: false, responsive: true };

  /* --- Gráfico 1: serie temporal de NDVI (demo) --- */
  const years = [2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024];
  const ndviWet = [0.62, 0.6, 0.58, 0.55, 0.53, 0.5, 0.48, 0.47];
  const ndviDry = [0.48, 0.45, 0.42, 0.38, 0.35, 0.31, 0.29, 0.27];

  const ndviEl = document.getElementById("chart-ndvi");
  if (ndviEl) {
    Plotly.newPlot(
      ndviEl,
      [
        { x: years, y: ndviWet, name: "Riparian", mode: "lines+markers",
          line: { color: "#38e1c4", width: 3 } },
        { x: years, y: ndviDry, name: "Hillslope", mode: "lines+markers",
          line: { color: "#ffb454", width: 3 } },
      ],
      { ...baseLayout, yaxis: { ...baseLayout.yaxis, title: "NDVI", range: [0.2, 0.7] } },
      config
    );
  }

  /* --- Gráfico 2: cambio de cobertura del suelo 2000 → 2020 (demo) --- */
  const classes = ["Native forest", "Shrubland", "Cropland", "Urban", "Bare soil"];
  const y2000 = [28, 34, 20, 8, 10];
  const y2020 = [22, 29, 17, 18, 14];

  const lulcEl = document.getElementById("chart-lulc");
  if (lulcEl) {
    Plotly.newPlot(
      lulcEl,
      [
        { x: classes, y: y2000, name: "2000", type: "bar", marker: { color: "#3b9eff" } },
        { x: classes, y: y2020, name: "2020", type: "bar", marker: { color: "#38e1c4" } },
      ],
      { ...baseLayout, barmode: "group", yaxis: { ...baseLayout.yaxis, title: "% of basin area" } },
      config
    );
  }
}
