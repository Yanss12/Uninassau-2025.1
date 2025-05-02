from menu_estoque import menu
from estoque import *

while True:
    opcao_escolhida = menu()

    if opcao_escolhida == 1:
        descricao = input('Informe a descrição: ')
        quantidade = int(input('Informe a quantidade: '))
        valor = float(input('Informe o valor: '))
        # Passando os valores para a função
        cadastrar_produto(descricao, quantidade, valor)

    elif opcao_escolhida == 2:
        estoque_atual = exibir_estoque()
        print(estoque_atual)

    elif opcao_escolhida == 3:
        break

    else:
        print('Opção invalida')
