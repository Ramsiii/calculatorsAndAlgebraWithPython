celsius10DaysHighs = [26, 28, 22, 22, 26, 29, 26, 23, 21, 20]

fahrenheit10DaysHighs = [round(((9/5)*temp+32),1) for temp in celsius10DaysHighs]

print(fahrenheit10DaysHighs)

# # Print with explicit formatting
# print([f"{temp:.3f}" for temp in fahrenheit10DaysHighs])