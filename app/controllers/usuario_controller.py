from app.models.usuario_model import UsuarioModel
from app.models.pessoa_fisica import PessoaFisica
from app.models.pessoa_juridica import PessoaJuridica


class UsuarioController:
    """Controla as operações relacionadas aos usuários."""

    @staticmethod
    def listar_usuarios(tipo):
        """Retorna os usuários do tipo informado."""

        try:
            usuarios = UsuarioModel.listar(tipo)
            return {"usuarios": usuarios}, 200
        except ValueError as error:
            return {"erro": str(error)}, 400

    @staticmethod
    def criar_usuario(tipo, dados):
        """Cria um usuário após validar os dados obrigatórios."""

        campos_por_tipo = {
            "fisica": {
                "renda_mensal",
                "idade",
                "nome_completo",
                "celular",
                "email",
                "categoria",
                "saldo",
            },
            "juridica": {
                "faturamento",
                "idade",
                "nome_fantasia",
                "celular",
                "email_corporativo",
                "categoria",
                "saldo",
            },
        }

        campos_obrigatorios = campos_por_tipo.get(tipo)

        if campos_obrigatorios is None:
            return {"erro": "Tipo de usuário inválido."}, 400

        if not campos_obrigatorios.issubset(dados):
            return {"erro": "Dados obrigatórios não informados."}, 400

        usuario_id = UsuarioModel.criar(tipo, dados)

        return {"id": usuario_id}, 201
    
    @staticmethod
    def realizar_saque(tipo, usuario_id, valor):
        """Realiza um saque para o usuário informado."""

        if not isinstance(valor, (int, float)):
            return {"erro": "Valor de saque inválido."}, 400

        try:
            usuario = UsuarioModel.buscar_por_id(tipo, usuario_id)
        except ValueError as error:
            return {"erro": str(error)}, 400

        if usuario is None:
            return {"erro": "Usuário não encontrado."}, 404

        if tipo == "fisica":
            cliente = PessoaFisica(
                usuario["nome_completo"],
                usuario["saldo"],
            )
        else:
            cliente = PessoaJuridica(
                usuario["nome_fantasia"],
                usuario["saldo"],
            )

        if not cliente.sacar_dinheiro(valor):
            return {"erro": "Saque não permitido."}, 400

        UsuarioModel.atualizar_saldo(tipo, usuario_id, cliente.saldo)

        return {
            "mensagem": "Saque realizado com sucesso.",
            "saldo": cliente.saldo,
        }, 200

    @staticmethod
    def realizar_extrato(tipo, usuario_id):
        """Retorna o extrato do usuário informado."""

        try:
            usuario = UsuarioModel.buscar_por_id(tipo, usuario_id)
        except ValueError as error:
            return {"erro": str(error)}, 400

        if usuario is None:
            return {"erro": "Usuário não encontrado."}, 404

        if tipo == "fisica":
            cliente = PessoaFisica(
                usuario["nome_completo"],
                usuario["saldo"],
            )
        else:
            cliente = PessoaJuridica(
                usuario["nome_fantasia"],
                usuario["saldo"],
            )

        return cliente.realizar_extrato(), 200