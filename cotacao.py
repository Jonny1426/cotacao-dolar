import requests as r

acess = r.get('https://economia.awesomeapi.com.br/all/USD-BRL')
texto = acess.json()

valor = float(texto['USD']['high'])

print('Moeda:',texto['USD']['name'])
print(f'cotação: {valor:.2f}')

