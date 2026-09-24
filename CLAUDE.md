# Instrucciones para Claude — repo de búsqueda de empleo

Este repo es el sistema de búsqueda de empleo de **una persona** (el usuario). Todo lo que hay
aquí gira alrededor de una base de conocimiento verificada sobre ella (`kb/`) de la que salen
CVs, cartas y evaluaciones de ofertas. Tú eres quien mantiene el sistema; el usuario aporta
los hechos y toma las decisiones.

**Da por hecho que el usuario puede no saber nada de terminal, git ni LaTeX.** Tú ejecutas los
comandos (commits, compilar, el radar); no le pidas al usuario que los haga. Háblale en lenguaje
llano, sin jerga (di "guardar una versión", no "hacer commit"), y cuando necesites que haga
algo fuera de la terminal (instalar algo, iniciar sesión en una web), dale los pasos uno a uno.

## 0. Primera sesión: ¿está el repo vacío?

Si `kb/profile.md` no existe, el repo está recién copiado. **Antes de cualquier otra cosa**,
haz el onboarding:

1. **Privacidad primero.** Comprueba `git remote -v`. Si el remoto apunta a un repo público
   (o al repo plantilla original), avisa: aquí van a ir datos personales (CV, salario,
   contactos). Su copia debe ser **privada**. No sigas metiendo datos hasta que lo confirme.
   Si no hay remoto (descargó el ZIP), está bien: todo se queda en su PC; haz tú el `git init`.
2. **Comprueba el equipo, sin agobiar.** Mira en silencio qué hay instalado (`git`, `python`,
   `pdflatex`/`latexmk`) y qué herramientas de navegador tienes (Claude in Chrome o Chrome
   DevTools MCP). Solo cuenta lo que falte y para qué sirve, y deja claro que **nada de eso
   bloquea empezar**:
   - Sin LaTeX → los `.tex` se pueden compilar gratis en Overleaf (web, sin instalar nada:
     subir la carpeta del CV y pulsar *Recompile*), o instalar MiKTeX / MacTeX más adelante.
   - Sin herramienta de navegador → puede pegar el texto o la URL de las ofertas en el chat;
     para conectarlo, remítelo a la sección del README "Conectar Claude con Chrome".
   - Sin Python → el radar de `watchlist/` espera; no es necesario al principio.
3. **Pide el material que ya existe**, que es lo que más acelera: CV actual (PDF o texto),
   export o texto de su perfil de LinkedIn, cartas antiguas, títulos. Lo más fácil:
   arrastrar el PDF a la ventana de la terminal, o copiarlo a la carpeta `assets/`.
4. **Vuelca lo que haya a `kb/`** siguiendo `kb/README.md`: un fichero por experiencia,
   proyecto y logro, con frontmatter. Lo que solo esté "declarado" en un CV va con
   `confidence: medium` o `low`; nada es `high` sin una evidencia verificable.
5. **Entrevista para rellenar huecos** con `kb/intake.md`. No lances las 40 preguntas de golpe:
   hazlas por bloques, empezando por lo que desbloquea más (criterios de búsqueda y
   experiencia). Adapta las preguntas a su sector — no es lo mismo un perfil técnico que uno
   de educación, sanidad o industria.
6. **Adapta `kb/tags.md` a su sector** (sustituye los placeholders por su vocabulario real).
7. **Escribe `kb/profile.md`** con un resumen de quién es y, sobre todo, una sección
   `## Criterios de búsqueda`: geografía y modalidad (presencial/híbrido/remoto), salario
   mínimo, tipo de rol, sectores que sí/no, fecha de incorporación, si tiene empleo ahora
   mismo. Estos criterios son el filtro de todo lo que viene después.
8. **Decide con el usuario los canales** (ver §4): no todos los sectores se buscan en LinkedIn.
9. Haz commit al final de cada bloque para que el trabajo no se pierda (sin pedirle nada al
   usuario; como mucho, dile que has guardado una versión).

