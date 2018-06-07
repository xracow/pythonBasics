chart = '*****'
x = 1
y = len(chart)
while x < y:
    print(chart[0:y])
    x = x+1
    y=y-1
    
    
    #solucion de renato
    
height= 10
while height > 0:
    print("*"*height)
    height-=1

#height= int(input("Enter height: "))
while height > 0:
    print("*"*height)
    height-=1
    
try:
    height= input("Enter height: ")
    while True:
        height= int(height)
        while height > 0:
            print("*"*height)
            height-=1
        height= input("Enter height: ")
except:
    print("Is not a number")
