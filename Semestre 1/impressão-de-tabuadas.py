# Faça um programa de resolução de tabuada. O programa deve inicialmente receber 2 números 
# que indicam de quais números devem ser impressas a tabuada. Por exemplo, se forem 
# recebidos os valores 2 e 5, seu programa deve imprimir a tabuada de 2, 3, 4 e 5. 
# O programa só deve aceitar valores entre 1 e 9. Enquanto o usuário digitar valores que não 
# sejam esses, emita uma mensagem de erro.

# Formato de entrada: Dois números em 2 linhas distintas indicando o intervalos dos números das tabuadas.

# Formato de saída: As tabuadas dos números dentro do intervalo.

number1 = int(input("Número inicial: "));
while (number1 < 1 or number1 > 9):
   print("Insira um número inicial entre 1 e 9");
   number1 = int(input("Número inicial: "));

number2 = int(input("Número final: "));
while (number2 < 1 or number2 > 9):
   print("Insira um número final entre 1 e 9");
   number2 = int(input("Número final: "));

if number1 > number2:
   print("Nenhuma tabuada nesse intervalo");
else:
   while (number1 <= number2):
       for n in range(1, 10):
           print("{} x {} = {}".format(number1, n, number1*n));
       if number1 != number2:
           print();
       number1 += 1;
