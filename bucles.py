llista.append(input('Introdueix un nom: '))
llista.append(input('Introdueix un nom: '))
llista.append(input('Introdueix un nom: '))

#Amb bucle
for i in range(3):
    llista.append(input('Introdueix un nom: '))

print('')
print(llista)
print('')

#Bucle en un interval concret
for i in range(17, 101):
    if(i % 2 == 0):
        print(i, end=' ')
print("\n")

#Bucle en una llista
compt = 0
for i in llista[0]:
    if(i=='a'):
        compt += 1
print('El primer nom de la llista és', llista[0], 'i té', compt, 'lletres a')
print('')

notes=[[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
for fila in range(len(notes)):
    for columna in range(len(notes[fila])):
        if notes[fila][columna] == 10:
            comptador += 1
            posicions.append((fila, columna))