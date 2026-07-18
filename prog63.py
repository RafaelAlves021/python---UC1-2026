cursos = ['ADS', 'Engenharia de Software']

# Adicionar um curso
novo_curso = input('Adicione um curso: ')
cursos.append(novo_curso)

# Mostrar lista organizada
print('\nLista de cursos:')
for curso in cursos:
    print(curso)

# Excluir um curso
curso_excluir = input('\nDigite o nome do curso que deseja excluir: ')

if curso_excluir in cursos:
    cursos.remove(curso_excluir)
else:
    print('Curso não encontrado!')

# Mostrar lista atualizada
print('\nLista atualizada:')
for curso in cursos:
    print(curso)