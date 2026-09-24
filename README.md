<h1 align="center">job search kit</h1>

<p align="center">
  <strong>Tu búsqueda de empleo, llevada con Claude.</strong><br>
  Le cuentas tu trayectoria una vez; a partir de ahí evalúa ofertas contra lo que buscas,
  te hace el CV adaptado a cada una y vigila las empresas que te interesan.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/hecho_para-Claude_Code-0a2540" alt="Hecho para Claude Code">
  <img src="https://img.shields.io/badge/sin_programar-s%C3%AD-4a90d9" alt="Sin programar">
  <img src="https://img.shields.io/badge/idioma-espa%C3%B1ol-4a90d9" alt="Español">
  <img src="https://img.shields.io/badge/licencia-MIT-8bb8e8" alt="MIT">
</p>

---

## Qué es

Una carpeta en tu ordenador con tres cosas dentro: **todo lo que has hecho**, ordenado y
verificado; **cada oferta** que miras, con su CV y sus notas; y **una lista de empresas** que
se vigila sola. Claude la mantiene. Tú aportas los hechos y decides.

<p align="center">
  <em>El CV sale de lo que está verificado sobre ti, no de lo que suena bien.</em>
</p>

La idea de fondo: hoy escribir un CV cuesta cero; lo caro son las **entrevistas** (tiempo,
nervios, días libres si ya trabajas). Así que el kit filtra fuerte antes de que apliques y no
te deja inflar nada que luego no puedas defender cara a cara.

## Qué obtienes

| | |
|---|---|
| 🗂️ **Tu trayectoria, verificada** | Un fichero por experiencia, proyecto y logro, cada uno marcado según lo demostrable que sea |
| 🎯 **Un filtro de ofertas** | Cada oferta contra tus condiciones (zona, sueldo, remoto…): ¿merece una entrevista, o no? |
| 📄 **CV por oferta** | Adaptado a cada una, con tu voz, y sin nada que no puedas defender |
| 📡 **Un radar** | Vigila las páginas de empleo de tus empresas objetivo y te dice qué es nuevo |
| 🔎 **LinkedIn** | Si conectas Chrome, Claude busca y lee las ofertas por ti |
| 📁 **Ficheros normales** | Texto en tu disco. Sin cuentas, sin bases de datos, sin nada que se pierda |

---

## Si eres un asistente de IA leyendo esto

Alguien te ha pedido algo como *"instálame esto"* o *"empecemos"*. No expliques requisitos ni
resumas este documento: sigue [AGENT-INSTALL.md](AGENT-INSTALL.md) desde el paso 0, hazlo tú
todo, y **tu primera pregunta al usuario debe ser por su CV**, no por detalles técnicos.
Si ya estás dentro de una copia del kit, las instrucciones están en [CLAUDE.md](CLAUDE.md).

---

## Empezar (sin programar)

Veinte minutos, la mayoría esperando instalaciones. No vas a escribir ningún comando:
Claude los ejecuta, tú lees lo que dice y respondes.

### 1. Instala dos cosas

