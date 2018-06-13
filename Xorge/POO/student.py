#Clase lunes 11 de junio 2018

class Student(object):
    number = 0
    def __init__(self,name,score): 
        self.name = name
        self.score = score
        print(f'Hellow {name}')
    
    def print_details(self):
        print(f'Name: {self.name}')
        print(f'Score: {self.score}')

student1 = Student('Giorgo',[99,55,100])
student1.number += 1
student2 = Student('Favio',[30,65,100])
print(student2.number)
student1.print_details()
student2.print_details()

'''
    OUTPUT
        Hellow Giorgo
        Hellow Favio
        Name: Giorgo
        Score: [99, 55, 100]
        Name: Favio n
        Score: [30, 65, 100]
'''