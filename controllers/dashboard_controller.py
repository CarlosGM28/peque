from flask import Blueprint, render_template, session, redirect, url_for

dashboard_bp = Blueprint('dashboard', __name__, url_prefix="/dashboard")

# Validar sesión antes de cargar cualquier vista del dashboard
def validar_sesion():
    return 'usuario_id' in session

@dashboard_bp.route("/")
def index():
    if not validar_sesion():
        return redirect(url_for("auth.login"))
    return render_template("dashboard/dashboard.html")

@dashboard_bp.route("/clientes")
def vista_clientes():
    if not validar_sesion():
        return redirect(url_for("auth.login"))
    return render_template("dashboard/clientes.html")

@dashboard_bp.route("/propietarios")
def vista_propietarios():
    if not validar_sesion():
        return redirect(url_for("auth.login"))
    return render_template("dashboard/propietarios.html")

@dashboard_bp.route("/pequepeques")
def vista_pequepeques():
    if not validar_sesion():
        return redirect(url_for("auth.login"))
    return render_template("dashboard/pequepeques.html")

@dashboard_bp.route("/paquetes")
def vista_paquetes():
    if not validar_sesion():
        return redirect(url_for("auth.login"))
    return render_template("dashboard/paquetes.html")

@dashboard_bp.route("/servicios")
def vista_servicios():
    if not validar_sesion():
        return redirect(url_for("auth.login"))
    return render_template("dashboard/servicios.html")

@dashboard_bp.route("/usuarios")
def vista_usuarios():
    if not validar_sesion():
        return redirect(url_for("auth.login"))
    return render_template("dashboard/usuarios.html")
