from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "banking.db"
SCHEMA_PATH = BASE_DIR / "schema.sql"


def initialize_database():
    """Cria e popula o banco SQLite usando o script fornecido no desafio."""

    if DATABASE_PATH.exists():
        print("O banco de dados já existe. Nenhuma alteração foi realizada.")
        return

    sql_script = SCHEMA_PATH.read_text(encoding="utf-8")

    with sqlite3.connect(DATABASE_PATH) as connection:
        connection.executescript(sql_script)

    print(f"Banco de dados criado em: {DATABASE_PATH}")


if __name__ == "__main__":
    initialize_database()