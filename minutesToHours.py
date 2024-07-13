
minutesOrHours = input("For total minutes to hours and minutes, type 'h'. For hours and minutes to only minutes, type 'm': \n")


if minutesOrHours == 'h':
    minutes = int(input('Enter minutes:\n'))
    hours = minutes // 60
    minutes_remaining = minutes % 60

    print(f'{minutes} minutes is {hours} hours and {minutes_remaining} minutes.')

elif minutesOrHours == 'm':
    hours = int(input('Enter hours:\n'))
    minutes = int(input('Enter minutes:\n'))
    hoursInMinutes = hours * 60
    total = minutes + hoursInMinutes

    print(f'{hours} hours and {minutes} minutes is {total} minutes.')
    
    