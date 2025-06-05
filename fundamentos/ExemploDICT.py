produto = {
    # Chave: valor
    'descricao': 'Pincel Pilot',
    'quant': 10,
    'valor': '19'
}

print(produto)

# get(chave) -> Retorna o valor pertencente a chave
print(produto.get('descricao'))

# items() -> Retorna chaves e valores do dicionário
print(produto.items())

# keys() -> Retorna as chaves do dicionário
print(produto.keys())

# values() -> Retorna os valores do dicionário
print(produto.values())