# print("The program starts here!")
# value = (input("Enter the correct option from a to d: "))
# if value == "a":
#     print("You chose a")
# elif value == "b":
#     print("You chose b")
# elif value == "c":
#     print("You chose c")
# elif value == "d":
#     print("You chose d")
# else:
#     print("Invalid response, try again")
#
# print("The program ends here")

# There are two type of if-else statements:
# Exclusive if else statements: No overlaps between the 2 conditions so the order does not matter
# my_number = int(input("Enter a number: "))
# if my_number < 10:
#     print("The number is less than 10")
# else:
#     print("The number is not less than 10")
# Here the number is either less that 10 or not, no intersections

# Inclusive if else statements: There are overlaps between the 2 conditions so be mindful of the order
my_number = int(input("Enter a number: "))
if my_number % 6 == 0:
    print("The number is divisible by 2 and 3")
elif my_number % 2 == 0:
    print("The number is divisible by 2")
elif my_number % 3 == 0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by either 2 or 3")
# You have to start with the point of intersection first or you will not be able to capture it later
