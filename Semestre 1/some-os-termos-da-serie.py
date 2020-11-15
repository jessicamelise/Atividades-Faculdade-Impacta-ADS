# Escreva um programa em Python 3 para somar os n primeiros termos da seguinte série:

########################################
#          1     1     1     1         #
# S = 1 + --- + --- + --- + --- + ...  #
#          4     9     16    25        #
########################################

# DICA: Aqui todas as frações são somadas, mas como calcular o denominador? 
# Tente primeiro fazer a exibição apenas dos denominadores.

# Os denominaores são: 1, 4, 9, 16, 25, 36, .... qual a relação entre eles e a posição dos números?
# Compare com a posição: 1, 2, 3, 4, 5, 6, ....

# A entrada será um número natural n > 0.
# A saída deve ser uma unica linha contendo apenas o resultado da somatória formatado 
# para exibir 6 casas de precisão.

numero = int(input("Número: "));
cont = 1;
soma = 0;
for n in range(cont, numero+1):
   soma = soma + (1/(n**2));
print( "%.6f" % soma);

