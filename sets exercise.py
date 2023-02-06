my_set = {5, 2, 65, 34, 75, 7, 45, 34}
max_num = 0
for item in my_set:
    if max_num < item:
        max_num = item
print(max_num)