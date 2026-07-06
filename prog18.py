num1 = int(input('Dígite um número:'))
num2 = int(input('Dígite outro número:'))
menu = int(input('Dígite o número da operação desejada:'))
match menu:
    case 1:
        op = num1 + num2
            
    case 2:
        op = num1 - num2
           
    case 3:
        op = num1 * num2
           
    case 4:
        op = num1 / num2
    case_:
        op=0
        print('Opção invalida')

print(f'O resultado da operação é {op}')