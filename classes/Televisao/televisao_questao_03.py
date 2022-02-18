#3) Modifique a classe Televisão de forma que, se pedirmos para mudar o canal 
# para baixo, além do mínimo, ela vá para o canal máximo. Se mudarmos para cima, 
# além do canal máximo, que volte ao canal mínimo. Exemplo:

#> > > tv=Televisão(2,10)
#> > > tv.muda_canal_para_baixo()
##> > > tv.canal
#10
#> > > tv.muda_canal_para_cima()
#> > > tv.canal
#2

class Televisão:
    def __init__(self,canal_inicial, canal_min, canal_max):
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
