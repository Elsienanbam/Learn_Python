#lists use the square bracket []
#characterisitcs of lists: they are indexed, mutable, ordered and can have duplicate values.

my_list = [21,65,88,-5,-3,56,9,34,78,24,46]
max_number = my_list[0]
for number in my_list:
    if number > max_number:
        max_number = number
for numb in my_list:
    if max_number >= (2 * numb):
        print(my_list.index(numb))
    else:
        print(-1)

