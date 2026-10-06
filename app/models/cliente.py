from abc import ABC, abstractmethod


class Cliente(ABC):
    """Define as operações obrigatórias para os clientes do banco."""

    @abstractmethod
    def sacar_dinheiro(self, valor):
        """Realiza um saque respeitando as regras do tipo de cliente."""

        pass

    @abstractmethod
    def realizar_extrato(self):
        """Retorna as informações do extrato do cliente."""

        pass