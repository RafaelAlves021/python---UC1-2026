nome = input('Dígite seu nome:')
idade = float(input('Dígite sua idade:'))
genero = input('Digite seu gênero (M/F): ').upper()
if idade >= 18 and genero == "M":
    print("Apto ao alistamento")
else:
    print("Não apto ao alistamento")

