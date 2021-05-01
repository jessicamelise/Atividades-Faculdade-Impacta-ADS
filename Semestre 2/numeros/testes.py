from numeros import *

# testando função eh_primo
primos = [2, 3, 5, 23, 29, 31, 37, 71, 73, 79, 83, 113, 127, 197, 257, 263, 269, 337, 347, 349]
nao_primos = [1, 4, 8, 10, 22, 24, 30, 48, 70, 77, 80, 84, 110, 125, 200, 225, 260, 270, 330, 345, 350]

print('primo')
for x in primos:
    print(x, eh_primo(x))

print('não é primo')
for x in nao_primos:
    print(x, eh_primo(x))

# testando função lista_primos
lista_teste_um_primos = lista_primos(10)
lista_teste_dois_primos = lista_primos(30)

print(lista_teste_um_primos)
for x in lista_teste_um_primos:
    print(x, eh_primo(x))

print(lista_teste_dois_primos)
for x in lista_teste_dois_primos:
    print(x, eh_primo(x))

# testando função conta_primos
lista_teste_um_conta_primo = [1,3,4,5,1,3,6,5]
lista_teste_dois_conta_primo = [1,3,4,5,1,3,6,5, 7, 13, 11, 12, 56, 11, 7, 1, 4, 3]

print(conta_primos(lista_teste_um_conta_primo), conta_primos(lista_teste_dois_conta_primo))

# testando função eh_armstrong
lista_teste_armstrong_um = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
lista_teste_armstrong_dois = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 150, 300, 350, 400]

for x in lista_teste_armstrong_um:
    print(x, eh_armstrong(x))

for x in lista_teste_armstrong_dois:
    print(x, eh_armstrong(x))

# testando função eh_quase_armstrong
lista_teste_quase_armstrong_um = [35, 75]
lista_teste_quase_armstrong_dois = [10, 11]

for x in lista_teste_quase_armstrong_um:
    print(x, eh_quase_armstrong(x))

for x in lista_teste_quase_armstrong_dois:
    print(x, eh_quase_armstrong(x))

# testando funçãao lista_armstrong
print(lista_armstrong(100))
print(lista_armstrong(1000))

# testando função eh_perfeito
lista_perfeito = [6, 28, 496, 8128]
lista_nao_perfeito = [2, 4, 10, 50, 80]

for x in lista_perfeito:
    print(x, eh_perfeito(x))

for x in lista_nao_perfeito:
    print(x, eh_perfeito(x))

# testando função lista_perfeito
print(lista_perfeitos(10))
print(lista_perfeitos(30))


