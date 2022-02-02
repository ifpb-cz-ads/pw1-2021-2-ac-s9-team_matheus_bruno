#1) Adicione os atributos tamanho e marca à classe Televisão. 
# Crie dois objetos Televisão e atribua tamanhos e marcas diferentes. 
# Depois, imprima o valor desses atributos de forma a confirmar a independência 
# dos valores de cada instância (objeto).

from .classes.Televisao.televisao_questao_01 import Televisão

tv_01 = Televisão()
tv_01.tamanho = 50
tv_01.marca = "LG"

tv_02 = Televisão()
tv_02.tamanho = 30
tv_02.marca = "PHILIPS"

print(f"----------Primeira TV----------\nTamanho: {tv_01.tamanho}\nMarca: {tv_01.marca}\n")
print(f"----------Segunda TV----------\nTamanho: {tv_02.tamanho}\nMarca: {tv_02.marca}")
