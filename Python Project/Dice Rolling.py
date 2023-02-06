import random
print("Let's roll dice!")

while 1:
    Response = input("Ready to roll the dice? ")
    if Response == "yes":
        print("rolling...")
        random_number = random.randint(0, 6)
        print("Dice has the number", random_number)
    elif Response == "no":
        print("whatever, bye")
        break
    else:
        print("Don't be a dummy, type yes or no in those exact words!")



