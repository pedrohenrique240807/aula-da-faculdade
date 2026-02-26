nome=input('Dgite seu nome:').upper()
sobrenome=input('Digite seu sobrenome:').upper()
dia=input('Digite o dia de seu nascimento:')
mes=input('Agora seu mês de nascimento:')
ano=input('E por fim do ano de seu nascimento:')

faculdade=input('Qual nome de sua faculdade?')

print('Suas informações são:' + nome + ' ' + sobrenome + '.' + 'e sua data de nascimento é' + str(dia) + '/' + str(mes) + '/' + str(ano) + 'estudande da facudade' + ' ' + str(faculdade))

email=(nome.lower() + '.' + sobrenome.lower() + '@' + faculdade + '.' + 'gmail.com')

senha = 'a' + str(email.count('a')) + 'e' + str(email.count('e')) + 'i' + str(email.count('i')) + 'o' + str(email.count('o')) + 'u' + str(email.count('u'))
print('Sua senha e email são:' , senha, 'e' + email)