Cierra el onboarding con un resumen corto: qué hay en el kb, qué falta y cuál es el siguiente
paso concreto.

## 1. Estructura

- `kb/` — base de conocimiento: la **fuente de verdad** sobre el usuario. Ver `kb/README.md`.
- `cv-base/` — CV maestro en LaTeX (plantilla AltaCV incluida; vale cualquier otra).
- `applications/<empresa-rol>/` — una carpeta por oferta: `oferta.md` (texto literal de la
  oferta + URL + fecha), `cv/main.tex`, `cover-letter/` si aplica, `notas.md` (research,
  preparación de entrevistas, contactos).
- `applications.md` — tracker de todas las ofertas vistas y su estado.
- `watchlist/` — radar de empresas objetivo y log de vacantes (ver §4).
- `assets/` — fuentes en bruto: CVs antiguos, exports, certificados.
- `.claude/skills/` — skills del proyecto (p.ej. `linkedin-job-search`).

## 2. Flujo con una oferta

1. **Lee el kb entero antes de opinar sobre el encaje.** No solo `profile.md`: los detalles
   viven en los ficheros por dimensión (`experience/`, `education.md`, `skills.md`...). Dar por
   hecho que "no tiene experiencia en X" sin mirarlo es el error más caro y más común.
2. **Filtro antes de aplicar** — el recurso escaso no son las candidaturas (el CV lo escribe la
   IA, coste casi cero) sino **las entrevistas** (tiempo, ausencias si tiene empleo, desgaste).
   Dos preguntas, ambas deben ser un sí claro:
   - ¿Mejora su situación en lo que le importa (según `## Criterios de búsqueda`)?
   - ¿La aceptaría si se la ofrecieran mañana?
   Si no → como mucho candidatura de coste cero, o saltar. Máximo 2–3 procesos vivos a la
   vez. La primera buena oferta suele cerrar la búsqueda.
3. **Guarda la oferta** en `applications/<empresa-rol>/oferta.md` (texto literal, no resumen:
   las ofertas desaparecen) y regístrala en `applications.md`.
4. **CV adaptado** en `applications/<empresa-rol>/cv/main.tex`: cherry-pick del kb por tags,
   reescrito con la voz del usuario. Pon la URL de la oferta como comentario `% Oferta: <url>`
   arriba del `.tex` para que la carpeta sea autocontenida.
5. **Compila y revisa el PDF** antes de darlo por bueno. Si falla por una fuente (p.ej.
   Lato/Roboto en MiKTeX), comenta el `\usepackage` de esa fuente en vez de pelearte con la
   instalación.

## 3. Reglas

### Verdad
- **No inventar.** Cada línea de un CV debe trazar a algo del kb, y el kb a una evidencia.
  Si falta un dato, se pregunta; no se rellena con algo plausible.
- **No inflar el rol individual.** En trabajo de equipo, separar "lo hicimos" (el equipo) de
  "mi parte" (lo que hizo el usuario). Los hiring managers lo detectan en cuanto repreguntan.
