# Criando uma lista.
lista1 = []

# copy():copia o valor de uma lista
lista2 = lista1.copy()

# append(elemento): Inserir um elemento ao final da lista.
lista1.append(7)
lista1.append(14)
lista1.append(21)

# insert(índice, elemento): Inserir um elemento em um índice específico
lista1.insert(0,0)
lista1.insert(5,28)

# extend(coleção): Inserir uma coleção de dados de forma individual
lista1.extend([35, 42, 49])

# pop(índice): Remove um elemento de uma lista, se o índice não estiver definido, remove o ultimo elemento
lista1.pop()

# remove(elemento): Remove por um elemento específico
lista1.remove(0)

# reverse(): Inverte as posições dos elementos
lista1.reverse()

# index(elemento): Retorna o índice do elemento buscado
lista1.index()

# count(elemento): Conta quantas vezes um elemento esta presente na lista
lista1.count()