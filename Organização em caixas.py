# Um funcionário responsavel pela logistíca em uma distribuidora tem o seguinte problema: O produto é muito fragil e deve ser enviado em caixas especiais, essas caixas estão disponíveis em quatro tamanhos: extragrande, grande, médio e pequeno. as quais podem conter até 50, 20, 5, 1 unidade respectivamente.
# Escreva um algoritmo em python que leia a quantidade de produtos a serem enviados e calcule o número de caixas de cada tamanho que devem ser utilizadas. O algoritmo deve ser eficiente, ou seja, deve utilizar o menor número possível de caixas.

# Entrada de dados
import time
quantidade_produtos = int(input("Digite a quantidade de produtos a serem enviados: "))

# Variaveis
caixa_xg = 0
caixa_g = 0
caixa_m = 0
caixa_p = 0

# Estrutura de repetição que verifica se a quantidade de produtos é diferente de 0
while quantidade_produtos != 0:
    if quantidade_produtos >= 50:
        caixa_xg += 1
        quantidade_produtos -= 50

    elif quantidade_produtos >= 20:
        caixa_g += 1
        quantidade_produtos -= 20

    elif quantidade_produtos >= 5:
        caixa_m += 1
        quantidade_produtos -= 5

    elif quantidade_produtos >= 1:
        caixa_p += 1
        quantidade_produtos -= 1

# Geração de resultado
print('Calculando...')
time.sleep(2)
print(f'A quantidade de caixas são {caixa_xg} extragrandes, {caixa_g} grandes, {caixa_m} medias, {caixa_p} pequenas')