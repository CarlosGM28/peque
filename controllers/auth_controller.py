from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.auth_service import verificar_login

auth_bp = Blueprint('auth', __name__)

# Vista del login
@auth_bp.route("/login", methods=["GET"])
def login():
    return render_template("vistas/login.html")

# Procesar login
@auth_bp.route("/login", methods=["POST"])
def login_post():
    username = request.form.get("email")
    password = request.form.get("password")

    usuario = verificar_login(username, password)

    if usuario:
        session['usuario_id'] = usuario['id']
        session['username'] = usuario['username']
        session['rol'] = usuario.get('rol', 'usuario')
        return redirect(url_for("dashboard.index"))
    else:
        flash("Usuario o contraseña incorrectos", "danger")
        return redirect(url_for("auth.login"))


# Cerrar sesión
@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
