import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        if(b == 0):
            raise ZeroDivisionError("Cannot divide number by 0.")
        
        return a/b
    except ZeroDivisionError as zde:
        print(f"Error : {zde}")


def calculator():
    try:
        cont = 'Y'
        while(cont == 'Y' or cont == 'y'):

            op = int(input("Enter operation : \n press 1 for + \n press 2 for - \n press 3 for * \n press 4 for /"))

            a = float(input("Enter first number : "))
            b = float(input("Enter second number : "))
            
            if(op==1):
                print(add(a, b))
            
            elif(op==2):
                print(sub(a, b))
            
            elif(op==3):
                print(mult(a, b))

            elif(op==4):
                print(div(a, b))

            else:
                print("Please enter valid operator!!")

            
            cont = input("Want to continue (Y / N) : ")
    except ValueError as ve:
        print(f"Error : {ve}")
    

calculator()



        
