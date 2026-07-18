lista_compras = []

while True:
    item = input("Digite um item da compra (ou 'sair' para terminar): ")

    if item.lower() == "sair":
        break

    lista_compras.append(item)
    print(f'"{item}" foi adicionado à lista!')

print("\nLista de compras:")
for item in lista_compras:
    print(f"- {item}")
   