# Escreva um algoritmo Python que leia três valores inteiros e apresente o menor dos valores lidos

# Entrada de dados
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
valor3 = int(input('Digite o terceiro valor: '))

# Geração de resultado
if valor1 <= valor2 and valor1 <= valor3:
    print(f'o menor valor digitado foi {valor1}')

elif valor2 <= valor1 and valor2 <= valor3:
    print(f'o menor valor digitado foi {valor2}')

elif valor3 <= valor1 and valor3 <= valor2:
    print(f'o menor valor digitado foi {valor3}')
