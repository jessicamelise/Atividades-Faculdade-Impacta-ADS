# Escreva um programa que receba as notas e a presença de um aluno, calcule a 
# média e imprima a situação final do aluno.

# No semestre são feitas 3 provas, e faz-se a média ponderada com pesos 2, 2 e 3, respectivamente.
# Os critérios para aprovação são:
# 1 - Frequência mínima de 75%.
# 2 - Média final mínina de 6.0 (calculada com uma casa de precisão).

# E devem ser considerados os casos especiais descritos para a impressão dos resultados, 
# com uma mensagem personalizada para cada situação.

# DICA: calcular com uma casa de precisão está associado ao valor que será salvo na memória e 
# não à exibição da resposta, que deve seguir o formato especificado, independentemente de como 
# estamos salvando o valor na memória. Uma coisa é o cálculo e outra a apresentação do resultado.
# Ou seja, o valor da média deve ser arredondado para uma casa de precisão antes de serem feitas 
# as verificações que irão decidir se o aluno foi ou não aprovado. Para isso use a função round 
# do Python, que funciona como mostrado no exemplo a seguir.
# Essa função recebe 2 parâmetros, o primeiro é o número a ser arredondado e o segundo é o número 
# de casas decimais que queremos:
# round(3.765, 1)
# 3.8

# A entrada serão três números reais no intervalo de 0 a 10, representando as notas do aluno, 
# e um número real no intervalo de 0 a 1 representando a frequência.

nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))
frequencia = float(input("Frequencia: "))

def mediaP(nota, peso):
    return (nota/7)*peso

somaMedia = mediaP(nota1, 2) + mediaP(nota2, 2) + mediaP(nota3, 3)

porcentFreq = frequencia * 100

print("Frequencia: {}%".format(int(porcentFreq)))
print("Media: {}".format(round(somaMedia, 1)))

if int(porcentFreq) < 75:
    print("Aluno reprovado por faltas!")
elif int(porcentFreq) >= 75 and round(somaMedia,1) < 4:
    print("Aluno reprovado!")
elif int(porcentFreq) >= 75 and round(somaMedia,1) >= 4 and round(somaMedia,1) < 6:
    print("Aluno de rec!")
elif int(porcentFreq) >= 75 and round(somaMedia,1) >= 6 and round(somaMedia,1) <= 9:
    print("Aluno aprovado!")
else:
    print("Aluno aprovado com louvor!")