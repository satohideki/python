from datetime import date

hoje = date.today().year
nome = input('Qual o seu nome? ')
nascimento = int(input('Qual sua data de nascimento? '))
idade = hoje - nascimento

print('Seu nome é', nome, 'e sua idade é:', idade);