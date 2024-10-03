import calcs

list1 = [3, 5, 7, 2, -10, 15, 1, 55, 7]
list2 = [7, 77, 777, 7777, 13, 1333, 78, 333, 666]

# find the min in each of two lists
print(calcs.min_int_in_list(list1))
print(calcs.min_int_in_list(list2))



list3 = [3,5,5,6,2,10,4]

# find the mean in list3
print(calcs.mean(list3))

list4 = [2,5,7,10,4,14]
list5 = [7,10,4,5,14,2,22]

# find the median in a list with an even number or integers
print(calcs.median(list4))

# find the median in a list with an odd number or integers
print(calcs.median(list5))

list6 = []
# should return None
print(calcs.median(list6))

list7 = [-4,6,8,-5,-2,0,7,7,4,-14,2,16,-8,3,-3,-9]

# find the sum of a list of integers
print(calcs.sum(list7))
