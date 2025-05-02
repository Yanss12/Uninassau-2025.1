import calculadora

print('------Calculadora------')
print('-----------------------')

num1 = int(input('Informe o 1º valor: '))
num2 = int(input('informe o 2º valor: '))

opção = input('informe sua opção (+, -, * ou /): ')

if opção == "+":
    resultado = calculadora.somar(num1, num2)
    print('A soma foi: ', resultado)

elif opção == "-":
    resultado = calculadora.subtrair(num1, num2)
    print('A subtração foi: ', resultado)

elif opção == "*":
    resultado = calculadora.multiplicar(num1, num2)
    print('A multiplicação foi: ', resultado)

elif opção == "/":
    resultado = calculadora.dividir(num1, num2)
    print('A divisão foi: ', resultado)