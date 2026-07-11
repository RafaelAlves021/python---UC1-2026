nome = "" 
while nome != "SAIR":
    nome = (input('Dígite um nome:')).upper()
    if nome=="SAIR":
        break
    print(f'Olá {nome} tudo bem?')