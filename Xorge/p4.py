#ejemplos con operadores logicos
''''El usuario introduce un numero y se tendra que evaluar
Si el texto es igual a suma y el numero es mayor  10 imprimir la sumatoria de si mismo
hasta que sea mayor o igual a 100
la sumatoria: 11 + 11 + 11 ...
En pantalla se visualizará:
11
22
33
44
..
109
cualquier caso diferente de entrada salir del programa.

'''

num= 3#int(input('Escribe el numero: '))
num2=num
suma= '+'#input('Escribe la suma: ')

if num > 10 and suma  == '+' :
    
    while num < 100:
        print(num)
        num += num2
        
    print(num)      
    

    