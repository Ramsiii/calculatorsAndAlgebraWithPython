# note: this module is not meant to replace the "statistics" or the "math" modules but rather for my own practice

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
    if not yourList:
        return None
    
    sortedList = sorted(yourList)
    
    length = len(sortedList)
    mid = length // 2
    
    if length % 2 == 0:
        median = (sortedList[mid-1]+sortedList[mid]) / 2
    else:
        median = sortedList[mid]
    return median

# finds the sum of a list of integers, same as already existing sum()

def sum(yourList):
    total = 0
    for each in yourList:
        total += each
    return total
