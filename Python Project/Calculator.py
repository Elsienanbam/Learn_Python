import time

print("=====Welcome to calculator=====")
while 1:
    print("What would you like to do?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    def exiting():
        print("Exiting...")
        time.sleep(2)
        print("Thank you, come again next time")


    def loop_it():
        time.sleep(2)
        while True:
            next_operation = input("Would you like to perform another operation? y/n: ")
            if next_operation == 'y':
                break
            elif next_operation == "n":
                exiting()
                break
            else:
                print("invalid response, please enter y or n ")


    response = int(input("Enter your choice: "))

    if response == 1:
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        sum = first_number + second_number
        print("Output: ", sum)
        loop_it()

    elif response == 2:
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        sum = first_number - second_number
        print("Output: ", sum)
        loop_it()

    elif response == 3:
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        sum = first_number * second_number
        print("Output: ", sum)
        loop_it()

    elif response == 4:
        first_number = int(input("What is the first number? "))
        second_number = int(input("What is the second number? "))
        sum = first_number / second_number
        print("Output: ", sum)
        loop_it()

    elif response == 5:
        exiting()
        break
    elif response != type(int):
        print("Please enter a valid response - (numbers 1 to 5)")
        continue


