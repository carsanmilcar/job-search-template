# Job search kit (para usar con Claude Code)

Un repo para llevar una búsqueda de empleo con Claude Code: una base de conocimiento
verificada sobre ti, de la que salen CVs y cartas adaptados a cada oferta, más un radar de
vacantes. Tú aportas los hechos y decides; Claude mantiene el sistema.

## Cómo empezar

1. **Haz tu copia PRIVADA.** Botón *Use this template* → *Create a new repository* →
   marca **Private**. Aquí vas a meter tu CV, salarios y contactos: no lo hagas en un fork
   público.
   (Sin GitHub: descarga el ZIP, descomprímelo y haz `git init` dentro.)
2. Clónala en tu PC y abre Claude Code en la carpeta:
   ```
   git clone https://github.com/<tu-usuario>/<tu-repo>.git
   cd <tu-repo>
   claude
   ```
3. Dile algo como: *"Acabo de copiar este repo, empecemos"* — y ten a mano tu CV actual
   (PDF) y, si puedes, el texto de tu perfil de LinkedIn.

Claude lee `CLAUDE.md`, ve que el repo está vacío y te guía: vuelca tu CV al kb, te
entrevista por bloques para rellenar huecos (`kb/intake.md`), fija tus criterios de búsqueda
y decide contigo por qué canales buscar.

## Después, el día a día

- *"Mira esta oferta: <url o texto>"* → la evalúa contra tu kb y tus criterios, y te dice si
  merece una entrevista (no solo una candidatura).
- *"Hazme el CV para esta"* → CV adaptado en `applications/<empresa-rol>/`.
- *"Pasa el radar"* → `python watchlist/check.py` consulta las career pages de tus empresas
  objetivo y te dice qué hay nuevo.

## Estructura

| Carpeta | Qué hay |
|---|---|
| `kb/` | Base de conocimiento sobre ti: la fuente de verdad. Ver `kb/README.md`. |
| `cv-base/` | CV maestro en LaTeX (plantilla [AltaCV](https://github.com/liantze/AltaCV)). |
| `applications/` | Una carpeta por oferta: oferta literal, CV, carta, notas. |
| `applications.md` | Tracker de ofertas y estado. |
| `watchlist/` | Empresas objetivo + log de vacantes vistas + script de radar. |
| `assets/` | Fuentes en bruto (CVs viejos, exports, certificados). |
| `CLAUDE.md` | Las instrucciones y reglas que sigue Claude. Edítalas a tu gusto. |

## Requisitos

- [Claude Code](https://docs.claude.com/claude-code).
- Una distribución LaTeX (MiKTeX, TeX Live, MacTeX) para compilar los CV — o pide a Claude
  otro formato.
- Python 3 para el radar (sin dependencias externas).
- Opcional, para buscar en LinkedIn: el MCP [Chrome DevTools](https://github.com/ChromeDevTools/chrome-devtools-mcp)
  con una pestaña de Chrome donde tengas la sesión de LinkedIn iniciada
  (lo usa la skill `.claude/skills/linkedin-job-search`).
