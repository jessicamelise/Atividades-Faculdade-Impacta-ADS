# Você foi contratado para escrever um programa simples de gerenciamento de pedidos para a pizzaria 
# do seu bairro. A gerente da pizzaria precisa que seus atendentes possam adicionar e remover 
# pedidos, além de exibir a lista atual de pedidos. Você então decidiu implementar uma primeira 
# versão do programa, para testar a sua funcionalidade, e para isso a interação com o usuário se 
# dará por linha de comando, sem uma interface gráfica por hora. O seu programa deverá aceitar 
# alguns comandos pré-definidos e executar a ação correspondente.

# Formato de entrada: Cada ação realizada no programa será dada em uma linha diferente, sendo a 
# entrada composta por um comando seguido de um valor separado por espaço quando necessário, 
# referente ao número do pedido. As possíveis entradas são:
# -ajuda: exibe um menu com a lista dos comandos existentes
# -sair: encerra o programa
# -exibir: exibe a lista atual de pedidos, caso a lista esteja vazia, exibe: "sem pedidos"
# -novo #pedido: adiciona o #pedido à lista de pedidos e exibe a mensagem de confirmação: "pedido #pedido adicionado"
# -cancela #pedido: remove o #pedido da lista de pedidos e exibe a mensagem de confirmação: "pedido #pedido removido", 
# caso o pedido não exista na lista, deve exibir a mensagem "pedido #pedido inexistente"

# Formato de saída: A saída devera conter o resultado correspondete aos comandos dados pelo usuário. 
# O comando ajuda deverá exibir o seguinte texto ao usuário:
# -----------------------------------
# Pizzaria 0.1 - menu de comandos
# -----------------------------------
# - ajuda: exibe o menu de ajuda
# - sair: encerra o programa
# - exibir: exibe a lista de pedidos
# - novo #pedido: adiciona o #pedido
# - cancela #pedido: remove o #pedido
#-----------------------------------

orderList = [];
checkTrue = False;
def helpInformation():
    print("-----------------------------------");
    print("Pizzaria 0.1 - menu de comandos");
    print("-----------------------------------");
    print("- ajuda: exibe o menu de ajuda");
    print("- sair: encerra o programa");
    print("- exibir: exibe a lista de pedidos");
    print("- novo #pedido: adiciona o #pedido");
    print("- cancela #pedido: remove o #pedido");
    print("-----------------------------------");

while (True):
    instruction = input("Ação: ");
    separate = instruction.split();
    if instruction == "ajuda":
        helpInformation();
    elif instruction == "exibir":
        if len(orderList) == 0:
            print("sem pedidos");
        else:
            print(" ".join(orderList));
    elif separate[0] == "novo":
        orderList.append(separate[1]);
        print("pedido {} adicionado".format(separate[1]));
    elif separate[0] == "cancela":
        for order in orderList:
            if order == separate[1]:
                checkTrue = True;
        if checkTrue:
            orderList.remove(separate[1]);
            print("pedido {} removido".format(separate[1]));
            checkTrue = False;
        else:
            print("pedido {} inexistente".format(separate[1]));
    else:
        break;