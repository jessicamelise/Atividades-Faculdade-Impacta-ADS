# Escreva um programa em Python3 que receba um número real positivo e não nulo, calcule e imprima 
# o resultado das seguintes operações aritméticas (n é o número recebido e e é o número de Euler):

# i) n²
# ii) nᵉ
# iii) √n
# iv) ³√n
# v) ᶰ√n
# vi) e . n
# vii) π / n
# viii) log7 n 
# ix) loge n
# x) logn n

# DICA 1: A única função que vocês precisam usar do módulo de mátemática é a função log. 
# DICA 2: Usem os valores do número Pi e do Número de Euler (e) também do módulo de matemática.
# DICA 3: Não existe (até onde eu sei) uma função para calcular a raiz cúbica no Python, e isso 
# tampouco é necessário, pois toda e qualquer raiz pode ser reescrita como um expoente fracionário. 
# Pra aqueles que não lembram como fazer isso, recomendo o seguinte material de estudo da Khan Academy: 
# https://pt.khanacademy.org/math/algebra/rational-exponents-and-radicals/rational-exponents-intro/v/rewriting-roots-as-rational-exponents

import math;

numero = float(input("Número: "));
print("i) {}".format(numero**2));
print("ii) {}".format(numero**math.e));
print("iii) {}".format(math.sqrt(numero)));
print("iv) {}".format(numero**(1/3)));
print("v) {}".format(numero**(1/numero)));
print("vi) {}".format(math.e * numero));
print("vii) {}".format(math.pi/numero));
print("viii) {}".format(math.log(numero,7)));
print("ix) {}".format(math.log(numero,math.e)));
print("x) {}".format(math.log(numero,math.pi)));