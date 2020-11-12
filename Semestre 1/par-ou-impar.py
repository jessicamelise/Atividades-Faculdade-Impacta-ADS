# Escreva um programa em Python 3 que receba um número inteiro não negativo e 
# exiba na dela uma mensagem dizendo se ele é par ou ímpar.

# A entrada será um número inteiro não negativo (pode ser nulo). Não é necessário fazer 
# nenhum tipo de validação.

numero = int(input("Insira um número inteiro não negativo: "))
if numero%2==0:
   print("O numero {} eh par!".format(numero))
else:
   print("O numero {} eh impar!".format(numero))