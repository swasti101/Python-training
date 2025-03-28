import math

def isEven(x):
    if(x % 2 == 0) : return True
    return False

def isOdd(x):
    if(x % 2 == 1) : return True
    return False

def isPrime(x):
    if(x <= 1): return False

    isprime = True
    i=2
    while(i*i <= x):
        if(x % i == 0):
            isprime = False
            break
        i += 1
    return isprime

try :
    num = int(input("Enter a number :"))
    if(isEven(num) == True):
        print("Given number is Even")

    if(isOdd(num) == True):
        print("Given number is odd.")

    if(isPrime(num) == True):
        print("Giben number is prime.")
except ValueError as ve:
    print(f"Error : {ve}")


