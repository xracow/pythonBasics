#pedir un numero y evaljar si es par he impar
#solamente imprimir :"es par" o "Es impar"

number = int(input("Escribe el numer: "))
residuo = 2%number
if residuo == 0: 
    print("Es par")
else:
    print("Es impar")
