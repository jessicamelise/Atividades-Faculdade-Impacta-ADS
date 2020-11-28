# Dada uma lista de compras, queremos saber qual é o item mais caro da lista.

# Formato de entrada: Uma sequência de itens, cada um descrito numa linha. Cada item contém 
# um código de produto (um número inteiro), a quantidade do produto e o preço unitário (um float). 
# A sequência termina com um item com 0 como código do produto. Este último item não deve ser 
# considerado para o cálculo.

# Formato de saída: O código do produto, a quantidade e o preço do item mais caro, escrito com 
# duas casas decimais. Se a sequência não tiver itens deve se escrever "nao tem compras". 
# Se houver mais de um item com preço total mais caro, deverão ser impressos os dados do 
# primeiro deles na lista de compras.

# OBS: para finalizar a lista use "0 0 0"

buyList = []

while (True):
   addItem = input("Itens separado por espaço: ");
   if addItem == "0 0 0":
       break;
   else:
       separateItem = addItem.split();
       totalPrice = int(separateItem[1])*float(separateItem[2]);
       buyList.append(int(separateItem[0]));
       buyList.append(int(separateItem[1]));
       buyList.append(totalPrice);

def findMaxPrice(arr):
   newList = [];
   for position in range(2, len(arr), 3):
      newList.append(arr[position]);
   maxNum = max(newList);
   return arr.index(maxNum);

if len(buyList) == 0:
   print("nao tem compras");
else:
   value = findMaxPrice(buyList);
   print("Item mais caro");
   print("Codigo: {}".format(buyList[value-2]));
   print("Quantidade: {}".format(buyList[value-1]));
   print("Custo: %.2f" % buyList[value]);