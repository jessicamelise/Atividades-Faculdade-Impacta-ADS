# Imagine que você fora contratado para fazer um programa para uma loja de tintas, com o objetivo de 
# calcular quantas latas de tinta são necessárias para pintar uma determinada área e calcular o preço final da compra.
# A loja trabalha com latas de tinta de:
# 24 litros, vendidas a R$91,00 cada e,
# 5.4 litros, vendidas a R$23,00 cada.
# Sabe-se ainda que cada litro de tinta cobre uma superfície de 7 metros quadrados.
# Faça um programa que receba o valor da área a ser pintada em metros quadrados, calcule e imprima:
# a) A quantidade de latas de tinta e o preço final, considerando apenas latas de 24 litros.
# b) A quantidade de latas de tinta e o preço final, considerando apenas latas de 5.4 litros.
# c) A quantidade de latas de tinta e o preço final, considerando ambas as latas, de 24 e 5.4 litros.
# Observação: O objetivo no item C) não é otimizar o custo nem a quantidade de tinta, apenas comprar o maior 
# número possível de latas de tintas maiores, isto é, o maior número inteiro, e comprar o restante em latas de tinta menores.

# Exemplo: Considerando latas de 10 e 3 litros
# se eu precisar de 28 litros de tinta, devo comprar 2 de 10 litros e 3 de 3 litros
# se eu precisar de 51 litros de tinta, devo comprar 5 de 10 litros e 1 de 3 litros
# se eu precisar de 5 litros de tinta, devo comprar 0 de 10 litros e 2 de 3 litros

# Formato de entrada: A entrada será um número real positivo não nulo.
# Formato de saída: A saída deverá ser impressa conforme o exemplo abaixo:
#################################################################
# a) 2 lata(s) de 24 litros: R$ 182.00                          #
# b) 6 lata(s) de 5.4 litros: R$ 138.00                         #
# c) 1 lata(s) de 24 litros e 1 lata(s) de 5.4 litros: R$ 114.00#
#################################################################
# Com o número de latas impresso como número inteiro e o custo final impresso com duas casas decimais.
# Dicas:
# Usem as funções math.ceil(n) e math.floor(n) para arredondar os números para os inteiros acima e abaixo de n, respectivamente.
# Usem o método str.format() para formatar a string e definir o número de casas decimais dos números a serem impressos.

import math;

metrosQuadrados = float(input("metros quadrados: "));

litrosNecessarios = metrosQuadrados/7;

vinteQuatro = litrosNecessarios/24;
priceVinteQuatro = "%.2f" %(math.ceil(vinteQuatro)* 91.00);

cinco_quatro = litrosNecessarios/5.4;
priceCinco_Quatro = "%.2f" %(math.ceil(cinco_quatro)* 23.00);

minVinteQuatro = math.floor(vinteQuatro);
restMetrosQuadrados = metrosQuadrados - (minVinteQuatro*(24*7));
minPriceVinteQuatro = minVinteQuatro * 91.00;
minCinco_quatro = (restMetrosQuadrados/7)/5.4;
minPriceCinco_quatro = math.ceil(minCinco_quatro) * 23.00;
total = "%.2f" %(minPriceVinteQuatro + minPriceCinco_quatro);


print("a) {} lata(s) de 24 litros: R$ {}".format(math.ceil(vinteQuatro), priceVinteQuatro));
print("b) {} lata(s) de 5.4 litros: R$ {}".format(math.ceil(cinco_quatro), priceCinco_Quatro));
print("c) {} lata(s) de 24 litros e {} lata(s) de 5.4 litros: R$ {}".format(minVinteQuatro, math.ceil(minCinco_quatro), total));