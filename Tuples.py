#tuples use the normal brackets
#tuples are like lists, except the objects in a tuple cannot be changed so not mutable.

my_tuple = ('go',4,6,8,'girl',3,6,'you','have','got','this')
#for x in range(len(my_tuple)):
#    print(x)
#    print(my_tuple[x])

# to mutate a tuple, we convert it to a list first, mutate, then convert back to tuple

#create a list from the tuple
my_list = list(my_tuple)
print(my_list)
print(my_tuple)

#replace the item in index 2
my_list[2] = 'word'

#append an item to the list, this function takes one argument
my_list.append('taken')

#insert an item to the list, this function takes 2 arguments
my_list.insert(4,'fiver')

#remove an item from the list
my_list.remove('fiver')

#remove an item from the list using its index
my_list.pop(3)

#convert the list back to the tuple
my_tuple = tuple(my_list)
#print(my_list)
#print(my_tuple)

#check if item is in the tuple, this function returns a boolean value
print('go' in my_tuple)

