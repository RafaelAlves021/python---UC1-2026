codigo = input('Dígite o código de erro:')
match codigo:
    case '200':
        print('Sucesso! Tudo certo com a sua requisição.')
    case '400':
        print('Erro do cliente: Requisição malformada.')
    case '401' | '403':
        print('Erro de permissão: Você não tem acesso a esta página.')
    case '404':
        print('Erro: Página não encontrada')
    case '500' | '503':
        print('Erro no servidor: Nosso sistema está instável no momento')
    case _:
        print('Para código inválido = código HTTP {codigo_status} desconhecido.')
    