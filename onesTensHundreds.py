# Dividing by a power of 10 shifts a value right. Ex: 321 // 10 is 32. Ex: 321 // 100 is 3.
# % by a power of 10 gets the rightmost digits. Ex: 321 % 10 is 1. Ex: 321 % 100 is 21.


threeDigitInt = int(input("Give me a 3 digit integer: \n"))

ones_digit     = threeDigitInt % 10    
tmp_val        = threeDigitInt // 10

tens_digit     = tmp_val % 10     
tmp_val        = tmp_val // 10

hundreds_digit = tmp_val % 10     

print(f"The ones digit is: {ones_digit}\nThe tens digit is: {tens_digit}\nThe hundreds digit is: {hundreds_digit}")
