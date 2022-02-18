#6) Altere o programa de forma que a mensagem saldo insuficiente seja 
# exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível (classe Conta).


from classes.Conta.conta_questao_06 import Conta

print("-------Mandando saldo como pareâmetro-------")
cliente = Conta('Matheus', 11, 200)

print(cliente.resumo_conta())

print(f"Foi depositado: {cliente.deposito(100)}\n")
print(cliente.resumo_conta())

print(f"\nFoi sacado: {cliente.saque(220)}\n Saldo disponível: {cliente.saldo}\n")
print(cliente.resumo_conta())
