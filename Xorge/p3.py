#pedir un numero y evaljar si es par he impar
#solamente imprimir :"es par" o "Es impar"

number = int(input("Escribe el numer: "))
residuo = number%2
if residuo == 0: 
    print("Es par")
else:
    print("Es impar")

#Example from the teacher
    
num = int(input('give the number: '))
if (num % 2) == 0:
    print('is odd!')
else:
    print('is even!')