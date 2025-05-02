
# Lista vai guardar todos os produtos
lista_estoque = []

# Função para cadastrar cada produto
def cadastrar_produto(descricao, quantidade = 0, valor = 0.0):
    produto = [descricao, quantidade, valor]
    lista_estoque.append(produto)

def exibir_estoque():
    return lista_estoque
