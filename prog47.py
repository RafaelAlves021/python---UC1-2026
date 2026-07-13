arroz = 4.00
feijao = 7.00
macarrao = 5.00

total = 0

codigo = input("Digite o código do produto (0 para sair): ")

while codigo != '0':

    if codigo == '001':
        total += arroz
        print(f"Arroz adicionado. Total: R${total}")

    elif codigo == '002':
        total += feijao
        print(f"Feijão adicionado. Total: R${total}")

    elif codigo == '003':
        total += macarrao
        print(f"Macarrão adicionado. Total: R${total}")

    else:
        print("Código inválido.")

    codigo = input("Digite o código do produto (0 para sair): ")

print(f"Valor final da compra: R${total}")

      
            