# Checklist técnico de code review

Revisión sobre el repositorio completo. Completar la columna "Revisor" con quien realizó cada
verificación (revisión cruzada entre integrantes).

## Checklist aplicado

| # | Criterio | Estado | Evidencia | Revisor |
|---|----------|--------|-----------|---------|
| 1 | Separación de responsabilidades (SRP): dominio, persistencia, servicio y presentación en módulos distintos | Aprobado | `solicitudes/` (5 módulos) | [COMPLETAR] |
| 2 | El servicio depende de abstracciones, no de archivos (DIP) | Aprobado | `servicios.py` recibe `SolicitudRepository` | [COMPLETAR] |
| 3 | Existen al menos dos implementaciones intercambiables del repositorio (OCP/LSP) | Aprobado | `RepositorioJSON`, `RepositorioEnMemoria` + pruebas de contrato | [COMPLETAR] |
| 4 | Interfaces pequeñas (ISP): quien solo consulta no depende de escribir | Aprobado | `ConsultaService` usa `SolicitudLectura` | [COMPLETAR] |
| 5 | Manejo de errores explícito con excepciones propias | Aprobado tras corrección | `excepciones.py`; hallazgo H2 | [COMPLETAR] |
| 6 | Nombres expresivos y sin parámetros opcionales masivos en la API nueva | Aprobado con observación | `DatosNuevaSolicitud`; la fachada conserva 8 parámetros (O3) | [COMPLETAR] |
| 7 | Sin duplicación de lógica de persistencia | Aprobado | un solo punto de lectura/escritura | [COMPLETAR] |
| 8 | Comportamiento externo preservado frente a la versión 1 | Aprobado | `test_equivalencia_v1_v2.py` (25 pasos) | [COMPLETAR] |
| 9 | Cobertura de ramas medida | Aprobado | 99 % (`docs/evidencias/02_cobertura_ramas.txt`) | [COMPLETAR] |
| 10 | Datos de prueba sintéticos | Aprobado tras corrección | hallazgo H6 | [COMPLETAR] |
| 11 | Análisis estático sin errores graves | Aprobado con observación | flake8 0 avisos; pylint 9.06/10 (O2) | [COMPLETAR] |

## Hallazgos y correcciones

| Id | Hallazgo | Severidad | Corrección |
|----|----------|-----------|------------|
| H1 | `SolicitudService` del informe contenía solo el constructor; la suite no podía ejecutarse | Alta | Servicio completo y pruebas ejecutadas |
| H2 | `obtener_todas()` devolvía `[]` con JSON corrupto; el siguiente guardado habría sobrescrito todos los datos | Alta | Ahora lanza `RepositorioError`; el archivo no se toca; hay pruebas |
| H3 | Se afirmaba comportamiento idéntico sin evidencia | Alta | Prueba de equivalencia v1/v2 con 25 pasos y comparación byte a byte |
| H4 | El informe indicaba más de 120 líneas para la versión 1; mide 66 | Media | Cifra corregida con la medición de `radon` |
| H5 | La suite solo importaba v2 aunque se decía probada sobre ambas versiones | Media | La prueba de equivalencia importa y ejecuta ambas |
| H6 | Pruebas con nombres y DNI de apariencia real | Media | Datos sintéticos |
| H7 | Se mencionaba `try/catch` (no existe en Python) | Baja | `try/except` |
| H8 | ISP y LSP afirmados sin demostración | Media | Interfaces separadas y segunda implementación con pruebas de contrato |

## Observaciones pendientes (no bloquean la aceptación)

- O1: `filtrar` combina DNI y estado con OR, como la versión 1; probablemente debería ser AND.
- O2: pylint marca docstrings faltantes y un aviso de clase abstracta intermedia.
- O3: la fachada mantiene 8 parámetros por compatibilidad; debería retirarse en una versión futura.
- O4: `tipo` sigue siendo un texto libre; el caso sugerido por la cátedra contempla prioridad y tipos.

## Criterios de aceptación técnica

1. Las 50 pruebas pasan en un clon limpio del repositorio.
2. La prueba de equivalencia v1/v2 pasa en los 25 pasos.
3. Cobertura de ramas mayor o igual al 95 %.
4. flake8 sin avisos sobre `solicitudes/`.
5. Ningún camino de error puede borrar o sobrescribir datos existentes.
