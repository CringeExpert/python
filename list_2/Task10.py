list1 = [x for x in range(0,100,3)]
print(list1)

for i in range(4,len(list1)//3,3):
    del list1[i]
print(list1)

print(sum(list1)/len(list1))

