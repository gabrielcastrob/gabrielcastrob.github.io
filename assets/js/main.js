/* ==========================================================================
   main.js · Lógica interactiva del portafolio (tema claro)
   --------------------------------------------------------------------------
   Bloques independientes:
     1) Navbar (scroll + menú móvil)
     2) Animaciones de aparición (IntersectionObserver)
     3) Fondo animado del hero (canvas: red de puntos)
     4) Scrollytelling de mapa (Leaflet + base FÍSICA de Esri)
   ========================================================================== */

document.addEventListener("DOMContentLoaded", () => {
  initNavbar();
  initReveal();
  initHeroCanvas();
  initWorkMap();
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
   4) SCROLLYTELLING DE MAPA (Leaflet + base FÍSICA de Esri)
   --------------------------------------------------------------------------
   El mapa permanece fijo y, al hacer scroll, VUELA a la ubicación de cada
   proyecto (leída de los atributos data-* de cada .story-step) mientras la
   tarjeta con sus figuras se despliega encima.
   Usa "Esri World Physical Map" (relieve físico, NO satélite).
   Para cambiar el mapa base, edita la URL del tileLayer de abajo.
   ------------------------------------------------------------------------- */
function initWorkMap() {
  const mapEl = document.getElementById("work-map");
  if (!mapEl || typeof L === "undefined") return;

  const init = JSON.parse(
    document.getElementById("work-map-data").textContent || "{}"
  );

  const map = L.map("work-map", {
    center: init.center || [0, 0],
    zoom: init.zoom || 3,
    scrollWheelZoom: false,
    zoomControl: true,
    attributionControl: true,
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

  // Colores por grupo (papers / field / wageningen)
  const groupColor = {
    papers: "#0d9488",
    field: "#d97706",
    wageningen: "#2563eb",
  };

  // Construye la lista de pasos desde el DOM (atributos data-*)
  const stepEls = Array.from(document.querySelectorAll(".story-step"));
  const markers = [];

  stepEls.forEach((el) => {
    const lat = parseFloat(el.dataset.lat);
    const lon = parseFloat(el.dataset.lon);
    const group = el.dataset.group || "papers";
    const color = groupColor[group] || "#0d9488";
    const title = el.querySelector("h3")?.textContent || "";

    const marker = L.circleMarker([lat, lon], {
      radius: 7,
      color: "#ffffff",
      weight: 2,
      fillColor: color,
      fillOpacity: 0.9,
    })
      .addTo(map)
      .bindPopup(`<strong>${title}</strong>`);
    markers.push(marker);
  });

  // Activa un paso: vuela el mapa, resalta su marcador y su tarjeta
  let current = -1;
  function activate(i) {
    if (i === current || !stepEls[i]) return;
    current = i;
    const el = stepEls[i];
    map.flyTo([parseFloat(el.dataset.lat), parseFloat(el.dataset.lon)],
              parseInt(el.dataset.zoom, 10) || 7, { duration: 1.4 });

    stepEls.forEach((s, idx) => s.classList.toggle("is-active", idx === i));
    markers.forEach((m, idx) =>
      m.setStyle({ radius: idx === i ? 11 : 7, fillOpacity: idx === i ? 1 : 0.75 })
    );
  }

  // Observa cuál panel está centrado en pantalla
  const obs = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) activate(Number(e.target.dataset.index));
      });
    },
    { threshold: 0.6 }
  );
  stepEls.forEach((el) => obs.observe(el));

  setTimeout(() => map.invalidateSize(), 300);
  activate(0);
}
