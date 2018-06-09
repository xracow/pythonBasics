'''funciones'''

'''
    Interactivamente se pediran numeros al usuario seguidos por un string que
    puede ser el signo "+" ó "-". A partir de ahi el siguiente elemento insertado
    se sumara o restará deacuerdo el valor del signo... el programa terminara cuando
    se inserte otro string que sea distinto de + o -4
    
    1
    +
    5
    6
    =====
    9
    -
    5
    4
    ...
'''
'''
def square(x):      
    return x ** 2
    
print(square(4))

 = []
 '''
sum = 0
num1=0
num2=0
sign="+"
Flag1 = True
Flag2 = True


while Flag1:
    num1 = input('Get the number1 :')
    
    if num1.isnumeric():        
        Flag1= False
        Flag2=True
        sign = input('Get the sign: ')
        
        if sign != '-' and sign != '+':            
            break
        
        else:            
           while Flag2:              
               num2 = input('Get the number2 :')
               
               if num2.isnumeric():
                   Flag2=False
                   Flag1= True
                   if sign == '-':
                       print(int(num1) - int(num2))
                   else:
                       print(int(num1) + int(num2))
                
            
            
     