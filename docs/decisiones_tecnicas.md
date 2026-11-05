# Decisiones técnicas

## D1 – Arquitectura por capas
Se separan dominio (`modelos.py`), persistencia (`repositorio.py`), casos de uso (`servicios.py`) y
presentación (`consola.py`). Motivo: la clase original mezclaba validación, I/O de archivo y mensajes
de consola, lo que impedía probar cada parte por separado.

## D2 – Fachada compatible con la versión 1
`GestorSolicitudesConsola` conserva firma y mensajes de `ejecutar_operacion`. Motivo: demostrar con
una prueba automática que el comportamiento externo no cambia. Costo: la fachada mantiene 8
parámetros; se documenta como deuda pendiente.

## D3 – Errores como excepciones, no como booleanos
Los servicios lanzan excepciones propias; la fachada las traduce a los mensajes originales.
Motivo: el `bool` de la versión 1 no distinguía la causa del fallo.

## D4 – JSON corrupto no devuelve lista vacía
Se lanza `RepositorioError` y no se escribe el archivo. Motivo: devolver `[]` y luego guardar
borraría todos los datos. Es una mejora deliberada sobre la versión 1, que se caía con
`JSONDecodeError`.

## D5 – Escritura atómica
Se escribe en un archivo temporal y se reemplaza con `os.replace`. Motivo: evitar archivos a medias
si el proceso se interrumpe durante el guardado.

## D6 – Interfaces de lectura y escritura separadas
`SolicitudLectura` y `SolicitudEscritura`; `SolicitudRepository` las combina. `ConsultaService`
depende solo de lectura. Motivo: aplicar ISP de forma verificable.

## D7 – Se mantiene la semántica OR del filtro
Un refactoring no debe cambiar el comportamiento. La combinación por OR queda documentada como
mejora futura (observación O1 del code review).

## D8 – Identificador con máximo + 1
`max(ids) + 1` en lugar de `len + 1`. Sin operación de borrado ambos coinciden; el nuevo cálculo no
repite identificadores si en el futuro se agregan bajas.

## D9 – Reloj inyectable
`SolicitudService` recibe `hoy` (por defecto `date.today`). Motivo: pruebas deterministas de la
fecha.