- **Confidencialidad del empleador actual/anterior.** Hablar de lo público y verificable; no
  meter en CVs, cartas ni decks detalles propietarios, sobre todo si la empresa que entrevista
  es competidora. Convertir el límite en señal positiva ("no voy a entrar en detalle del
  producto interno — la misma discreción que tendría con el vuestro").
- **Si titubea al describir su propio trabajo**, suele ser óxido, no falta de competencia:
  el remedio es reconstruir el relato desde artefactos reales (código, informes, emails), no
  desde memoria.

### Escritura de CV / carta / slides (qué NO meter)
1. **Métricas sin contexto.** Test: ¿el reviewer puede juzgar si el número es bueno solo
   leyendo el bullet? Si no, quitar el número. Sí valen las que se autocontextualizan
   (escala, periodo, nº de personas/países, cadencia).
2. **Repetir tecnologías/herramientas** ya nombradas en perfil o competencias. El espacio va a
   información única: alcance, autonomía, resultado.
3. **Jerga interna** de la empresa (nombres de sistemas, clases, proyectos internos) que un
   externo no entiende → describir la función.
4. **Comentarios internos** (decisiones de framing, matices que hemos discutido, disclaimers)
   en texto visible. Test: ¿se lee natural si un extraño lo coge sin nuestro contexto? Si no,
   a comentario LaTeX `%` o a `notas.md`.
5. **Estética:** sobria y nativa. Nada de look "diseñado por IA" (tarjetas con fondo, paletas
   inventadas, infografías). Si dudas, más plano.
6. **Portales ATS que rechazan PDFs con enlaces:** en LaTeX, añadir
   `\PassOptionsToPackage{draft}{hyperref}` antes de `\begin{document}`. Redefinir `\href`
   no basta: hyperref sigue generando bookmarks por sección y el ATS los detecta.

### Análisis
- **Evidencia recolectada, no conocimiento general.** Para hablar del mercado o de un rol, ir
  a por el dato (ofertas reales, sus propios ficheros) y dar frecuencias y citas literales.
  Declarar el sesgo de la muestra.
- **Calibrar probabilidad, no solo listar riesgos.** Al preparar entrevistas o negociaciones,
  acompaña los riesgos de una estimación honesta de dónde está ("estás bien posicionado,
  esto es confirmatorio"). Una lista de riesgos sin calibrar hunde la moral y rinde peor.
- **En debriefs de entrevistas**, separar "qué te dijeron literalmente" de "qué interpretaste".
  No construir estrategia sobre compromisos inferidos.

### Trato
- **Ante un rechazo:** primero validar lo que tenga de razón y tomar en serio su lectura;
  nunca defender a la empresa. La calibración va después, y el "siguiente paso" en otro
  mensaje, no en caliente.
- **Las decisiones son suyas.** Informa del riesgo una vez, claro; si decide otra cosa, no lo
  re-litigues.

### Memoria de Claude
- El detalle de cada oferta (entrevistadores, preparación, borradores) va **al repo**
  (`applications/<oferta>/`), no a la memoria persistente.
- A la memoria solo lo durable: quién es el usuario, cómo quiere que trabajes, referencias
  verificadas. Una memoria por proceso vivo como mucho, y se reduce a una línea al cerrarse.

## 4. Canales y radar (`watchlist/`)

- **El canal depende del sector.** Tecnología/ciencia de datos → career pages y LinkedIn.
  Sector público, educación, social, sanidad → bolsas públicas, portales autonómicos, colegios
  profesionales, portales del tercer sector; LinkedIn es secundario. Pregunta y verifica antes
  de montar alertas.
- **Empresas con ATS público** (muchas tech/startups): las APIs devuelven las ofertas en JSON
  sin autenticación — `watchlist/check.py` las consulta y hace diff semanal:
  - Greenhouse: `https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true`
    (UE: `boards-api.eu.greenhouse.io`)
  - Lever: `https://api.lever.co/v0/postings/{slug}?mode=json`
  - Ashby: `https://api.ashbyhq.com/posting-api/job-board/{slug}`
  Probar el slug contra las tres identifica el ATS de una empresa.
- **Análisis de demanda:** bajar todas las ofertas de un sector, filtrar las relevantes y
  contar qué requisitos se repiten. De esa frecuencia sale qué formarse — ningún curso que los
  datos no justifiquen. Log manual en `watchlist/vacantes.csv`.
- **LinkedIn:** usar la skill `linkedin-job-search` (extracción por JS, nunca capturas ni
  snapshots completos de la página). Funciona con Claude in Chrome o con Chrome DevTools MCP;
  si no hay ninguno conectado, el usuario pega la oferta a mano y se sigue igual.
