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


from classes.Televisao.televisao_questao_03 import Televisão

tv_01 = Televisão(7, 2, 10)
tv_01.tamanho = 50
tv_01.marca = "LG"

tv_02 = Televisão(5, 1, 8)
tv_02.tamanho = 30
tv_02.marca = "PHILIPS"


print(f"----------Primeira TV----------\nTamanho: {tv_01.tamanho}\nMarca: {tv_01.marca}\nCanal inicial: {tv_01.canal_inicial}")
print(f"Canal mínimo: {tv_01.canal_min}\nCanal Máximo: {tv_01.canal_max}")
print(f"Canal para cima: {tv_01.muda_canal_para_cima()}")
print(f"Canal para baixo: {tv_01.muda_canal_para_baixo()}")


print(f"----------Segunda TV----------\nTamanho: {tv_02.tamanho}\nMarca: {tv_02.marca}\nCanal inicial: {tv_02.canal_inicial}")
print(f"Canal mínimo: {tv_02.canal_min}\nCanal Máximo: {tv_02.canal_max}")
print(f"Canal para cima: {tv_02.muda_canal_para_cima()}")
print(f"Canal para baixo: {tv_02.muda_canal_para_baixo()}")
