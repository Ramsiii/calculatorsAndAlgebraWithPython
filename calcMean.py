def mean(yourList):
    total = 0
    for each in yourList:
        total += each
    
    mean = total / (len(yourList))
    return mean


myList = [3,5,5,6,2,10,4]

print(mean(myList))