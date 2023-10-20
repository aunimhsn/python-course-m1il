# Acquisition des notes
marks = []

while True:
    mark = input('Veuillez entrer un nombre positif :')
    try:
        mark = int(mark)

    except ValueError:
        print('Vous n\'avez pas entrer un nombre')
    else:
        if (mark > 0):
            marks.append(mark)
        else:
            break

# Calcul de la moyenne
try:
    average = sum(marks) / len(marks)
except ZeroDivisionError:
    print('Vous n\'avez rentré aucune note')
else:
    print(f'La moyenne est {average:.2f}')