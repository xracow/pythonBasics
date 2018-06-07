Total=0
try:
    while Total< 10:
        num1=int(input("Escrbe el numero:"))
        num2=int(input("Escrbe el segundo numero:"))
        Total=num1+num2

except:
    print("Es texto")
    
#    ejemplo del profe
    

    try:
        while True:
            one = int(input("First number: "))
            two = int(input("First number: "))
            sum = one + two
            if sum < 10:
                print("The sum {sum}")
            else:
                break
    except:
        pass
    print("bye")