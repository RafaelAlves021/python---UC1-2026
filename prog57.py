def notas(n1,n2,n3,n4):
    notas = (n1 +n2 +n3 +n4) / 4
    if notas >=7:
        print('Aprovado!')
    elif notas >=5:
        print('Recuperação')
    else:
        print('Reprovado')
num1 = float(input('Dígite sua nota:'))
num2 = float(input('Dígite sua nota:'))
num3 = float(input('Dígite sua nota:'))
num4 = float(input('Dígite sua nota:'))
notas(num1,num2,num3,num4)