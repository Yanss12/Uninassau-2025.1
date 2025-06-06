from biblioteca_func import *
import pprint

while True:
    opção = int(input("\nInforme sua opção: (1 - Adicionar livro) (2 - Exibir catalogo) (3 - Buscar titulo): "))

    if opção == 1:
        #receber os dados
        titulo = input("Informe o titulo: ")
        autor = input("informe o nome do autor: ")
        ano_publicacao = int(input("informe o ano de publicação: "))
        id_livro = gerar_id()

        livros = {
            "titulo" : titulo,
            "autor" : autor,
            "ano_publicacao" : ano_publicacao,
            "id" : id_livro
        }

        adicionar_livro(livros)

    elif opção == 2:
        catalogo_livros = listar_livros()
        pprint.pprint(catalogo_livros)
        
    elif opção == 3:
        titulo = input("Informe o titulo: ")
        resultado = buscar_livro_por_titulo(titulo)
        print(resultado)
