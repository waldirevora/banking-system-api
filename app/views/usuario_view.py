from flask import Blueprint, jsonify, request

from app.controllers.usuario_controller import UsuarioController


usuario_bp = Blueprint("usuarios", __name__)


@usuario_bp.get("/usuarios/<tipo>")
def listar_usuarios(tipo):
    """Lista usuários por tipo."""

    resposta, status = UsuarioController.listar_usuarios(tipo)
    return jsonify(resposta), status


@usuario_bp.post("/usuarios/<tipo>")
def criar_usuario(tipo):
    """Cria um usuário do tipo informado."""

    dados = request.get_json(silent=True) or {}
    resposta, status = UsuarioController.criar_usuario(tipo, dados)
    return jsonify(resposta), status