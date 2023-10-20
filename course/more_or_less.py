from random import randint

secret = randint(0, 100)
user_input = int(input('Veuillez entrer un nombre entre 0 et 100 : '))
attempts = 1

while user_input != secret:
    if secret > user_input:
        print('C\'est plus')
    else:
        print('C\'est moins')

    user_input = int(input('Veuillez entrer un nombre entre 0 et 100 : '))
    attempts += 1

print(f'Bravo, vous avez trouve le nombre secret en {attempts} essai.s')