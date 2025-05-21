from models.paquete_model import (
    get_all_paquetes,
    get_paquete_by_id,
    insert_paquete,
    update_paquete,
    patch_paquete,
    delete_paquete
)

def listar_paquetes():
    return get_all_paquetes()

def obtener_paquete(paquete_id):
    return get_paquete_by_id(paquete_id)

def agregar_paquete(data):
    if not data.get("denominacion") or not data.get("precio"):
        raise ValueError("Denominación y precio son obligatorios")
    insert_paquete(
        data["denominacion"], data["precio"],
        data.get("tiempo_promedio"), data.get("paradas")
    )

def actualizar_paquete(paquete_id, data):
    update_paquete(
        paquete_id,
        data["denominacion"], data["precio"],
        data.get("tiempo_promedio"), data.get("paradas")
    )

def modificar_paquete(paquete_id, campos):
    patch_paquete(paquete_id, campos)

def eliminar_paquete(paquete_id):
    delete_paquete(paquete_id)
