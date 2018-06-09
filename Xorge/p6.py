'''El usuario tendra que introducir valores numericos, los cuales se almacenarán para después saca
el promedio y mostrarlo cuando el valor introducido no sea numerico.

5
7
8
s
promedio: 6.5
'''
Flag = 0
Suma = 0
ListNum = []
#print(ListNum[len(ListNum)-1])
#a=type(ListNum[len(ListNum)-1])
try:
    while Flag <= 0:
        num = int(input('Escribe el valor:'))
        ListNum.append(num)
    
except:
    for n in ListNum:
        Suma += n
        Promedio = Suma / (len(ListNum))
    print(Promedio)

#string

#solucion de renato el maestro

myList = []
sum = 0

while True:
    num = input('Get the number')
    if num.isnumeric():
        sum += int(num)
        myList.append(sum)
    else:
        break
    
    prom = sum/len(myList)
    print(f'Promedio: {prom}')