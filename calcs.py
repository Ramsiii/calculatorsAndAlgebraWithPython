# finds the lowest integer in a list
def min_int_in_list(a_list):
    list_index = 0
    min_int = a_list[0]
    while list_index < len(a_list)-1:
        if a_list[list_index] < min_int:
            min_int = a_list[list_index]
        list_index += 1
    return min_int


# finds the mean of a list of integers
def mean(yourList):
    total = 0
    for each in yourList:
        total += each
    
    mean = total / (len(yourList))
    return mean

# finds the median in a list of integers
def median(yourList):
    
    sortedList = sorted(yourList)
    
    if len(sortedList) % 2 == 0:
        median = int((sortedList[int(((len(sortedList))/2)-1)]+sortedList[int((len(sortedList))/2)]) / 2)
    else:
        median = sortedList[int((len(sortedList)-1)/2)]
    return median