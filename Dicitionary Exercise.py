my_list = [2,5,8,4,2,6,8,0,5,3,6,1,3,3]
my_dict = {}
for i in my_list:
    if i in my_dict:
        cnt = my_dict[i]
    else:
        cnt = 0
    my_dict[i] = cnt+1

for key, value in my_dict.items():
    print(key, value)

print(my_dict)