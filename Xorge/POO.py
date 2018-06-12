class Antenna (object):
    color = ''
    longitude =''

class Hair(object):
    color = ''
    longitude =''

class Eye(object):
    shape = ''
    color = ''
    size = ''

class Parent(object):
    color = ''
    size = ''
    aspect = ''
    antennas = Antenna()
    eyes = Eye()
    hair = Hair()

    def floatAction(self):
        print('I\'m floating!')
        
class OtherParent (Obj):
    def flayAction(self):
        print('I\'m flying!')
        
class NewObj (Parent,OtherParent):
    pass

myNewObj = NewObj()
myNewObj.floatAction() 
myNewObj.flayAction()
