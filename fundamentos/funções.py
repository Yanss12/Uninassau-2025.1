# Função: bloco de codigo "independente" executados mediante uma chamada

# def somar():
#     numero1 = int(input('informe um 1º numero: '))
#     numero2 = int(input('informe um 2º numero: '))

#     resultado = numero1 + numero2

#     print(f'O resultado da soma de {numero1} e {numero2} é {resultado}')

# somar()

# Boas praticas de funções: não usar print e input dentro das funções, ou seja, o codigo acima é lixo

def somar(numero1, numero2: int):
    resultado = numero1 + numero2
    return resultado

valor1 = int(input('informe o 1º numero: '))
valor2 = int(input('informe o 2º numero: '))
print(f'O resultado da soma entre {valor1} e {valor2} é {somar(valor1, valor2)}')