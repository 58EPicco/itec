dataA = [
    [ # Males
        [1, 'Liam', 19837],
        [2, 'Noah', 18267],
        [3, 'Michael', 14516],
        [4, 'James', 13525],
        [5, 'Oliver', 13389]
    ],
    [ # Females
        [1, 'Emma', 18688],
        [2, 'Olivia', 17921],
        [3, 'Ava', 14924],
        [4, 'Isabella', 14464],
        [5, 'Sophia', 13928]
    ]
]

dataB = 'Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f'

# Transforma el string en lista
dataB = dataB.split(',')
aux = [[],[]]
for i in range(2, len(dataB), 3):
    if dataB[i] == 'm':
        aux[0].append([dataB[i - e] for e in range(2, -1, -1)])
    elif dataB[i] == 'f':
        aux[1].append([dataB[i - e] for e in range(2, -1, -1)])
dataB = aux

# Ordena la lista B
for sex in range(2):
    i = len(dataB[sex]) - 1
    flag = 0
    while True:
        if int(dataB[sex][i][1]) > int(dataB[sex][i-1][1]):
            aux = dataB[sex][i-1]
            dataB[sex][i-1] = dataB[sex][i]
            dataB[sex][i] = aux
        i -= 1
        if i == flag:
            flag += 1
            i = len(dataB[sex]) - 1
            if flag == len(dataB[sex]) - 1:
                break

namesInit = []
# Ejercicio 1
print('--------------------------------------------')
for sex in range(2):
    if sex == 0:
        print('Varones: \n ')
    else:
        print(' \nMujeres: \n ')
    for p in range(5):
        namesInit.append(dataA[sex][p][1]) # code eje 2
        namesInit.append(dataB[sex][p][0]) # code eje 2

        cantNacA = dataA[sex][p][2]
        cantNacB = int(dataB[sex][p][1])
        if cantNacA > cantNacB:
            print(f'{cantNacA - cantNacB} de {dataA[sex][p][1]} del 2018 sobre {dataB[sex][p][0]} del 2008')
        else:
            print(f'{cantNacB - cantNacA} de {dataB[sex][p][0]} del 2008 sobre {dataA[sex][p][1]} del 2018')

print('--------------------------------------------')
# Ejercicio 2
letter = input('Letra inicial: ')
namesOutput1 = ''
for name in namesInit:
    if name[0] == letter:
        namesOutput1 += name + ' '
print(f'Nombres con {letter}: {namesOutput1}')
print('--------------------------------------------')
# Ejercicio 3
namesOutput2 = ''
for name in namesInit:
    if namesInit.count(name) > 1:
        namesInit.remove(name)
        namesOutput2 += name + ' '
print(f'Nombres que se repiten: {namesOutput2}')
print('--------------------------------------------')
