"""Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por km para viagem de até 200km e R$0,45 para viagens mais longas
"""
distancia = float(input('Qual a distância da sua viagem? '))
print('Você está preste a começar uma viagem de {}Km'.format(distancia))
"""if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45"""
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45  # simplificado com poucas linhas
print('E o preço da sua passagem ficará no valor de R${:.2f}'.format(preco))
