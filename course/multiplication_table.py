user_input = int(input("Veuillez la table à afficher : "))
multiplication_table = []

for i in range(1, 11):
    if ((user_input*i) % 3 == 0):
        multiplication_table.append(f'{user_input*i}*')
    else:
        multiplication_table.append(user_input*i)
                                    

print(multiplication_table)

