# Job search kit (para usar con Claude Code)

Una carpeta para llevar tu búsqueda de empleo con Claude: le cuentas tu trayectoria una vez,
la guarda ordenada y verificada, y a partir de ahí te evalúa ofertas, te hace el CV adaptado a
cada una y vigila las webs de empleo de las empresas que te interesan. Tú aportas los hechos y
decides; Claude hace el resto.

**No hace falta saber programar.** Solo hay que instalar un par de cosas la primera vez (unos
15 minutos) y luego se habla con Claude en español normal.

## Lo que necesitas

- Un ordenador con Windows o Mac.
- Una suscripción de pago a Claude (**Pro** o **Max**) en [claude.ai](https://claude.ai).
  El plan gratuito no incluye Claude Code.
- Google Chrome (u otro navegador basado en Chromium, como Edge o Brave) si quieres que
  Claude busque ofertas en LinkedIn por ti. Es opcional.

## Paso 1 — Instalar Claude Code (una sola vez)

**Windows**
1. Instala [Git for Windows](https://git-scm.com/downloads/win) con las opciones por defecto
   (siguiente, siguiente…). Claude lo usa para guardar versiones de tu trabajo.
2. Abre **PowerShell** (tecla Windows → escribe `powershell` → Enter), pega esto y pulsa Enter:
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```

**Mac**: abre **Terminal** (Cmd+Espacio → `terminal`), pega esto y pulsa Enter:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

Cierra la ventana cuando termine. La primera vez que abras Claude te pedirá que inicies sesión
con tu cuenta de claude.ai en el navegador.

## Paso 2 — Conseguir tu copia de esta carpeta

**Opción fácil (sin cuenta de GitHub):** botón verde **Code** → **Download ZIP** arriba en
esta página. Descomprímelo donde quieras (por ejemplo, en Documentos) y renombra la carpeta a
algo tuyo, como `busqueda-empleo`. Todo se queda en tu ordenador.

**Opción con GitHub (para tener copia en la nube):** botón **Use this template** → *Create a
new repository* → marca **Private**. ⚠️ Privado sí o sí: ahí vas a guardar tu CV, sueldos y
contactos. Después pídele a Claude que te la descargue al ordenador.

## Paso 3 — Abrir Claude dentro de la carpeta

**Windows:** abre la carpeta en el Explorador de archivos, haz clic en la barra de dirección
(donde pone la ruta), escribe `powershell` y pulsa Enter. Se abre una ventana ya situada en
la carpeta. Ahí escribe:
```
claude --chrome
```

**Mac:** abre Terminal, escribe `cd ` (con espacio), arrastra la carpeta a la ventana, pulsa
Enter y escribe `claude --chrome`.

(Si no vas a usar lo del navegador, basta con `claude`).

## Paso 4 — Empezar

Escribe algo como:

> Acabo de copiar este repo, empecemos.

Y ten a mano tu CV actual en PDF. Para pasárselo, arrastra el PDF a la ventana o cópialo a la
carpeta `assets/`. Claude te guía desde ahí: lee tu CV, te hace preguntas por bloques para
completar lo que falte, apunta qué buscas (zona, sueldo, remoto…) y decide contigo dónde
buscar.

**Sobre los permisos:** Claude te irá pidiendo permiso antes de crear ficheros o ejecutar
cosas. Es normal: lee lo que propone y acepta. Si algo no lo entiendes, pregúntale "¿qué vas
a hacer con esto?".

## Conectar Claude con Chrome (opcional, para LinkedIn)

Sirve para que Claude busque y lea ofertas de LinkedIn en tu navegador. Sin esto todo lo demás
funciona igual: basta con pegarle el texto o el enlace de la oferta.

1. Instala la extensión **Claude** desde la
   [Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)
   e inicia sesión en ella con la misma cuenta de Claude.
2. Abre Claude con `claude --chrome` (Paso 3).
3. Dentro de Claude, escribe `/chrome`. Debe decir que está activado. Elige **Enabled by
   default** para no tener que poner `--chrome` cada vez.
4. Ten abierta una pestaña con tu sesión de LinkedIn iniciada. Claude nunca escribe tus
   contraseñas: si hay que iniciar sesión, lo haces tú.

Luego pídele, por ejemplo: *"Busca en LinkedIn ofertas de administrativo en remoto de la
última semana"*.

(Alternativa para gente técnica: el MCP
[Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp). La skill de
LinkedIn funciona con cualquiera de los dos).

## El día a día

- *"Mira esta oferta: <enlace o texto>"* → te dice si encaja con tu perfil y tus condiciones,
  y si merece la pena ir a una entrevista (no solo mandar el CV).
- *"Hazme el CV para esta"* → CV adaptado, guardado en su propia carpeta dentro de
  `applications/`.
- *"Busca en LinkedIn…"* → si has conectado Chrome.
- *"Pasa el radar"* → mira las páginas de empleo de tus empresas objetivo y te dice qué hay
  nuevo desde la última vez.
- *"¿Cómo voy?"* → resumen de las ofertas vistas y en qué punto está cada una.

Cada vez que vuelvas, abre Claude en la misma carpeta (Paso 3): lo que habéis trabajado está
guardado en los ficheros, así que retoma donde lo dejasteis.

## Si algo falla

- **"claude no se reconoce como comando"** → cierra la ventana y abre una nueva (tras
  instalar hace falta). Si sigue, repite el Paso 1.
- **No se genera el PDF del CV** → hace falta LaTeX. Pide a Claude que te lo explique: o
  instalas MiKTeX (Windows) / MacTeX (Mac), o subes la carpeta del CV a
  [Overleaf](https://www.overleaf.com) (gratis, en la web) y pulsas *Recompile*.
- **`/chrome` dice que la extensión no está conectada** → reinicia Chrome, comprueba que la
  extensión tiene la sesión iniciada con la misma cuenta y vuelve a abrir `claude --chrome`.
- **Cualquier otra cosa** → pregúntale a Claude directamente, en la misma ventana.

## Qué hay en la carpeta

| Carpeta | Qué hay |
|---|---|
| `kb/` | Todo sobre ti, ordenado y verificado: la fuente de la que salen los CV. |
| `cv-base/` | Plantilla de CV en LaTeX ([AltaCV](https://github.com/liantze/AltaCV)). |
| `applications/` | Una carpeta por oferta: la oferta tal cual, tu CV, carta, notas. |
| `applications.md` | Lista de ofertas y en qué estado está cada una. |
| `watchlist/` | Empresas que te interesan y el radar que vigila sus ofertas. |
| `assets/` | Tus documentos originales (CVs viejos, certificados…). |
| `CLAUDE.md` | Las instrucciones que sigue Claude. Si quieres cambiar cómo trabaja, díselo y lo edita. |
