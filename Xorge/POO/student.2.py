#Clase lunes 11 de junio 2018
from Classes.Student import Student #A qui mandamos llamar el objeto student desde el archivo StudentClass

student1 = Student('Giorgo',[99,55,100])
student1.print_details()
print(student1.getAverage())
#student1.number += 1
student2 = Student('Favio',[30,65,100])
#print(student2.number)

student2.print_details()
print(student2.getAverage())
  