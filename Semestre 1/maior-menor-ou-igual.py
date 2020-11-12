# Dados dois números inteiros A e B, exibir:
# - 'A é maior', se A for maior do que B;
# - 'B é maior', se B for maior do que A;
# - 'iguais', se os números forem iguais.

# As entradas para A e B deverão ser números inteiros

numeroA = int(input("Primeiro número(A): "))
numeroB = int(input("Segundo número(B): "))
if numeroA == numeroB:
   print("iguais")
elif numeroA > numeroB:
   print("A eh maior")
else:
   print("B eh maior")