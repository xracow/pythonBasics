class Student(object):
    number = 0
    def __init__(self,name,score): 
        self.name = name
        self.score = score
        print(f'Hellow {name}')
    

    def getAverage(self):
        return sum(self.score)/len(self.score)


    def print_details(self):
        print(f'Name: {self.name}')
        print(f'Score: {self.score}')
        print(f'average: {self.getAverage()}')
    