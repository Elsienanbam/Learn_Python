# A function is a group of code written to achieve a specific task.
# the return statement allows the output of the function to be used again in other parts of your code
# any line of code after the return statement in a function is ignored
# there is no limit to the number of arguments a function can have
#def intro(title, name):
#    greet = ('Nice to meet you ' , title , ' ' , name)
#    return

#my_title = input('what is your title? ')
#my_name = input('what is your name? ')
#greeting = intro(my_title, my_name)
#print(greeting)


# if you want to give arguments without worrying about the order, use the key arguments format
# def intro(title, name):
#     greet = ('Nice to meet you ' + title + ' ' + name)
#     return greet
#
# my_title = input('what is your title? ')
# my_name = input('what is your name? ')
# greeting = intro(name=my_name, title=my_title)
# print(greeting)

# A variable defined in the global scope cannot be reassigned in a local scope unless the 'global' keyword
globalvar = 'this is global'
def my_function():
    global globalvar
    globalvar = 'okay'
    print(globalvar)
my_function()
print(globalvar)