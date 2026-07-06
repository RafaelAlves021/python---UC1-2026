print('Bem vindo ao TechPArk')
idade = int(input("Digite sua idade: "))
ingresso = input("Você tem ingresso? (S/N): ").upper()

if idade >= 12 and ingresso == "S":
    print("Pode entrar na montanha-russa!")
else:
    print("Não pode entrar na montanha-russa!")