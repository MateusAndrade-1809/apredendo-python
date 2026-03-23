aluno = {
    'nome': input('Digite seu usuario: '),
    'Curso': input('Curso: '),
}
print('Otimo curso!')
aluno['senha'] = input('Digite sua senha: ')
print(f'{aluno["nome"]}, cursa {aluno["Curso"]} e sua senha é {aluno["senha"]}')
# dicionario é uma lista mutavel melhorada que tem como utlizar de diversas formas