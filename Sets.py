# Sets are like dictionaries except they have no keys, just values
# sets use curly brackets like dictionaries
# Characteristics are: they are not ordered, not indexed, cannot have duplicate values.
# changeable but you cannot replace another item and you can have items of different data types
# we can only fetch items from a set using loops

my_set = {'elsie', 'this',4,5.65,12,'is','a','set'}
print(my_set)

# this is the only way to loop through a set
#for item in my_set:
#    print(item)

# to check items in a set:
#print('this' in my_set)

#add an item to a set
my_set.add('I see')

# To remove an item from a set, you can use the 'remove' or the 'discard' function. Only use 'remove' if
# you are sure the item you are trying to remove exists in the set or else it will display an error.
# It is better to use 'discard' because nothing happens if the item is not found in the set.
#my_set.discard(4)

# the 'pop' function also removes items from a set but it takes no argument so you have to assign a
# variable to be able to identify what item was removed.
#popped = my_set.pop()

# the 'clear' function empties a set, it removes all the items in it
my_set.clear()
print(my_set)

