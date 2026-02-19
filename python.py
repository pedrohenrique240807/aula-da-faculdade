nome=input('qual seu nome?')
print('ola', nome, 'seja bem vindo ao meu mundo')

dominio= input('digite seu dominio!')
print(dominio)

senha= input('crie uma senha')
print('sua senha é:' ,senha)

email= nome + '@' + dominio
print('seu email é :', email)

palavra= 'jaca'
#colocar a string como toda maiuscula
print('colocando o texto em maiucula:', palavra.upper())

PALAVRA= 'JACA'
#colocar a string como toda maiuscula
print('colocando o texto em minuscula: ', PALAVRA.lower())


#colocar caracter da string
palavra_contar = 'banana'
print('Contar a letra b',palavra_contar.count('b'))
print('Contar a letra a',palavra_contar.count('a'))
print('Contar a letra n',palavra_contar.count('n'))

print(email)
letraa=email.count('a')
letrae=email.count('e')
letrai=email.count('i')
letrao=email.count('o')
letrau=email.count('u')


senha= 'a'+str(letraa)+ 'e'+str(letrae)+ 'i'+str(letrai)+ 'o'+str(letrao)+ 'u'+str(letrau)

print(senha)


