def mean(yourList):
    total = 0
    for each in yourList:
        total += each
    
    mean = total / (len(yourList))
    return mean


if __name__ == '__main__':

    myList = [3,5,5,6,2,10,4]

    print(f'Example list: \n{myList}')
    print('The mean of that list is:')
    print(mean(myList))
