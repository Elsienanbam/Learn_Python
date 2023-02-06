# A string is a python data type that is made up of a sequence of characters

# string conversion
# strings = 987923
# print(type(strings))
# conv_strings = str(strings)
# print(type(conv_strings))

# concatenation
first_name = 'Elsie'
last_name = 'David'
age = 27
# full_name = first_name + " "+ last_name
# name_age = full_name + " " + str(age)
# print(full_name)
# print(name_age)

# format method
# full_names = "{} {}"
# full_names = full_names.format(first_name, last_name)
# name_age = "{} {}"
# name_age = name_age.format(full_names, age)
# print(full_names)
# print(name_age)
# or
# full_names = "{1} {0} {0} {1}"
# full_names = full_names.format(first_name, last_name)
# name_age = "{1} {0}"
# name_age = name_age.format(full_names, age)
# print(full_names)
# print(name_age)

# f-string
# full_names = f"{1 + age} {first_name} {len(last_name)} {last_name + first_name}"
# print(full_names)

# Escape characters:
# \ - ignore
# \\ - backslash
# \n - newline
# \r - carriage return
# \t - tab
# \b - backspace
# ignore = ("this is me \"testing\" a new thing")
# print(ignore)
# backslash = ("type your name\\age")
# print(backslash)
# newline = ("I am testing the new line thing:\n here we go")
# print(newline)
# carriage_return = ("Not even sure what carraige return means \rbut")
# print(carriage_return)
# tab = ("My name is Elsie\tNanbam")
# print(tab)
# backspace = ("please delete r\b")
# print(backspace)

# checking for a substring in a string:

my_string = "I am a string"
# print('strindg' in my_string)
# print('String' not in my_string)

# A string is an array made up of substrings, you can use their index positions to access each substring
# for i in range (len(my_string)):
#     print(my_string[i])
# for char in my_string:
#     print(char)
# print(my_string[1 : -8])

# IN-BUILT STRING METHODS
# # to convert to uppercase:
# print(my_string.upper())

# # to convert to lowercase:
# print(my_string.lower())

# # to convert to proper title:
# print(my_string.title())

# # to swap case for all characters:
# print(my_string.swapcase())

# to remove trailing white spaces or characters on the right
# space_str = ('Hello World ')
# print(space_str.strip())

# # to remove trailing white spaces or characters on the left
# print(space_str.lstrip('H'))

# # to remove trailing white spaces or characters on the right and left
# print(space_str.strip('h'))

# # To check if a string is made up of just whitespaces and no other character
# print(my_string.isspace())

# # To check the number of times a character or a sequence of characters exist in a string
# print(my_string.count('am'))

# # To check if a character or sequence of characters exist in a string
# # It returns the index position of the first occurrence of the character or sequence of characters
# # If a character does not exist in a string, 'find' returns -1 and 'index' returns an error
# print(my_string.find('a'))
# print(my_string.index('i'))

letters = "abcdefghijklmnopqrstuvwxyz"
# # python idiom for backwards
# print(letters[::-1])
# To get the first item in a sequence without error if the string is empty
# print(letters[:1])
# To get last n number of items in a string use [-n:]
print(letters[-4:])
