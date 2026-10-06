from app.models.cliente import Cliente


class PessoaFisica(Cliente):
    """Representa um cliente Pessoa Física."""

    LIMITE_SAQUE = 1000.00

    def __init__(self, nome_completo, saldo=0.0):
        self.nome_completo = nome_completo
        self.saldo = saldo

    def sacar_dinheiro(self, valor):
        """Realiza saque dentro do limite da Pessoa Física."""

        if valor <= 0:
            return False

        if valor > self.LIMITE_SAQUE or valor > self.saldo:
            return False

        self.saldo -= valor
        return True

    def realizar_extrato(self):
        """Retorna o saldo atual da Pessoa Física."""

        return {
            "nome": self.nome_completo,
            "saldo": self.saldo,
        }