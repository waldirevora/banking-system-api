from app.models.usuario_model import UsuarioModel


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