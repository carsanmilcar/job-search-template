# Knowledge Base

DB en markdown de todo lo mencionable en CVs. Sirve para hacer cherry-picking según oferta.

## Estructura

- `profile.md` — quién eres en resumen + `## Criterios de búsqueda` (geografía, modalidad, salario, roles). Filtra todas las ofertas.
- `intake.md` — cuestionario de la primera sesión (Claude lo usa para entrevistarte).
- `experience/` — un `.md` por rol/empresa.
- `projects/` — un `.md` por proyecto independiente.
- `achievements/` — logros atómicos (un `.md` por logro reusable). Cada uno se puede meter como bullet en el CV de turno.
- `education.md` — formación.
- `skills.md` — competencias por categoría.
- `publications.md` — papers, datasets, librerías publicadas.
- `languages.md` — idiomas.
- `tags.md` — taxonomía controlada de tags.

## Cómo se usa

1. Cuando llega una oferta, abrir `tags.md` y elegir tags relevantes para tu perfil.
2. Filtrar `achievements/` por esos tags → conjunto candidato de bullets.
3. Cherry-pick + reescritura final en el CV target con tu propia voz.

## Frontmatter estándar

Cada entrada lleva:

```yaml
---
title: ...
type: experience | project | achievement | education | skill | publication
status: active | completed | wip
domains: [...]
skill-areas: [...]
methods: [...]
tools: [...]
audiences: [...]
confidence: high | medium | low
evidence:
  - <url o ruta verificable>
---
```

- **confidence: high** — verificable públicamente (commit, Zenodo, paper).
- **confidence: medium** — interno pero defendible en entrevista.
- **confidence: low** — necesita refrescarse antes de mencionar.

## Reglas

- **No inventar.** Cada bullet debe trazar a algo verificable (commit, informe, email, CV previo, etc.). Guarda esas fuentes en `assets/` si quieres tenerlas a mano.
- **No pulir voz aquí.** El KB es material en bruto. La voz va al CV final.
- **Tags consistentes.** Si necesitas un tag nuevo, añadirlo a `tags.md` antes de usarlo.
