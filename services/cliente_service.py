from models.cliente_model import (
    get_all_clientes,
    get_cliente_by_id,
    insert_cliente,
    update_cliente,
    patch_cliente,
    delete_cliente
)

def listar_clientes():
    return get_all_clientes()

def obtener_cliente(cliente_id):
    return get_cliente_by_id(cliente_id)

def agregar_cliente(data):
    campos = ["nombre", "dni", "telefono", "correo", "procedencia", "acompanantes"]
    
    for campo in campos:
        if campo not in data:
            raise ValueError(f"Campo requerido faltante: {campo}")

    # Validación adicional
    if len(data["dni"]) != 8 or not data["dni"].isdigit():
        raise ValueError("El DNI debe tener 8 dígitos numéricos.")

    try:
        acompanantes = int(data["acompanantes"])
    except:
        raise ValueError("La cantidad de acompañantes debe ser numérica.")

    insert_cliente(
        data["nombre"].strip(),
        data["dni"].strip(),
        data["telefono"].strip(),
        data["correo"].strip(),
        data["procedencia"].strip(),
        acompanantes
    )

def actualizar_cliente(cliente_id, data):
    update_cliente(
        cliente_id,
        data['nombre'], data['dni'], data.get('telefono'),
        data.get('correo'), data.get('procedencia'), data.get('acompanantes')
    )

def modificar_cliente(cliente_id, campos):
    patch_cliente(cliente_id, campos)

def eliminar_cliente(cliente_id):
    delete_cliente(cliente_id)
