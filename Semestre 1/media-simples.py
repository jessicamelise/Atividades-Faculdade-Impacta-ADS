# Escreva um programa em Python3 que receba 4 valores, referentes à altura de 4 pessoas, 
# calcule e imprima a média desses valores.

#As entradas serão números reais positivos não nulos. Não é necessário fazer nenhum tipo de 
# validação dos dados de entrada

v1 = float(input("Primeira altura: "))
v2 = float(input("Segunda altura: "))
v3 = float(input("Terceira altura: "))
v4 = float(input("Quarta altura: "))
calculo = (v1+v2+v3+v4)/4
print("A media das alturas é", calculo)