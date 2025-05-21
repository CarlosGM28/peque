from werkzeug.security import generate_password_hash
from models.usuario_model import *

def listar_usuarios():
    return get_all_usuarios()

def obtener_usuario(user_id):
    return get_usuario_by_id(user_id)

def registrar_usuario(data):
    if not data.get("username") or not data.get("password"):
        raise ValueError("Usuario y contraseña son obligatorios")
    
    hashed_password = generate_password_hash(data["password"])
    insert_usuario(data["username"], hashed_password, data.get("rol", "usuario"))

def editar_usuario(user_id, data):
    hashed_password = generate_password_hash(data["password"])
    update_usuario(user_id, data["username"], hashed_password, data.get("rol", "usuario"))

def modificar_usuario(user_id, campos):
    if "password" in campos:
        campos["password"] = generate_password_hash(campos["password"])
    patch_usuario(user_id, campos)

def eliminar_usuario(user_id):
    delete_usuario(user_id)
