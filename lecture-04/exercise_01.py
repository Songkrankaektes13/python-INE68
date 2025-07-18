print('--------------')
print('MPH\tKPH')
print('--------------')

for mph in range(60, 131, 10):
    kph = mph * 0.6214
    print(mph, '\t', round(kph, 2))

print('--------------')

