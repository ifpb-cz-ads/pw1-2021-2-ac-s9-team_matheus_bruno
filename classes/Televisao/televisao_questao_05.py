#5) Utilizando a classe Televisão modificada no exercício anterior, crie duas instâncias 
# (objetos), especificando o valor de min e max por nome.

class Televisão:
    def __init__(self,canal_inicial, canal_min=2, canal_max=14):
        self.canal_inicial = canal_inicial
        self.canal_min = canal_min
        self.canal_max = canal_max

    def muda_canal_para_baixo(self):
        if self.canal_inicial-1 >= self.canal_min:
            return self.canal_inicial - 1
        else:
            return self.canal_max

    def muda_canal_para_cima(self):
        if self.canal_inicial+1 <= self.canal_max:
            return self.canal_inicial + 1
        else:
            return self.canal_min