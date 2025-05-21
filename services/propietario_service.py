from models.propietario_model import (
    get_all_propietarios,
    get_propietario_by_id,
    insert_propietario,
    update_propietario,
    patch_propietario,
    delete_propietario
)

def listar_propietarios():
    return get_all_propietarios()

def obtener_propietario(propietario_id):
    return get_propietario_by_id(propietario_id)

def agregar_propietario(data):
    if not data.get("nombres") or not data.get("dni"):
        raise ValueError("Nombres y DNI son obligatorios")
    insert_propietario(data["nombres"], data["dni"], data.get("telefono"))

def actualizar_propietario(propietario_id, data):
    update_propietario(propietario_id, data["nombres"], data["dni"], data.get("telefono"))

def modificar_propietario(propietario_id, campos):
    patch_propietario(propietario_id, campos)

def eliminar_propietario(propietario_id):
    delete_propietario(propietario_id)
