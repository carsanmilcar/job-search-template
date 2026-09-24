# Radar de vacantes

- `companies.csv` — empresas objetivo: carril (tipo de empresa/rol), ubicación y modalidad,
  banda salarial estimada, ATS + slug, vía de entrada (contactos que te pueden presentar), notas.
- `check.py` — `python watchlist/check.py`, una vez por semana: consulta las APIs públicas de
  Greenhouse / Lever / Ashby de las empresas del CSV, filtra títulos por `KEYWORDS` y muestra
  qué ofertas son nuevas o se han cerrado desde la última vez (guarda `snapshot.json`, que no
  se versiona).
- `vacantes.csv` — log manual de toda oferta relevante que veas, aunque esté cerrada. **De la
  frecuencia de requisitos sale qué formarse**: ningún curso que la tabla no justifique.

## Cómo averiguar el ATS de una empresa

Mira la URL de su página de empleo (`boards.greenhouse.io/<slug>`, `jobs.lever.co/<slug>`,
`jobs.ashbyhq.com/<slug>`), o pide a Claude que pruebe el nombre contra las tres APIs.
Valores de `ats`: `greenhouse`, `greenhouse-eu`, `lever`, `ashby`. Pon `verificar` si no lo
sabes todavía y `workday` u otro si no tiene API pública (el script se la salta; se revisa a mano).

## No todo está en un ATS

Para empleo público, educación, social o sanidad, los canales son otros (bolsas y portales
autonómicos, colegios profesionales, portales del tercer sector). Anótalos en
`companies.csv` con `ats` vacío y revísalos a mano.
