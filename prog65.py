mercado = []

while True:
    produto = input('Escolha o seu produto: ')

    if produto.lower() == "sair":
        break

    if produto in mercado:
        print('Item já cadastrado')    
    
    
    else:
        mercado.append(produto)


for x in mercado:
    print(x)