# Returns the Simple Linear Regression in Slope Intercept Form y = mx + b given two points with x and y coordinates (explanatory variables and response variables)

def slope_intercept_form(x1, y1, x2, y2):
    m = float((y2-y1)/(x2-x1))
    b = (m*x2 - y2) / -1
    final_slope_int_form = f"The slope intercept form for your coordinates is y = {m}x + {b}"
    return m, b, final_slope_int_form

if __name__ == '__main__':
    # test with user input
    x1 = float(input("What is x1? "))
    y1 = float(input("What is y1? "))

    x2 = float(input("What is x2? "))
    y2 = float(input("What is y2? "))

    # unpacking the tuple that is returned by the function
    m, b, equation = slope_intercept_form(x1, y1, x2, y2)
    print(equation)
