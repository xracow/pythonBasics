'''
BankAccount
'''

class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        self.balance -= amount
        return self.balance

   
BankAccount1 = BankAccount()
'''
print(BankAccount1.balance)

amount = int(input('ingresa el deposito:'))
BankAccount1.deposit(amount)
print(BankAccount1.balance)  
'''

print('Selecciona las siguientes opciones:')
print('presiona 1 si quieres hacer un deposito')
print('presiona 2 si quieres hacer un retiro')
print('presiona 3 si quieres ver el balance')
print('presiona 4 si quieres salir')

flag = True
while flag:
    option = input('Ingresa la opcion requerida:')

    if option == '1':
        amount = int(input('ingresa el deposito:'))
        BankAccount1.deposit(amount)

    elif option == '2':
        amount = int(input('ingresa la cantidad a retirar:'))

        if amount > BankAccount1.balance:
            print('Fondos insuficientes, pruebe con una cantidad mas baja')
            
        else:
           BankAccount1.withdraw(amount)

    elif option == '3':
        print(BankAccount1.balance)

    elif option == '4':
        flag = False    
    