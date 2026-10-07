from flask import Flask

from app.views.usuario_view import usuario_bp


def create_app():
    """Cria e configura a aplicação Flask."""

    app = Flask(__name__)
    app.register_blueprint(usuario_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)