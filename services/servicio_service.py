from models.servicio_model import (
    get_all_servicios,
    get_servicio_by_id,
    insert_servicio,
    update_servicio,
    patch_servicio,
    delete_servicio
)

def listar_servicios():
    return get_all_servicios()

def obtener_servicio(servicio_id):
    return get_servicio_by_id(servicio_id)

def agregar_servicio(data):
    if not data.get("cliente_id") or not data.get("paquete_id") or not data.get("pequepeque_id"):
        raise ValueError("cliente_id, paquete_id y pequepeque_id son obligatorios")
    insert_servicio(data["cliente_id"], data["paquete_id"], data["pequepeque_id"])

def actualizar_servicio(servicio_id, data):
    update_servicio(servicio_id, data["cliente_id"], data["paquete_id"], data["pequepeque_id"])

def modificar_servicio(servicio_id, campos):
    patch_servicio(servicio_id, campos)

def eliminar_servicio(servicio_id):
    delete_servicio(servicio_id)
