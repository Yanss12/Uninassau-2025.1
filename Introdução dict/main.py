from agenda import adicionar_contato, exibir_contatos, atualizar_telefone
from pprint import pprint

while True:
    opção = int(input('\nInforme sua opção: (1 - Adicionar Contato): (2 - Exibir contatos): (3 - Atualizar contato): '))

    if opção == 1:
        # Receber os dados
        nome = input('Informe o nome: ')
        telefone = input('informe o telefone: ')
        email = input('Informe o email: ')

        # Organizar em um dicionario
        contato = {
            'nome': nome,
            'telefone': telefone,
            'email': email,
        }

        adicionar_contato(contato)

    elif opção == 2:
        agenda = exibir_contatos()
        pprint(agenda)

    elif opção == 3:
        contato = input('Informe o contato a ser atualizado: ')
        novo_numero = input('Informe o novo numero: ')

        # Chamado da função
        status = atualizar_telefone(contato, novo_numero)

        if status:
            print('Contato atualizado com sucesso')
        else:
            print('Contato não encontrado')