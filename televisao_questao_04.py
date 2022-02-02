#4) Utilizando o que aprendemos com funções, modifique o construtor da 
# classe Televisão de forma que min e max sejam parâmetros opcionais, 
# onde min vale 2 e max vale 14, caso outro valor não seja passado.

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
