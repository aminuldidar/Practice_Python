# Take only the positive numbers from a list and add to a new list 

a = [10, -5, 15, 20, -7, 0 ,25, -13]
newlist = []
for i in a:
    if i>0:
        newlist.append(i)
print(newlist)


