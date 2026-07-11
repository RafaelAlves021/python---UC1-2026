carros = {}
for i in range(2):
    carro = str(input('Qual o seu carro:'))
    marca = str(input('Qual a marca:'))
    valor = str(input('Qual o valor:'))
    carros[carro] = (marca, valor)

print(f'Informações do carro: {carros}')