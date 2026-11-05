# TPI Metodología de Sistemas II – Gestión de Solicitudes Académicas

Trabajo Práctico Integrador de la Tecnicatura Universitaria en Programación (a distancia), comisión 9.
Autores: Walter Verdún e Ignacio Salazar.

El proyecto toma un módulo funcional pero mal estructurado (versión inicial) y lo evoluciona mediante
refactoring seguro hacia una versión por capas, verificando con pruebas automáticas que el
comportamiento externo se mantiene.

## Descripción

Sistema de consola que administra solicitudes académicas de estudiantes (reclamos, equivalencias,
excepciones). Persiste los datos en un archivo JSON local.

## Funcionalidades

- Registrar solicitud (valida DNI de al menos 7 caracteres y tipo presente).
- Cambiar el estado: `PENDIENTE`, `EN_PROCESO`, `RESUELTO`, `RECHAZADO`.
- Asignar responsable.
- Buscar/filtrar por DNI o por estado.
- Reporte estadístico (total, pendientes, resueltos).

## Tecnologías

Python 3.10 o superior, `unittest` (biblioteca estándar). No requiere dependencias para ejecutarse.
Herramientas de análisis opcionales: `coverage`, `flake8`, `radon`, `pylint` (ver `requirements-dev.txt`).

## Instalación y uso

```bash
git https://github.com/walter404/TPI-MS2-GestionSolicitudes
cd TPI-MS2-GestionSolicitudes
python -m solicitudes          # demostración con datos sintéticos
python -m unittest discover -v # 50 pruebas
```

```python
from solicitudes import (RepositorioJSON, SolicitudService, ConsultaService,
                         DatosNuevaSolicitud)

repo = RepositorioJSON("solicitudes.json")
comandos, consultas = SolicitudService(repo), ConsultaService(repo)
comandos.crear_solicitud(DatosNuevaSolicitud("30111222", "Estudiante Demo", "Reclamo", "Desc"))
print(consultas.generar_reporte())
```

La fachada `GestorSolicitudesConsola.ejecutar_operacion(...)` conserva la firma y los mensajes de la
versión 1 y sirve para demostrar la equivalencia de comportamiento.

## Estructura

```
legacy/gestor_solicitudes_v1.py   versión inicial (referencia, tag estado-inicial)
solicitudes/                      versión refactorizada (tag estado-refactorizado)
  modelos.py                      entidades, enum de estados, DatosNuevaSolicitud
  excepciones.py                  excepciones del dominio
  repositorio.py                  contratos (lectura/escritura) + JSON y memoria
  servicios.py                    SolicitudService (comandos) y ConsultaService (consultas)
  consola.py                      fachada de consola compatible con la versión 1
tests/                            unitarias, de contrato, de equivalencia v1/v2
docs/                             checklist de code review, decisiones, evidencias, diagramas
```

## Tags de Git

`estado-inicial`, `etapa-diagnostico`, `etapa-refactoring`, `etapa-pruebas`, `etapa-docs`,
`estado-refactorizado`. Ver `docs/GUIA_TAGS.md`.

## Datos

Todos los datos de ejemplo y de prueba son sintéticos.

