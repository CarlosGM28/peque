from models.pequepeque_model import (
    get_all_pequepeques,
    get_pequepeque_by_id,
    insert_pequepeque,
    update_pequepeque,
    patch_pequepeque,
    delete_pequepeque
)

def listar_pequepeques():
    return get_all_pequepeques()

def obtener_pequepeque(pequepeque_id):
    return get_pequepeque_by_id(pequepeque_id)

def agregar_pequepeque(data):
    campos_obligatorios = ["matricula", "nombre", "capacidad", "material", "fecha_registro", "fecha_inicio", "color", "propietario_id"]
    for campo in campos_obligatorios:
        if not data.get(campo):
            raise ValueError(f"El campo '{campo}' es obligatorio")
    insert_pequepeque(data)

def actualizar_pequepeque(pequepeque_id, data):
    update_pequepeque(pequepeque_id, data)

def modificar_pequepeque(pequepeque_id, campos):
    patch_pequepeque(pequepeque_id, campos)

def eliminar_pequepeque(pequepeque_id):
    delete_pequepeque(pequepeque_id)
