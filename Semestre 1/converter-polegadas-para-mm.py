# Faça um programa em Python3 que receba um valor em polegadas, converta e imprima o resultado em milímetros.

# A entrada será um número real

# multiplique o valor da polegada por 25.4 para saber o mm

pol = float(input("Insira o valor em polegadas: "))
mm = pol * 25.4
print("{} polegada(s) é o mesmo que {} mm".format(pol, mm))