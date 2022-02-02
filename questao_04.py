#4) Utilizando o que aprendemos com funções, modifique o construtor da 
# classe Televisão de forma que min e max sejam parâmetros opcionais, 
# onde min vale 2 e max vale 14, caso outro valor não seja passado.


from .classes.Televisao.televisao_questao_04 import Televisão

tv_01 = Televisão(7)
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
