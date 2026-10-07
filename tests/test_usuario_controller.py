from unittest.mock import patch

from app.controllers.usuario_controller import UsuarioController


def test_listar_usuarios():
    """Valida a listagem de usuários."""

    usuarios = [{"id": 1, "nome_completo": "João"}]

    with patch(
        "app.controllers.usuario_controller.UsuarioModel.listar",
        return_value=usuarios,
    ):
        resposta, status = UsuarioController.listar_usuarios("fisica")

    assert status == 200
    assert resposta["usuarios"] == usuarios


def test_listar_tipo_invalido():
    """Valida o tratamento de um tipo de usuário inválido."""

    with patch(
        "app.controllers.usuario_controller.UsuarioModel.listar",
        side_effect=ValueError("Tipo de usuário inválido."),
    ):
        resposta, status = UsuarioController.listar_usuarios("invalido")

    assert status == 400
    assert resposta["erro"] == "Tipo de usuário inválido."


def test_criar_usuario():
    """Valida a criação de uma Pessoa Física."""

    dados = {
        "renda_mensal": 5000,
        "idade": 30,
        "nome_completo": "Teste",
        "celular": "9999-9999",
        "email": "teste@example.com",
        "categoria": "Categoria A",
        "saldo": 1000,
    }

    with patch(
        "app.controllers.usuario_controller.UsuarioModel.criar",
        return_value=4,
    ):
        resposta, status = UsuarioController.criar_usuario("fisica", dados)

    assert status == 201
    assert resposta["id"] == 4


def test_criar_usuario_com_dados_incompletos():
    """Valida a rejeição de dados incompletos."""

    resposta, status = UsuarioController.criar_usuario(
        "fisica",
        {"nome_completo": "Teste"},
    )

    assert status == 400
    assert resposta["erro"] == "Dados obrigatórios não informados."

def test_saque_pessoa_fisica_acima_do_limite():
    """Valida o limite de saque da Pessoa Física."""

    usuario = {
        "nome_completo": "Teste PF",
        "saldo": 5000,
    }

    with patch(
        "app.controllers.usuario_controller.UsuarioModel.buscar_por_id",
        return_value=usuario,
    ):
        resposta, status = UsuarioController.realizar_saque(
            "fisica",
            1,
            1500,
        )

    assert status == 400
    assert resposta["erro"] == "Saque não permitido."


def test_saque_pessoa_juridica():
    """Valida saque permitido para Pessoa Jurídica."""

    usuario = {
        "nome_fantasia": "Teste PJ",
        "saldo": 5000,
    }

    with patch(
        "app.controllers.usuario_controller.UsuarioModel.buscar_por_id",
        return_value=usuario,
    ), patch(
        "app.controllers.usuario_controller.UsuarioModel.atualizar_saldo"
    ) as atualizar_saldo:
        resposta, status = UsuarioController.realizar_saque(
            "juridica",
            1,
            1500,
        )

    assert status == 200
    assert resposta["saldo"] == 3500
    atualizar_saldo.assert_called_once_with("juridica", 1, 3500)


def test_realizar_extrato():
    """Valida o extrato de uma Pessoa Física."""

    usuario = {
        "nome_completo": "Teste PF",
        "saldo": 2500,
    }

    with patch(
        "app.controllers.usuario_controller.UsuarioModel.buscar_por_id",
        return_value=usuario,
    ):
        resposta, status = UsuarioController.realizar_extrato(
            "fisica",
            1,
        )

    assert status == 200
    assert resposta == {
        "nome": "Teste PF",
        "saldo": 2500,
    }