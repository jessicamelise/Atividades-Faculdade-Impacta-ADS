#Faça um programa que recebe dois valores quaisquer, armazenando-os nas variáveis v1 e v2, 
# e em seguida troca os valores de v1 e v2 e imprime os valores trocados.

# A saída devera ser as duas entradas impressas na ordem inversa. Serão impressos os valores 
# armazenados em v1 e v2, nessa ordem, mas o programa deverá ter trocado os valores recebidos 
# em cada variável. (o valor originalmente em v1 passa para v2 e vice-versa).


v1 = input("Primeiro número: ")
v2 = input("Segundo número: ")
v3 = v1
v1 = v2
v2 = v3
print('valor em v1:', v1)
print('valor em v2:', v2)