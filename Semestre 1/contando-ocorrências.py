# Escreva um programa que irá receber duas entradas: uma sequencia de caracteres e um único 
# caractere e irá contar quantas vezes o caractere aparece na sequencia. Você deve escrever 
# uma função que irá receber como parâmetros a sequencia e o caractere, e retornar o número de 
# ocorrências pedido. No código principal do programa, faça a leitura dos dados de entrada 
# (input's), chame a sua função para contar o número de ocorrências, e em seguida imprima o 
# resultado pedido.
# OBS: Não é permitido o uso do .count() para realizar a contagem. 
# DICA: A ideia é criar uma função que faça a mesma coisa que o .count(), portanto você pode 
# usar o .count() para comparar os seus resultados e validar a sua função. Para fazer a contagem, 
# faça um laço (for ou while) iterando sobre a sequência e criei um contador para guardar quantas 
# vezes o caractere foi encontrado.

# Formato de entrada: A entrada conterá duas strings, sendo a primeira a sequências de caracteres 
# e a segunda o caractere que deve ser buscado. 
  
# Formato de saída: apresentar o seguinte texto:
# Caso o caractere seja encontrado pelo menos 1 vez na sequência: O caractere buscado ocorre <quantidade> vezes na sequencia.
# E se o caractere não for encontrado na sequência: Caractere nao encontrado.

sequence = input("Sequencia: ");
unique = input("Caracter: ");

def counter(caracters, caracter):
   count = 0;
   for each in caracters:
       if each == caracter:
           count += 1;
   if count == 0:
       print("Caractere nao encontrado.");
   else:
       print("O caractere buscado ocorre {} vezes na sequencia.".format(count));

counter(sequence, unique);