
def factorial(n):
    n_counter = n
    while n_counter != 1:
        n *= (n_counter-1)
        n_counter -= 1
    return n


n = int(input("Give me a non-negative integer: "))

print(f"The factorial of {n} is {factorial(n)}.")