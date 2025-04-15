# Criando uma lista.
lista = []

# append(elemento): Inserir um elemento ao final da lista.
lista.append(7)
lista.append(14)
lista.append(21)

# insert(índice, elemento): Inserir um elemento em um índice específico
lista.insert(0,0)
lista.insert(5,28)

# extend(coleção): Inserir uma coleção de dados de forma individual
lista.extend([35, 42, 49])

# pop(índice): Remove um elemento de uma lista, se o índice não estiver definido, remove o ultimo elemento
lista.pop()

# remove(elemento): Remove por um elemento específico
lista.remove(0)

print(lista)