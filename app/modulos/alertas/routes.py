# app/modulos/alertas/routes.py  —  Equipo E4: Alertas WhatsApp
# Este archivo es de E4. Solo E4 lo modifica.
from flask import Blueprint, render_template
 
from app.comun.auth import rol_requerido
 
bp = Blueprint("alertas", __name__,
               template_folder="templates", static_folder="static",
               static_url_path="/static/alertas")
 
 
@bp.route("/")
@rol_requerido("Administrador", "Orientadora")
def index():
    return render_template("alertas/index.html")