speed_kmh = float(input('Veuillez entrer une vitesse en km/h : '))
KMH_TO_MPH = 1.609
# result = round(speed_kmh / KMH_TO_MPH, 2)
# print(f'{speed_kmh} km/h = {result} m/h')

result = speed_kmh / KMH_TO_MPH
print(f'{speed_kmh} km/h = {result:.2f} m/h')

