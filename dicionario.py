
pessoa = {}

# adicionando uma nova chave ao dicionário
pessoa['nome'] = input('Informe o nome: ')
pessoa['idade'] = input('Informe idade: ')
pessoa['profissao'] = input('Informe profissao: ')
pessoa['empresa'] = input('Informe empresa: ')


# exibindo os dados do dicionário
print(pessoa.get('nome'))
print(pessoa.get('idade'))
print(pessoa.get('profissao'))
print(pessoa.get('empresa'))

