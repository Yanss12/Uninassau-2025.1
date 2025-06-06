from biblioteca_func import *
import pprint

while True:
    opção_menu = int(input("\nInforme sua opção: (1 - Gerenciar livros) (2 - Gerenciar usuarios): "))
    
    if opção_menu == 1:
        opcao_livro = int(input("\nInforme sua opção: (1 - Adicionar livro) (2 - Exibir catalogo) (3 - Buscar titulo): "))

        if opcao_livro == 1:
            id_livro = gerar_id()
            titulo = input("Informe o titulo: ")
            autor = input("informe o nome do autor: ")
            ano_publicacao = int(input("informe o ano de publicação: "))
            print(f"o id do livro {titulo} é {id_livro}")

            livros = {
                "id" : id_livro,
                "titulo" : titulo,
                "autor" : autor,
                "ano_publicacao" : ano_publicacao
            }

            adicionar_livro(livros)

        elif opcao_livro == 2:
            catalogo_livros = listar_livros()
            pprint.pprint(catalogo_livros)
        
        elif opcao_livro == 3:
            titulo = input("Informe o titulo: ")
            resultado = buscar_livro_por_titulo(titulo)
            print(resultado)

    elif opção_menu == 2:
        opcao_usuario = int(input("\nInforme sua opção: (1 - Adicionar cliente) (2 - Exibir clientes) (3 - buscar cliente)"))