#2) Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe Televisão de forma a receber 
#o canal inicial em seu construtor.

from classes.Televisao.televisao_questao_02 import Televisão

tv_01 = Televisão(7)
tv_01.tamanho = 50
tv_01.marca = "LG"

tv_02 = Televisão(5)
tv_02.tamanho = 30
tv_02.marca = "PHILIPS"

print(f"----------Primeira TV----------\nTamanho: {tv_01.tamanho}\nMarca: {tv_01.marca}\nCanal inicial: {tv_01.canal_inicial}\n")
print(f"----------Segunda TV----------\nTamanho: {tv_02.tamanho}\nMarca: {tv_02.marca}\nCanal inicial: {tv_02.canal_inicial}")
