# Guía para armar el historial y los tags

La consigna pide un historial ordenado y tags por hito. Se recomienda que cada integrante haga sus
propios commits con su identidad, para que la participación quede demostrada en el historial.

```bash
git init
git branch -M main

# 1. Sistema base
git add legacy/gestor_solicitudes_v1.py README.md
git commit -m "Sistema base: version inicial monolitica"
git tag estado-inicial

# 2. Diagnostico
git add docs/diagramas/antes.* docs/evidencias/05_flake8.txt docs/evidencias/06_pylint.txt
git commit -m "Diagnostico de deuda tecnica y code smells"
git tag etapa-diagnostico

# 3. Refactoring
git add solicitudes/
git commit -m "Refactoring por capas: modelos, repositorio, servicios, consola"
git tag etapa-refactoring

# 4. Pruebas
git add tests/ docs/evidencias/0[1-4]_* docs/evidencias/07_* docs/evidencias/08_*
git commit -m "Pruebas unitarias, de contrato y de equivalencia v1/v2"
git tag etapa-pruebas

# 5. Documentacion
git add docs/ requirements-dev.txt
git commit -m "Checklist de code review, decisiones tecnicas y registro de prompts"
git tag etapa-docs

# 6. Estado final
git tag estado-refactorizado

git remote add origin https://github.com/walterverdun/TPI-MS2-GestionSolicitudes.git
git push -u origin main --tags
```

Antes de entregar, verificar que el repositorio sea público (o accesible para la cátedra), que los
tags existan (`git ls-remote --tags origin`) y que un clon limpio ejecute
`python -m unittest discover`.

La consigna escribe el tag final como "estadorefactorizado" en un punto y como
`estado-refactorizado` en otro; conviene confirmar con la cátedra y, si hay duda, crear ambos.
