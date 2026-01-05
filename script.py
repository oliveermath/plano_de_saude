# Mensagens de boas-vindas

print('| >    BEM VINDO CARO CLIENTE    < |')
print(35 * '-')
print('------- Somos a UnitSaude -------')
print(35 * '~')

# Entrada do usuário do nome, valor base e idade
nome = input('Por favor, nos informe seu nome: ')
valorbase = float(input('Informe o valor base: ')) 
idade = int(input('Digite a sua idade: '))

# Calculando o valor mensal e porcentagem com base na faixa etária
if idade >= 0 and idade < 19:
    valormensal = (valorbase * 100) / 100 # 100% do valor

elif idade < 29:
    valormensal = (valorbase * 150) / 100 # 150% do valor

elif idade < 39:
    valormensal = (valorbase * 225) / 100 # 225% do valor

elif idade < 49:
    valormensal = (valorbase * 240) / 100 # 240% do valor

elif idade < 59:
    valormensal = (valorbase * 350) / 100 # 350% do valor

else:
    valormensal = (valorbase * 600) / 100 # 600% do valor

print(40 * '-')
print(40 * '>') 
print(40 * '-')

# Saída do resultado final
print(f'Bem vindo ao sistema UnitSaude, {nome}') # Mensagem principal
print(f'O valor do seu plano é: R${valorbase:.2f} reais') # Valor base do cliente
print(f'A sua idade é de: {idade} anos') # Idade do cliente
print(f'O valor mensal do plano é: R${valormensal:.2f} reais') # Valor mensal 
