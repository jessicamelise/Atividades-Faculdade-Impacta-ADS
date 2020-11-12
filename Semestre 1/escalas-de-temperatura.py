# Faça um programa em Python3 que receba uma temperatura em Fahrenheit, calcule e 
# imprima o valor convertido para a escala Celsius e para a escala Kelvin, de 
# acordo com as equações de conversão abaixo:
# t_celsius = (t_fahrenheit - 32) * 5/9
# t_kelvin = t_celsius + 273.15

# A entrada será um número real n, com n >= -459.67. (o zero absoluto, ou 0K, é igual a -459.67°F)

# na temperatura Kelvin não se usa o termo grau. (Diz-se 250 Kelvin e não 250 graus Kelvin)

t_fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))

t_celsius = (t_fahrenheit - 32) * 5/9
t_kelvin = t_celsius + 273.15


print("Convertendo {} graus Fahrenheit temos: {} graus Celsius e {} Kelvin".format(t_fahrenheit, t_celsius, t_kelvin))
