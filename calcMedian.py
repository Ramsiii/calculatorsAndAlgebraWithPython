def median(yourList):
    
    sortedList = sorted(yourList)
    
    if len(sortedList) % 2 == 0:
        median = int((sortedList[int(((len(sortedList))/2)-1)]+sortedList[int((len(sortedList))/2)]) / 2)
    else:
        median = sortedList[int((len(sortedList)-1)/2)]
    return median


myList = [2,5,7,10,4,14]
print(median(myList))

myList2 = [7,10,4,5,14,2,22]
print(median(myList2))