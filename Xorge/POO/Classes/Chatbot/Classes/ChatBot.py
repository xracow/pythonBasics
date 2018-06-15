import random

class ChatBot:
    def __init__(self,name,edad):
        self.name = name
        self.edad = edad
        print(f'Hola soy{name}')
    
    def Saludo(self):
        print('Que onda barrio')

    def PreguntaRandom(self,pregunta):
        respuesta= {
        'Hola ¿como estas?':'Super!',
        'Como te llamas':self.name,
        'Cual es tu lenguaje de programación favorito':'PHP',
        'Cual es tu edad':self.edad
        }

        if pregunta in respuesta:
            return respuesta[pregunta]
        else:
            return 'No te entendí'

        

    def chiste(self):
        chistes=[
            '¿En qué se parece una zapatería a una familia?\n' +
            'En que la zapatería hace calzado.\n'+
            '¿Y la familia?',
            '¿Qué le dice una pared a otra pared?\n'+
            'Nos vemos en la esquina.',
            '¿En qué se parece un aeropuerto a una peluquería?\n'+
            'En que en el aeropuerto aterrizan y en la peluquería te rizan'
        ]
        return chistes[random.randint(0,2)]

    def despedida(self):
        return 'hasta la vista baby'

Robot1 = ChatBot('Epifanio',54) 
"""
Robot1.Saludo()
pregunta = input('progunta me lo que quieras: ')

print(Robot1.PreguntaRandom(pregunta))
print(Robot1.chiste())
print(Robot1.despedida())
"""

flag = True
while flag:
    print("______Menu_______")
    print('Selecciona las siguientes opciones:')
    print('presiona 1 para saludarte')
    print('presiona 2 si quieres preguntarme algo')
    print('presiona 3 si quieres un chiste')
    print('presiona 4 si quieres salir')
    option = input('Ingresa la opcion requerida:')
  
    if option == '1':
        Robot1.Saludo()

    elif option == '2':
        pregunta = input('progunta me lo que quieras: ')
        print(Robot1.PreguntaRandom(pregunta))

    elif option == '3':
        print('')
        print(Robot1.chiste())

    elif option == '4':
        print(Robot1.despedida())
        flag = False
    else:
        print("opcion no valida")

    print("\n")    
    
