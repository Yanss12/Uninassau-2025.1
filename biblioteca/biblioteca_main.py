from biblioteca_func import *
from biblioteca_menu import *
import pprint

while True:
    opção = int(input("\nInforme sua opção: (1 - Adicionar livro): (2 - Exibir catalogo): "))

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
        