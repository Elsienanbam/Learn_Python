#sum all the items in the tuple

data = (3,65,7,32,7)
#for i in range(len(data)):
#    if i == 0:
#        answer = int(data[i])
#    else:
#        answer = int(data[i]) + answer
#print(answer)

for item in data:
    if data.index(item) == 0:
        sum = item
    else:
        sum = sum + item
print(sum)
