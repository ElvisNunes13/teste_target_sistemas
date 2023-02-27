import json
with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

menor_faturamento = faturamento[0]['valor']
maior_faturamento = faturamento[0]['valor']

soma_faturamento = 0
dias_com_faturamento = 0
for dia in faturamento:
    if dia['valor'] > 0:
        dias_com_faturamento += 1
        soma_faturamento += dia['valor']
    if dia['valor'] < menor_faturamento:
        menor_faturamento = dia['valor']
    if dia['valor'] > maior_faturamento:
        maior_faturamento = dia['valor']

media_mensal = soma_faturamento / dias_com_faturamento

dias_acima_da_media = 0
for dia in faturamento:
    if dia['valor'] > media_mensal:
        dias_acima_da_media += 1

print('Menor faturamento: R$ {:.2f}'.format(menor_faturamento))
print('Maior faturamento: R$ {:.2f}'.format(maior_faturamento))
print('Número de dias com faturamento acima da média mensal: {}'.format(dias_acima_da_media))