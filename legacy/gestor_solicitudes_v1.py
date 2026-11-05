# Version Inicial: gestor_solicitudes_v1.py (Tag: estado-inicial)
import json, os, datetime

class GestorSolicitudesSistema:
    def __init__(self, archivo="solicitudes.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as f:
                json.dump([], f)

    def ejecutar_operacion(self, op, id_sol=None, dni=None, nombre=None, tipo=None, desc=None, estado=None, resp=None):
        with open(self.archivo, "r") as f:
            datos = json.load(f)

        if op == "CREAR":
            if not dni or not tipo or len(dni) < 7:
                print("Error: Datos invalidos.")
                return False
            nueva = {
                "id": len(datos) + 1, "dni": dni, "estudiante": nombre,
                "tipo": tipo, "descripcion": desc, "estado": "PENDIENTE",
                "responsable": "SIN ASIGNAR", "fecha": str(datetime.date.today())
            }
            datos.append(nueva)
            with open(self.archivo, "w") as f: json.dump(datos, f, indent=4)
            print("Solicitud creada con exito.")
            return True

        elif op == "CAMBIAR_ESTADO":
            for s in datos:
                if s["id"] == id_sol:
                    if estado in ["PENDIENTE", "EN_PROCESO", "RESUELTO", "RECHAZADO"]:
                        s["estado"] = estado
                        with open(self.archivo, "w") as f: json.dump(datos, f, indent=4)
                        print(f"Estado de la solicitud {id_sol} actualizado a {estado}.")
                        return True
                    else:
                        print("Estado invalido.")
                        return False
            print("Solicitud no encontrada.")
            return False

        elif op == "ASIGNAR":
            for s in datos:
                if s["id"] == id_sol:
                    s["responsable"] = resp
                    with open(self.archivo, "w") as f: json.dump(datos, f, indent=4)
                    print(f"Responsable {resp} asignado a la solicitud {id_sol}.")
                    return True
            print("Solicitud no encontrada.")
            return False

        elif op == "FILTRAR":
            res = [s for s in datos if (dni and s["dni"] == dni) or (estado and s["estado"] == estado)]
            print(f"--- RESULTADOS DE BUSQUEDA ({len(res)}) ---")
            for r in res:
                print(f"ID: {r['id']} | DNI: {r['dni']} | Estudiante: {r['estudiante']} | Tipo: {r['tipo']} | Estado: {r['estado']} | Resp: {r['responsable']}")
            return res

        elif op == "REPORTE":
            tot = len(datos)
            pend = sum(1 for s in datos if s["estado"] == "PENDIENTE")
            res = sum(1 for s in datos if s["estado"] == "RESUELTO")
            print("=== REPORTE GENERAL DE SOLICITUDES ===")
            print(f"Total: {tot} | Pendientes: {pend} | Resueltos: {res}")
            return {"total": tot, "pendientes": pend, "resueltos": res}
