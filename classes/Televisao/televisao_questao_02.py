#2) Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe T
# elevisão de forma a receber o canal inicial em seu construtor.

class Televisão:
    def __init__(self, canal_inicial):
        self.canal_inicial = canal_inicial
        self.tamanho = 30
        self.marca = "Century"

