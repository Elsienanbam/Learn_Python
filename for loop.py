# The 3 arguments for range are start, stop, increment/step
# for i in range(0, 12, 3):
#     print(i)
# print("The loop has ended")

# By default, the first and 3rd arguments are set to 0 and 1, only specify when this is not the case
# for i in range(5):
#     print(i)
# for i in range(4, 10):
#     print(i)

# The 'break' keyword terminates a loop before it is completed
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# print("The loop has ended")

# The 'continue' keyword stops the current iteration and proceeds to the next, it skips that part of the loop
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)
# print("The loop has ended")

for i in range(15):
    print("The number {0:2} squared is {1:<3}, and the cube is {2:>4}".format(i, i**2, i**3))
# for left alignment use '<', for right alignment use '>', for centered alignment use '^'
