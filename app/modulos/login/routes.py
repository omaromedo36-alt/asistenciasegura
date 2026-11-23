# app/modulos/login/routes.py Equipo E1: Inicio de sesión + paneles por rol 
# Este archivo es de E1. Solo E1 lo modifica.
#
# CONTRATO: al iniciar sesión, E1 debe guardar:
# session["usuario_id"], session["rol"], session["nombre"] (ver app/comun/auth.py)

from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash
from app.comun.auth import login_requerido

# Si tienes un modelo o función de base de datos para buscar usuarios, impórtala aquí:
# from app.modulos.login.models import obtener_usuario_por_correo

bp = Blueprint(
    "login", 
    __name__, 
    template_folder="templates", 
    static_folder="static", 
    static_url_path="/static/login"
)

@bp.route("/login", methods=["GET", "POST"])
def entrar():
    if request.method == "POST":
        correo = request.form.get("correo")
        contrasena = request.form.get("contrasena")
        
        # TODO E1: Validar correo y contraseña con check_password_hash, bloqueo por intentos, etc.
        # Ejemplo de implementación sugerida:
        # usuario = obtener_usuario_por_correo(correo)
        # 
        # if usuario and check_password_hash(usuario["password_hash"], contrasena):
        #     # Cumpliendo con el contrato:
        #     session["usuario_id"] = usuario["id"]
        #     session["rol"] = usuario["rol"]
        #     session["nombre"] = usuario["nombre"]
        #     
        #     flash("Inicio de sesión exitoso.", "success")
        #     return redirect(url_for("login.panel"))
        # else:
        #     flash("Credenciales inválidas o cuenta bloqueada.", "danger")
        
        pass

    return render_template("login/entrar.html")

@bp.route("/logout")
def salir():
    session.clear()
    flash("Sesión cerrada.", "info")
    return redirect(url_for("login.entrar"))

@bp.route("/panel")
@login_requerido
def panel():
    rol = session.get("rol")
    
    # TODO E1: Mostrar un panel distinto según session["rol"]
    if rol == "admin":
        return render_template("login/panels/admin.html")
    elif rol == "empleado":
        return render_template("login/panels/empleado.html")
    else:
        # Panel por defecto o genérico
        return render_template("login/panel.html")