# Escreva um algoritmo Python que realize o cálculo do Imposto de Renda a ser pago.Para isso é solicitado a renda anual e o número de dependentes do contribuinte. A renda líquida é calculada sobre a renda anual com um desconto de 2% para cada dependente do contribuinte. O contribuinte com uma renda líquida de até R$ 2.000,00 não paga imposto. Para aqueles que possuem renda líquida entre R$ 2.000,00 e R$ 5.000,00 o imposto é de 5% sobre o valor da renda líquida; e para rendas líquidas de R$ 5.000,00 até R$ 10.000,00 é de 10%. Rendas superiores a R$10.000,00 pagam 15% de imposto.

# Entrada de dados
renda_anual = float(input('Informe a renda anual: '))
quantidade_dependentes = int(input('Informe o numero de dependentes: '))

#processamento
porcentagem_desconto = quantidade_dependentes * 2
valor_desconto = (renda_anual / 100) * porcentagem_desconto
renda_liquida = renda_anual - valor_desconto

# Geração do resultado
if renda_liquida <= 2000:
    print('Isento do imposto de renda')

elif renda_liquida > 2000 and renda_liquida <= 5000:
    valor_imposto = renda_liquida * 0.05
    print(f'Imposto a pagar: R$ {valor_imposto:.2f}')

elif renda_liquida > 5000 and renda_liquida <= 10000:
    valor_imposto = renda_liquida * 0.10
    print(f'Imposto a pagar: R$ {valor_imposto:.2f}')

else:
    valor_imposto = renda_liquida * 0.15
    print(f'imposto a pagar R$: {valor_imposto:.2f}')