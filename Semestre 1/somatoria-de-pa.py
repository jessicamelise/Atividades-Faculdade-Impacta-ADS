# Escreva um programa em Python 3 que receba dois números inteiros representando uma progressão 
# aritmética começando sempre em 1 e calcule a sua somatória. 

# O primeiro é a razão R da PA e o segundo é o último número N da série.
# Exemplo: R = 3 e N = 22 resulta na seguinte série: 1, 4, 7, 10, 13, 16, 19, 22

# DICA: Comece fazendo um laço de repetição para percorrer e exibir um número da série de 
# cada vez, até que você consiga exibir todos os números do exemplo acima corretamente. 
# Em seguida crie uma variável acumuladora para ir somando cada um desses números de maneira 
# a "acumular" o resultado final. (lembre-se depois de apagar ou comentar todos os prints 
# que não forem necessários para que a saída na tela fique como o enunciado pede!)

# A entrada deve ser dois números inteiros positivos, não é necessário validar a entrada

razao = int(input("Número da Razão: "));
ultimoNum = int(input("Último número da série: "));
cont = 1;
soma = 0;
for numero in range(cont, ultimoNum+1, razao):
   soma = soma + numero;
print("A somatoria da PA é: {}".format(soma));