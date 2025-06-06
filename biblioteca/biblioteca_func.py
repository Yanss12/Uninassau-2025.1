import random
catalogo_livros = []

# função para adicionar livro no catalogo
def adicionar_livro(novo_livro : dict) -> None:
   '''
      Descrição: Função para adicionar novo livro no catalogo(lista).\n
      Parâmetro: A função recebe um novo_livro do tipo dict.\n
      Retorno: A função não retorna nada.
   '''    
   catalogo_livros.append(novo_livro)

# função para gerar um id aleatorio para os livros
def gerar_id(min_val=1,max_val=1000):
   '''
      Descrição: Função para gerar um id aleatorio para os livros.\n
      parâmetro: A função recebe um numero aleatorio que define o id.\n
      Retorno: A função retorna um id aleatorio para cada livro.
   '''
   return random.randint(min_val,max_val)

# função para listar os livros do catalogo
def listar_livros() -> list:
   '''
      Descrição: função para retornar os livros no catalogo(lista).\n
      Parâmetro: a função não recebe valores do parametro.\n
      Retorno: A função retorna uma lista com todos os livros.
   '''
   return catalogo_livros

# função para pesquisar livros pelo titulo
def buscar_livro_por_titulo(titulo: str) -> list:
   '''
      Descrição: Função para buscar livros pelo título no catálogo.\n
      Parâmetro: titulo (str) - título do livro a ser buscado.\n
      Retorno: Lista de livros que correspondem ao título informado.
   '''
   for livro in catalogo_livros:
      if livro.get('titulo').lower() == titulo.lower():
         return livro
