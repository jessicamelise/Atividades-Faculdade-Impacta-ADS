# Escreva um programa em Python3 que receba quatro números reais (a, b, c, d) e reproduza as seguintes expressões algébricas:
#     a² + 3 . b 
# i) ------------ + d
#         c
#                           d²
# ii) log10(a) + e ̄ ᵇ⁄ᶜ - -----
#                           π
#
#       ³√a² . b ¹/³ + c . d
# iii) -----------------------
#          a + b + c + d
#
#       (a + b) . (c + d)
# iv) ----------------------
#          a . b . c . d
#
#     a² + b²        c² + d²
# v) ----------  -  ---------
#      c . d          a . b
#
# vi) O quadrado da soma de (a, b, c, d)
# vii) A soma dos quadrados de (a, b, c, d)
# viii) A raiz cúbica do produto de (a, b, c, d)

# DICA 1: A única função que vocês precisam usar do módulo de mátemática é a função log (ou log10). 
# DICA 2: Usem os valores do número Pi e do Número de Euler (e) também do módulo de matemática.
# DICA 3: Não existe (até onde eu sei) uma função para calcular a raiz cúbica no Python, e isso tampouco 
# é necessário, pois toda e qualquer raiz pode ser reescrita como um expoente fracionário. Pra aqueles 
# que não lembram como fazer isso, recomendo o seguinte material de estudo da Khan Academy: 
# https://pt.khanacademy.org/math/algebra/rational-exponents-and-radicals/rational-exponents-intro/v/rewriting-roots-as-rational-exponents

# Formato de entrada: As entradas poderão ser quaisquer números reais, positivos ou negativos mas não nulos.
# Formato de saída: Durante o cálculo, o valor final calculado para cada item deve ser arredondado para 4 casas decimais, usando a função round.

import math;

a = float(input("Número a: "));
b = float(input("Número b: "));
c = float(input("Número c: "));
d = float(input("Número d: "));

print("i) {}".format(round((a**2+3*b)/c+d, 4)));
print("ii) {}".format(round(math.log10(a)+ math.e**(-b/c) - d**2/math.pi, 4)));
print("iii) {}".format(round((math.pow(a**2,(1/3))*b**(1/3)+c*d)/(a+b+c+d), 4)));
print("iv) {}".format(round(((a+b)*(c+d))/(a*b*c*d), 4)));
print("v) {}".format(round(((a**2 + b**2)/(c*d))-((c**2+d**2)/(a*b)), 4)));
print("vi) {}".format(round((a+b+c+d)**2, 4)));
print("vii) {}".format(round((a**2)+(b**2)+(c**2)+(d**2), 4)));
print("viii) {}".format(round((a*b*c*d)**(1/3), 4)));