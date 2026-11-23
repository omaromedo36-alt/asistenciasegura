# app/modulos/usuarios/routes.py  —  Equipo E6: usuarios y roles
# Este archivo es de E6. Solo E6 lo modifica.
from flask import Blueprint, render_template
 
from app.comun.auth import rol_requerido
 
bp = Blueprint("usuarios", __name__,
               template_folder="templates", static_folder="static",
               static_url_path="/static/usuarios")
 
 
@bp.route("/")
@rol_requerido("Administrador")
def index():
    return render_template("usuarios/index.html")