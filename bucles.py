llista=[]
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

#Bucle de bucle amb elements
notes=[[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
compt=0
for i in notes:
    for j in i:
        if(j==10):
            compt+=1
print('Hi ha', compt, 'deus (10) a la classe')

print('Endivina un númer entre 1 i 10: ')
n=7
while True:
    num=int(input('Introdueix un número: '))
    if(num==n):
        print('Has encertat!')
        break
    elif(num!=n):
         print('No has encertat, torna-ho a intentar')