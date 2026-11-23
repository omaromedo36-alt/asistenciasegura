# app/modulos/rfid_panel/routes.py  —  Equipo E3: Credenciales RFID/NFC
# Este archivo es de E3. Solo E3 lo modifica.
from flask import Blueprint, render_template
 
from app.comun.auth import rol_requerido
 
bp = Blueprint("rfid_panel", __name__,
               template_folder="templates", static_folder="static",
               static_url_path="/static/rfid_panel")
 
 
@bp.route("/")
@rol_requerido("Administrador")
def index():
    return render_template("rfid_panel/index.html")