
pessoa = {}

# adicionando uma nova chave ao dicionário
pessoa['nome'] = input('Informe o nome: ')
pessoa['CPF'] = input('Informe CPF: ')
pessoa['RG'] = input('Informe o RG: ')
pessoa['Data de Nascimento'] = input('Informe Data de Nascimento: ')
pessoa['genero'] = input('Informe genero: ')
pessoa['e-mail'] = input('Informe e-mail: ')
pessoa['telefone'] = input('Informe telefone: ')
pessoa['tipo sanguineo'] = input('Informe tipo sanguineo: ')
pessoa['profissao'] = input('Informe profissao: ')
pessoa['empresa'] = input('Informe empresa: ')


# exibindo os dados do dicionário
print(pessoa.get('nome'))
print(pessoa.get('CPF'))
print(pessoa.get('RG'))
print(pessoa.get('Data de Nascimento'))
print(pessoa.get('genero'))
print(pessoa.get('e-mail'))
print(pessoa.get('telefone'))
print(pessoa.get('tipo sanguineo'))
print(pessoa.get('profissao'))
print(pessoa.get('empresa'))

