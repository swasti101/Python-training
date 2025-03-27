import random
random_number = (random.randint(1, 100))

user_guess = int(input())
attempts = 1
while user_guess != random_number:
    attempts += 1 
    if(user_guess > random_number):
        message = "Too high!!"
    else :
        message = "Too low!!"
    
    user_guess = int(input(f"{message}, Try Again : "))


print(f"You took {attempts} attempts to guess the number!!")