def convertTimeTo24Hr(s):
    # if the last two char are 'AM' and
    # the first two are '12' 
    if s[-2:] == 'AM' and s[:2] == '12':
        # add '00' to beginning and cut the first and last two char
        return '00' + s[2:-2]
    # elif last two digits are 'AM'
    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2] 
    elif s[-2:] == 'AM':
        # return the string without last two char 'AM'
        return s[:-2]
    else:
        # if PM and not 12, add 12 to the first two char converted to an int, 
        # convert these back to string and concatenate them with
        # the string without the first two and the last two char
        return str(int(s[:2]) + 12) + s[2:8]
        

if __name__ == '__main__':
    s = input('Enter the time in the format 00:00:00AM: ')

    result = convertTimeTo24Hr(s)
    print(f'The 24-hour format for that time is: {result}.')
