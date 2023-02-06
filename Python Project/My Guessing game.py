import random

random_number = random.randint(0, 100)
my_guess = input('guess a number: ')
my_guess = int(my_guess)
while my_guess != random_number:
    if my_guess < random_number:
        print((str(my_guess)) + " is less than the number")
    else:
        print((str(my_guess)) + " is greater than the number")
    print('you have to guess again')
    my_guess = input("guess another number: ")
    my_guess = int(my_guess)
print("you got it!")
