#run.py punto de arranque de la aplicacion.
# En tu compu: python tun.py
# En Render: gunicorn run:app
from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=app.config["MODO_DESARROLLO"], PORT=5000)