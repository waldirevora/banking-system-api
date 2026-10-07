from pathlib import Path
import sqlite3


DATABASE_PATH = (
    Path(__file__).resolve().parents[2] / "database" / "banking.db"
)

TABELAS = {
    "fisica": "pessoa_fisica",
    "juridica": "pessoa_juridica",
}


class UsuarioModel:
    """Realiza operações de usuários no banco SQLite."""

    @staticmethod
    def _conectar():
        """Abre uma conexão com o banco configurada para retornar registros por nome."""

        connection = sqlite3.connect(DATABASE_PATH)
        connection.row_factory = sqlite3.Row
        return connection

    @classmethod
    def listar(cls, tipo):
        """Lista os usuários do tipo informado."""

        tabela = TABELAS.get(tipo)

        if tabela is None:
            raise ValueError("Tipo de usuário inválido.")

        with cls._conectar() as connection:
            registros = connection.execute(
                f"SELECT * FROM {tabela}"
            ).fetchall()

        return [dict(registro) for registro in registros]

    @classmethod
    def criar(cls, tipo, dados):
        """Cria um usuário no banco e retorna seu identificador."""

        if tipo == "fisica":
            query = """
                INSERT INTO pessoa_fisica
                (renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            valores = (
                dados["renda_mensal"],
                dados["idade"],
                dados["nome_completo"],
                dados["celular"],
                dados["email"],
                dados["categoria"],
                dados["saldo"],
            )

        elif tipo == "juridica":
            query = """
                INSERT INTO pessoa_juridica
                (faturamento, idade, nome_fantasia, celular, email_corporativo, categoria, saldo)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            valores = (
                dados["faturamento"],
                dados["idade"],
                dados["nome_fantasia"],
                dados["celular"],
                dados["email_corporativo"],
                dados["categoria"],
                dados["saldo"],
            )

        else:
            raise ValueError("Tipo de usuário inválido.")

        with cls._conectar() as connection:
            cursor = connection.execute(query, valores)
            connection.commit()

        return cursor.lastrowid

    @classmethod
    def buscar_por_id(cls, tipo, usuario_id):
        """Busca um usuário pelo identificador."""

        tabela = TABELAS.get(tipo)

        if tabela is None:
            raise ValueError("Tipo de usuário inválido.")

        with cls._conectar() as connection:
            registro = connection.execute(
                f"SELECT * FROM {tabela} WHERE id = ?",
                (usuario_id,),
            ).fetchone()

        return dict(registro) if registro else None

    @classmethod
    def atualizar_saldo(cls, tipo, usuario_id, saldo):
        """Atualiza o saldo de um usuário."""

        tabela = TABELAS.get(tipo)

        if tabela is None:
            raise ValueError("Tipo de usuário inválido.")

        with cls._conectar() as connection:
            connection.execute(
                f"UPDATE {tabela} SET saldo = ? WHERE id = ?",
                (saldo, usuario_id),
            )
            connection.commit()