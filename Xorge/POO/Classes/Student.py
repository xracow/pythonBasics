class Subjects:
    def __init__(self,name,score):
        self.name = name
        self.score = score

class Student(object):
    def __init__(self,name,score, subject): 
        self.name = name
        self.score = score
        self.subject = []
        print(f'Hellow {name}')
        for key, value in self.Subject.items():
            self.subjects.append(Subject(key,value))


    def print_details(self):
        print(f'Name: {self.name}')
        print(f'Score: {self.score}')
        print(f'average: {self.getAverage()}')

    def getAverage(self):
        pass
        #return sum(self.score)/len(self.score)



    