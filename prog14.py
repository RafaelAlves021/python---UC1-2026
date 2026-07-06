cargo = input('Dígite seu cargo:').upper()
if cargo == 'caixa':
    salario = 1500
    inss = (salario*12)/100
    print(inss)
    irrf = (salario*8)/100
    print(irrf)
    salariofinal = salario - irrf - inss
    print(salariofinal)
elif cargo == 'vendedor': 
    salario = 2400
    inss = (salario*12)/100
    print(inss)
    irrf = (salario*14)/100
    print(irrf)
    salariofinal = salario - irrf - inss
    print(salariofinal)
elif cargo == 'gerente':
    salario = 4000
    inss = (salario*12)/100
    print(inss)
    irrf = (salario*14)/100
    print (irrf)
    salariofinal = salario - irrf - inss
    print(salariofinal)

 