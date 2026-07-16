def idade(anoa, anon):
    idade = anoa - anon
    if idade < 18:
        print('Menor de idade')
    elif idade <= 65:
        print('Maior de idade')
    else:
        print('Idoso')
anoa = int(input('Dígite o ano atual:'))
anon = int(input('Dígite o seu ano de nascimento:'))
idade(anoa,anon)
