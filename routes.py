from controllers.index_controller import index_bp
from controllers.cliente_controller import cliente_bp
from controllers.propietario_controller import propietario_bp
from controllers.pequepeque_controller import pequepeque_bp
from controllers.paquete_controller import paquete_bp
from controllers.servicio_controller import servicio_bp
from controllers.usuario_controller import usuario_bp
from controllers.auth_controller import auth_bp
from controllers.dashboard_controller import dashboard_bp 

def register_routes(app):
    app.register_blueprint(index_bp, url_prefix="/")
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)  
    app.register_blueprint(cliente_bp, url_prefix="/api/clientes")
    app.register_blueprint(propietario_bp, url_prefix="/api/propietarios")
    app.register_blueprint(pequepeque_bp, url_prefix="/api/pequepeques")
    app.register_blueprint(paquete_bp, url_prefix="/api/paquetes")
    app.register_blueprint(servicio_bp, url_prefix="/api/servicios")
    app.register_blueprint(usuario_bp, url_prefix="/api/usuarios")
