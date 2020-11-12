# Na empresa em que você trabalha há muitos funcionários, e às vezes o depósito 
# do INSS é feito incorretamente para alguns deles pois é um processo manual 
# e portanto sujeito a erros. Com isso você decidiu propor a automação de tal 
# processo, para torná-lo mais rápido e reduzir a chance de erros. Escreva um 
# programa que receba o salário base de um funcionário e calcule qual a contribuição 
# devida ao INSS, dada de acordo com a seguinte tabela:

# -------------------------------------------------
# | Salário de Contribuição (R$) | Alíquota       |
# -------------------------------------------------
# | Até R$ 1.751,81              | 8%             |
# -------------------------------------------------
# | De R$ 1.751,82 a R$ 2.919,72 | 9%             |
# -------------------------------------------------
# | De R$ 2.919,73 a R$ 5.839,45 | 11%            |
# -------------------------------------------------

# Lembrando que esta tabela define um teto para o salário considerado, portanto salários 
# maiores que o salário máximo serão descontados de um valor fixo e igual a 11% do valor do teto.

# A entrada será um número real, representando o salário base do funcinário.
# ex. formula porcentagem: 160 x 25% = 160 (25/100) = 160 x 0,25 = 40

salario = float(input("Insira seu sálario: "))
if salario <= 1751.81:
   desc = salario * (8/100)
   print("Desconto do INSS: R$ {:.2f}".format(desc))
elif salario > 1751.81 and salario <= 2919.72:
   desc = salario * (9/100)
   print("Desconto do INSS: R$ {:.2f}".format(desc))
elif salario > 2919.72 and salario < 5839.45:
   desc = salario * (11/100)
   print("Desconto do INSS: R$ {:.2f}".format(desc))
else:
   print("Desconto do INSS: R$ 642.34")