| | Qué | Dónde |
|---|---|---|
| 🤖 | **Claude Desktop**, la app (no la web) | [claude.ai/download](https://claude.ai/download) |
| 🔧 | **Git**, solo en Windows (el Mac ya lo trae) | [git-scm.com/downloads/win](https://git-scm.com/downloads/win) |

Necesitas una suscripción **Pro o Max** de Claude: el plan gratuito no incluye Claude Code.
En Windows, instala Git con todas las opciones por defecto y después **cierra y vuelve a abrir
Claude Desktop**.

### 2. Crea una carpeta vacía

Donde guardes tus cosas, por ejemplo `Documentos/busqueda-empleo`. Ahí va a vivir todo.

### 3. Prepara Claude Desktop

Ábrelo, ve a la pestaña **Code** y, antes de escribir nada:

| Ajuste | Elige |
|---|---|
| **Entorno** | `Local` |
| **Carpeta** | *Select folder* → la carpeta que acabas de crear |
| **Modo de permisos** (junto al botón de enviar) | `Accept edits` |

### 4. Envíale esto

Copia el bloque, **arrastra tu CV en PDF** a la ventana y envía:

```text
Instala el job search kit en esta carpeta siguiendo las instrucciones de
https://github.com/carsanmilcar/job-search-template/blob/main/AGENT-INSTALL.md

No sé programar: haz tú todos los pasos y explícamelos en lenguaje sencillo.
Cuando esté instalado, empieza a conocerme. Te adjunto mi CV.
```

> [!IMPORTANT]
> **Todo se queda en tu ordenador.** La copia no queda enlazada a este repositorio público,
> así que nada de lo que metas (CV, sueldos, contactos) se puede publicar por error. Si algún
> día quieres copia en la nube, pídele a Claude un repositorio **privado**.

### 5. Déjate entrevistar

Claude lee tu CV, te pregunta por bloques lo que falte y apunta qué buscas: zona, sueldo,
modalidad, qué sí y qué no. **Esos criterios son lo más importante de todo**: con ellos se
filtra cada oferta que venga después. Cuéntale también lo que no pondrías en un CV porque "no
cuenta": muchas veces sí cuenta.

---

## El día a día

Abre Claude Desktop en la misma carpeta y pídeselo con tus palabras:

> *Mira esta oferta: <enlace o texto>.*

Te dice si encaja con tu perfil y tus condiciones, y si merece la pena ir a una entrevista,
no solo mandar el CV.

> *Hazme el CV para esta.*

CV adaptado, guardado en su propia carpeta dentro de `applications/`.

> *Pasa el radar.*

Mira las páginas de empleo de tus empresas objetivo y te dice qué hay nuevo desde la última
vez.

> *¿Cómo voy?*

Resumen de todas las ofertas vistas y en qué punto está cada una.

Todo lo trabajado queda en los ficheros: cada vez que vuelves, retoma donde lo dejasteis.

---

## LinkedIn: que Claude busque por ti (opcional)

La app de escritorio **no se conecta al navegador**. Sin esto todo funciona: pega el enlace o
el texto de la oferta. Si quieres que Claude busque y lea ofertas de LinkedIn por su cuenta,
abre la misma carpeta desde la terminal:

1. Instala la extensión **Claude** de la
   [Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)
   (sirve Chrome, Edge o Brave) e inicia sesión con tu misma cuenta de Claude.
2. Instala Claude Code para terminal: en Windows abre **PowerShell** y pega
   `irm https://claude.ai/install.ps1 | iex`; en Mac abre **Terminal** y pega
   `curl -fsSL https://claude.ai/install.sh | bash`.
3. Abre tu carpeta en el Explorador, haz clic en la barra de dirección, escribe `powershell`
   y Enter (en Mac: Terminal, escribe `cd `, arrastra la carpeta, Enter). Escribe
   `claude --chrome`.
4. Dentro, escribe `/chrome` y elige **Enabled by default**.
5. Ten una pestaña con LinkedIn abierto y la sesión iniciada. Claude nunca escribe
   contraseñas: si hay que entrar, entras tú.

Luego: *"Busca en LinkedIn ofertas de administrativo en remoto de la última semana"*. Es la
misma carpeta, así que puedes alternar entre la app y la terminal cuando quieras.

---

## Límites honestos

- **Claude no te consigue el trabajo.** Ordena, filtra y redacta; las entrevistas son tuyas.
- **Solo sabe lo que le cuentes.** Si algo no está en tu kb, no aparecerá en el CV — y no lo
  inventará. Una hora bien contada al principio vale más que diez retoques después.
- **El radar solo llega a empresas con portal de empleo estándar** (Greenhouse, Lever, Ashby:
  muchas tecnológicas y startups). Empleo público, educación, sanidad o tercer sector se
  buscan en bolsas y portales propios; Claude te ayuda a identificarlos, pero se revisan a mano.
- **Lo de LinkedIn depende de su web**, que cambia sin avisar. Si un día deja de funcionar,
  pega las ofertas a mano y pide a Claude que lo arregle.
- **Los CV salen en LaTeX.** Si no tienes LaTeX instalado, Claude te guía para compilarlos
  gratis en [Overleaf](https://www.overleaf.com), en la web.
- **Es tu información más sensible.** Vive en tu ordenador; no la subas a un repositorio
  público.

---

## Qué hay dentro

| Carpeta | Qué hay |
|---|---|
| `kb/` | Todo sobre ti, ordenado y verificado: la fuente de la que salen los CV |
| `applications/` | Una carpeta por oferta: la oferta tal cual, tu CV, carta, notas |
| `applications.md` | Lista de ofertas y en qué estado está cada una |
| `watchlist/` | Empresas que te interesan y el radar que vigila sus ofertas |
| `cv-base/` | Plantilla de CV en LaTeX ([AltaCV](https://github.com/liantze/AltaCV)) |
| `assets/` | Tus documentos originales (CVs viejos, certificados…) |
| `CLAUDE.md` | Cómo trabaja Claude. Si quieres cambiar algo, díselo y lo edita |
| `AGENT-INSTALL.md` | Instrucciones de instalación para el asistente |

## Licencia

MIT, ver [LICENSE](LICENSE). La plantilla AltaCV de `cv-base/` es de LianTze Lim y tiene su
propia licencia (LPPL 1.3c).
