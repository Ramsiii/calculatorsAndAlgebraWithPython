# finds the lowest integer in a list
def min_int_in_list(a_list):
    list_index = 0
    min_int = a_list[0]
    while list_index < len(a_list)-1:
        if a_list[list_index] < min_int:
            min_int = a_list[list_index]
        list_index += 1
    return min_int
