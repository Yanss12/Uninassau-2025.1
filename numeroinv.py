# Escreva um algoritmo em python que receba do usuário 2 variáveis, e ao final exiba as variáveis com os valores invertidos

# Leitura dos dados de entrada
numero_1 = int(input('informe o primeiro valor: '))
numero_2 = int(input('informe o segundo valor: '))

# Processamento
var_auxiliar = numero_1
numero_1 = numero_2
numero_2 = numero_1

# Geração de resultado
print(f'O valor do numero 1 é: {numero_1}')
print(f'O valor do numero 2 é: {numero_2}')