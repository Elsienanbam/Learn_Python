#Dictionaries use the curly brackets
#characteristics of dictionaries: they are not indexed, mutable, not ordered
# and can have duplicate values but no duplicate keys.

my_dict = {
'flustered' : 'agitated or confused',
'plucky' : 'having or showing determined courage in the face of difficulties',
'insouciant' : 'showing a casual lack of concern',
'Nanbam' : 'Middle name'
}
my_dict['elsie'] = 'First name'

for key in my_dict:
    print(key)

for key in my_dict:
    print(my_dict[key])
for value in my_dict.values():
    print(value)
for key, value in my_dict.items():
    print(key, value)