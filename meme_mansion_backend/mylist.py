mylist = [5,51,2,2,5,7]

newList = []



for i in mylist:
    if i not in newList:
        newList.append(i)

print(newList)
    