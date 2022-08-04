import json
f = open('answers/assignment 3/dados.json')
dados = json.load(f)
aux = 0
maior = 0
menor = 0
soma = 0
media = 0
for dia in dados:
    if (dia['valor']) != 0:
        aux = dia['valor']
        if (aux > maior):
            maior = aux
        if(menor == 0):
            menor = aux
        elif (aux < menor):
            menor = aux
        soma += dia['valor']
print('Faturamento do mês maior foi: R$ ' + str(maior) + '.')
print('Faturamento do mês menor foi: R$ ' + str(menor) + '.')
media = soma / len(dados)
diasFaturamento = ''
for i in dados:
    if (i['valor']) != 0:
        if (i['valor']) > media:
           diasFaturamento += (str(i['dia']) + ' ')      
print('faturamento foi maior que a média mensal foram: ' + diasFaturamento)