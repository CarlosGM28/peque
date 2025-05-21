from models.usuario_model import validar_credenciales

def verificar_login(username, password):
    return validar_credenciales(username, password)
