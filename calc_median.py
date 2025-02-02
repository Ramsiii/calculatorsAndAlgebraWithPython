def median(yourList):
    
    sortedList = sorted(yourList)
    
    if len(sortedList) % 2 == 0:
        median = int((sortedList[int(((len(sortedList))/2)-1)]+sortedList[int((len(sortedList))/2)]) / 2)
    else:
        median = sortedList[int((len(sortedList)-1)/2)]
    return median

if __name__ == '__main__':
    
    myList = [2,5,7,10,4,14]
    print(f'Example of a list with an even number of integers: \n{myList}')
    print('The median of that list is:')
    print(median(myList))

    myList2 = [7,10,4,5,14,2,22]
    print(f'Example of a list with an odd number of integers: \n{myList2}')
    print('The median of that list is:')
    print(median(myList2))
