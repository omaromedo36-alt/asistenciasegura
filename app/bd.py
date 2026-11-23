import pymysql
import pymysql.cursors
from flask import current_app, g

def obtener_conexion():
    """Abre UNA conexion por peticion y la reutiliza mientras dure la peticion."""
    if "conexion" not in g:
        cfg = current_app.config
        opciones = dict(
            host=cfg["DB_HOST"],
            port=cfg["DB_PORT"],
            user=cfg["DB_USER"],
            password=cfg["DB_PASSWORD"],
            database=cfg["DB_NAME"],
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor, 
            autocommit=False,
        )
        if cfg["DB_SSL_CA"]:
            opciones["ssl"] = {"ca": cfg["DB_SSL_CA"]}
        g.conexion = pymysql.connect(**opciones)
    return g.conexion

def cerrar_conexion(_error=None):
    conexion = g.pop("conexion", None)
    if conexion is not None:
        conexion.close()

def consultar(sql, parametros=None):
    """SELECT que devuelve una lista de filas."""
    with obtener_conexion(). cursor()as cursor:
         cursor.execute(sql,parametros or ())
         return cursor.fetchall()

def consultar(sql, parametros=None):
    """SELECT que devuelve una sola fila (o None)."""
    with obtener_conexion(). cursor()as cursor:
         cursor.execute(sql,parametros or ())
         return cursor.fetchall()

def ejecutar(sql, parametros=None):
    """INSET / UPDATE / DELETE. devuelve el id generado (si lo hay)."""
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute(sql, parametros or ())
            nuevo_id = cursor.lastrowid
        conexion.commit()
        return nuevo_id
    except Exception:
        conexion.rollback()
        raise

def init_app(app):
    app.teardown_appcontext(cerrar_conexion)