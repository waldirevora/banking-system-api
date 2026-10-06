from app.models.cliente import Cliente


class PessoaJuridica(Cliente):
    """Representa um cliente Pessoa Jurídica."""

    LIMITE_SAQUE = 5000.00

    def __init__(self, nome_fantasia, saldo=0.0):
        self.nome_fantasia = nome_fantasia
        self.saldo = saldo

    def sacar_dinheiro(self, valor):
        """Realiza saque dentro do limite da Pessoa Jurídica."""

        if valor <= 0:
            return False

        if valor > self.LIMITE_SAQUE or valor > self.saldo:
            return False

        self.saldo -= valor
        return True

    def realizar_extrato(self):
        """Retorna o saldo atual da Pessoa Jurídica."""

        return {
            "nome": self.nome_fantasia,
            "saldo": self.saldo,
        }