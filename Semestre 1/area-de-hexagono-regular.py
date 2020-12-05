# Escreva um programa em Python3 que peça o valor do lado de um hexágono regular, calcule e imprima sua área e seu perímetro.
# Sabemos que um hexágono regular é o polígono de 6 lados iguais e com todos os ângulos internos iguais entre si.
# Sabemos ainda que um hexágono regular de lado L é formado por 6 triângulos equiláteros de lado L,
# sendo a área de 1 triângulo equilátero de lado L dada por:
#      a² . √3 
# A = ---------
#         4
# Formato de entrada: A entrada poderá ser qualquer número real não negativo (maior ou igual a zero).
# Formato de saída: A saída deverá ser formatada conforme o exemplo a seguir:
######################################
# Lado do hexagono: <valor1> metros, #
# Area: <valor2> metros quadrados,   #
# Perimetro: <valor3> metros.        #
######################################
# Sendo valor 1, 2 e 3 respectivamente os valores do lado, da área e do perímetro do hexágono.
# Dica: Usem um print() para cada linha da resposta, evitem o '\n' no começo.

import math;

lado = float(input("Valor: "));

print("Lado do hexagono: {} metros,".format(lado));
print("Area: {} metros quadrados,".format((((lado**2)*(math.sqrt(3)))/4)*6));
print("Perimetro: {} metros.".format(lado*6));