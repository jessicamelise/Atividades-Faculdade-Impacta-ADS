# Escreva um programa em Python 3 para somar os n primeiros termos da seguinte série:

########################################
#           1     1     1     1        #
# S = -1 + --- - --- + --- - --- + ... #
#           2     3     4     5        #
########################################

# DICA 1: n é o número de termos, então n = 3 significa que apenas as três primeiras 
# frações serão consideradas: -1, +1/2 e -1/3. Lembrando que o -1 pode ser escrito 
# como -1/1, sem alterar o resultado pois qualquer número dividido por 1 é igual 
# ao próprio número.

# DICA 2: Você pode criar uma variável para calcular as frações: 1/1, 1/2, 1/3, 1/4, ... 
# e depois usar uma estrutura de decisão interna ao laço de repetição para decidir se 
# aquela fração deve ser somada ou subtraída. Observe que a decisão de somar ou subtrair 
# está associada à posição dos números: o 1°, 3°, 5°, 7°, ... são subtraídos e o 2°, 4°, 
# 6°, 8°, ... são somados.

# A entrada será um número natural n > 0.
# A saída deve ser uma unica linha contendo apenas o resultado da somatória formatado 
# para exibir 6 casas de precisão.

numero = int(input("Número: "));
cont = 1;
soma = 0;
subtracao = 0;

for n in range(cont, numero+1):
    if n%2 == 0:
        soma = soma + (1/n);
    else:
        subtracao = subtracao - (1/n);

total = soma+subtracao;

print( "%.6f" % total);