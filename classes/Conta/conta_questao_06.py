#6) Altere o programa de forma que a mensagem saldo insuficiente seja exibida 
# caso haja tentativa de sacar mais dinheiro que o saldo disponível (classe Conta).

class Conta:
    def __init__(self, nome_cliente, numero, saldo=0):
        self.saldo = 0
        self.clientes = nome_cliente
        self.numero = numero
        self.saldo = saldo

    def resumo_conta(self):
        return f"Conta N°: {self.numero}\nSaldo: {self.saldo}"

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return valor
        else:
            return "Saldo insuficiente!"

    def deposito(self, valor):
        self.saldo += valor
        return valor
