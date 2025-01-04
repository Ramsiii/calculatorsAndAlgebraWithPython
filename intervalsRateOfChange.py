from avgRateOfChange import average_rate

# Interval examples
# f(x) = x² at x = 2

# Calculate average rate of change with smaller and smaller intervals, i.e. approaching instantaneous rate of change 

x = 2
intervals = [1, 0.1, 0.01, 0.001]

for h in intervals:
    x1, x2 = x, x + h
    y1, y2 = x1**2, x2**2
    print(f"Interval size {h}: Rate = {average_rate(x1, y1, x2, y2)}")