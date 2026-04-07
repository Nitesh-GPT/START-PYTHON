import random

Random_number = random.randint(1, 10)
user_input = int(input('Enter any number between 1 and 10: '))
while Random_number != user_input:
    if Random_number <user_input:
        print('your guess is too high')
    elif Random_number > user_input:
        print('your guess is too low')
    user_input = int(input("guess again: "))
print("perfect buddy ! your guess right")