# Files in python can be in two modes: Text file or Binary file
# To open a text file for reading only use the 'open' function
# The arguments are the name of the file and optionally, the mode it should be handled in
# 'rt' means read operation and text mode
# open("File.txt" , "rt")
#
# FILE OPENING OPERATIONS:
# 'r' - read operation
# (if the file does not exist an error is thrown)
# 'a' - append operation, the file is open already and we're appending to it
# (if the file does not exist a new file is created and the data is written on to the file)
# 'w' - write operation, the data written overwrites what exists on the file
# (if the file does not exist a new file is created and the data is written on to the file)
# 'x' - create operation, a new file is created
# (if the file exists already an error is thrown)
# 't' - text mode, opens the file in text mode
# 'b' - binary mode, opens the file in binary mode
#
# the file you want to handle should be in the same directory as the python file
# or you would have to reference the path

# # To open a file and read all contents
# read_file = (open("file.txt", "rt"))
# # To open a file and read a line from the content of the file
# print(read_file.readline())
# print(read_file.readline())
# print(read_file.readline())
# Loop through a file
# for line in read_file:
#     print(line)
# To write in a file, you can either append or overwrite using a loop.
# To create a new file, use a name that does not exist already
# The argument is the content you want to write in the file

# # To overwrite:
# write_file = (open("new_file.txt", "w"))
# write_file.write("Like the appearance of a rainbow in a cloud on a rainy day, \nso was the appearance of the brightness all around it: \nThe whole picture is of colorful, bright, happy radiance – like a rainbow in a cloud.")

# # To append:
# append_file = (open("new_file.txt", "a"))
# append_file.write("\nIn John’s heavenly vision, he saw the throne of God surrounded by a rainbow")

#To create a new file:
# create_file = open("created_file.txt", "x")
# print(create_file)

# To delete a file, you need to import the 'os' module first, then use the remove method
# The name of the file is the argument
import os
# os.remove("created_file.txt")

# To check if the path exists:
# print(os.path.exists("content.txt"))
# if os.path.exists('filenew.txt'):
#     os.remove("filenew.txt")
# else:
#     print("The file does not exist")