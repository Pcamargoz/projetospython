n = str(input('Digite seu nome completo:')).strip()
nome = n.split()
print('prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(nome[0]))
print('Seu ultimo nome e {}'.format(nome[len(nome)-1]))

