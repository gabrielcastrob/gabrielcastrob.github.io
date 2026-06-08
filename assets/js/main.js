/* ==========================================================================
   main.js · Lógica interactiva del portafolio (tema claro)
   --------------------------------------------------------------------------
   Bloques independientes:
     1) Navbar (scroll + menú móvil)
     2) Animaciones de aparición (IntersectionObserver)
     3) Fondo animado del hero (canvas: red de puntos)
     4) Mapa de trabajos (Leaflet + base FÍSICA de Esri)
     5) Pestañas de la sección Work (Papers / Field / Wageningen)
     6) Gráficos interactivos (Plotly)  — DATOS DEMO, edítalos abajo.
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  initNavbar();
  initReveal();
  initHeroCanvas();
  initWorkMap();
  initTabs();
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
    { threshold: 0.12 }
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
    const count = Math.min(80, Math.floor((w * h) / 18000));
    pts = Array.from({ length: count }, () => ({
      x: Math.random() * w,
      y: Math.random() * h,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
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
      ctx.arc(p.x, p.y, 1.7, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(13,148,136,0.55)";   // teal
      ctx.fill();

      for (let j = i + 1; j < pts.length; j++) {
        const q = pts[j];
        const d = Math.hypot(p.x - q.x, p.y - q.y);
        if (d < 130) {
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = `rgba(37,99,235,${0.10 * (1 - d / 130)})`; // azul
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
   4) MAPA DE TRABAJOS (Leaflet + base FÍSICA de Esri)
   --------------------------------------------------------------------------
   Lee el objeto 'map' inyectado desde content.py (center, zoom, markers).
   Usa "Esri World Physical Map" (relieve físico, NO satélite).
   Para cambiar el mapa base, edita la URL de tileLayer más abajo.
   ------------------------------------------------------------------------- */
function initWorkMap() {
  const mapEl = document.getElementById("work-map");
  if (!mapEl || typeof L === "undefined") return;

  const data = JSON.parse(
    document.getElementById("work-map-data").textContent || "{}"
  );
  if (!data.center) return;

  const map = L.map("work-map", {
    center: data.center,
    zoom: data.zoom || 3,
    scrollWheelZoom: false,
    zoomControl: true,
  });

  // ---- Base física de Esri (relieve) ----
  L.tileLayer(
    "https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}",
    {
      attribution: "Tiles &copy; Esri — Source: US National Park Service",
      maxZoom: 13,
      maxNativeZoom: 8,   // el servicio físico llega a z8; Leaflet sobre-amplía
    }
  ).addTo(map);

  // Colores de marcador por grupo (papers / field / wageningen)
  const groupColor = {
    papers: "#0d9488",
    field: "#d97706",
    wageningen: "#2563eb",
  };

  // Marcadores
  (data.markers || []).forEach((m) => {
    const color = groupColor[m.group] || "#0d9488";
    L.circleMarker(m.coords, {
      radius: 8,
      color: "#ffffff",
      weight: 2,
      fillColor: color,
      fillOpacity: 0.95,
    })
      .addTo(map)
      .bindPopup(`<strong>${m.name}</strong>`);
  });

  // Reajusta tamaño cuando el contenedor se hace visible
  setTimeout(() => map.invalidateSize(), 300);
}

/* -------------------------------------------------------------------------
   5) PESTAÑAS DE LA SECCIÓN WORK
   ------------------------------------------------------------------------- */
function initTabs() {
  const btns = document.querySelectorAll(".tab-btn");
  const panels = document.querySelectorAll(".tab-panel");
  if (!btns.length) return;

  btns.forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.dataset.tab;
      btns.forEach((b) => b.classList.toggle("is-active", b === btn));
      panels.forEach((p) =>
        p.classList.toggle("is-active", p.id === "tab-" + id)
      );
    });
  });
}

/* -------------------------------------------------------------------------
   6) GRÁFICOS INTERACTIVOS (Plotly)
   --------------------------------------------------------------------------
   *** DATOS DEMO ***  Cambia los arrays de abajo por tus datos reales.
   ------------------------------------------------------------------------- */
function initCharts() {
  if (typeof Plotly === "undefined") return;

  const FONT = { family: "Inter, sans-serif", color: "#5b6b82" };
  const baseLayout = {
    paper_bgcolor: "rgba(0,0,0,0)",
    plot_bgcolor: "rgba(0,0,0,0)",
    font: FONT,
    margin: { l: 48, r: 18, t: 10, b: 40 },
    xaxis: { gridcolor: "#e2e8f0", zerolinecolor: "#e2e8f0" },
    yaxis: { gridcolor: "#e2e8f0", zerolinecolor: "#e2e8f0" },
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
          line: { color: "#0d9488", width: 3 } },
        { x: years, y: ndviDry, name: "Hillslope", mode: "lines+markers",
          line: { color: "#d97706", width: 3 } },
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
        { x: classes, y: y2000, name: "2000", type: "bar", marker: { color: "#2563eb" } },
        { x: classes, y: y2020, name: "2020", type: "bar", marker: { color: "#0d9488" } },
      ],
      { ...baseLayout, barmode: "group", yaxis: { ...baseLayout.yaxis, title: "% of basin area" } },
      config
    );
  }
}
