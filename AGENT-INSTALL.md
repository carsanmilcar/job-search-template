# Instalación — instrucciones para el asistente de IA

Estás instalando el *job search kit* para una persona que probablemente **no programa**.
Haz tú cada paso, explícalo en una frase llana y no le pidas que teclee comandos. Estos pasos
van seguidos: no pares entre ellos salvo donde se indica.

## Reglas

1. **Tu primera respuesta es corta.** Nada de diagnósticos, requisitos ni resúmenes de este
   documento. Instala (pasos 0–1) y lo primero que le pidas al usuario es su CV — salvo que
   ya lo haya adjuntado, en cuyo caso no pidas nada y sigue.
2. **Si te bloqueas, pregunta; no informes.** Una pregunta corta con una opción por defecto
   que pueda aceptar con un "sí". Un informe de lo que falta no le sirve a quien no programa.
3. **Cuenta lo que ha pasado de verdad.** Si algo falla, dilo; no lo tapes.

## 0. Dónde estás

- Necesitas escribir en **su disco real**. Si estás en un sandbox, un contenedor o una sesión
  en la nube, díselo en tu primera respuesta y para: esto tiene que vivir en su ordenador.
- La carpeta de trabajo es la carpeta abierta en esta conversación. Si no está vacía (aparte
  de ficheros ocultos), pregunta antes de mezclar nada.

## 1. Traer la plantilla sin enlazarla al repo público

La copia del usuario **no debe quedar conectada al repo público**: ahí va a guardar su CV,
sueldos y contactos, y un `git push` por error los publicaría.

Con git disponible (lo normal):

```bash
git clone --depth 1 https://github.com/carsanmilcar/job-search-template.git _plantilla
# mover TODO el contenido (incluidos .claude/ y .gitignore) a la carpeta actual, sin _plantilla/.git
rm -rf _plantilla/.git
# ...mover y borrar _plantilla/
git init
git add -A
git commit -m "Copia inicial del job search kit"
```

Sin git (Windows sin Git for Windows): descarga
`https://github.com/carsanmilcar/job-search-template/archive/refs/heads/main.zip`, descomprime
el contenido de `job-search-template-main/` en la carpeta actual y borra el zip. Dile que
conviene instalar [Git for Windows](https://git-scm.com/downloads/win) para guardar versiones
de su trabajo, pero **no bloquees**: sigue sin él.

Comprueba que existen `CLAUDE.md`, `kb/` y `.claude/skills/linkedin-job-search/SKILL.md`.

## 2. Arrancar

Lee `CLAUDE.md` entero y sigue su **§0 Primera sesión** desde el paso 2 (el 1, privacidad, ya
queda cubierto: no hay remoto). Dile en dos líneas qué has hecho. Si adjuntó el CV, guarda una
copia en `assets/` si puedes y empieza a volcarlo al kb; si no, pídeselo.

Si más adelante quiere copia en la nube, ayúdale a crear un repo **privado** en GitHub y
enlazarlo; nunca al repo plantilla.
