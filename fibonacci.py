# returns the nth fibonacci number, starting at 0
def FibonacciNumber(termIndex):
    if termIndex == 0:
       return 0
    
    previous = 0
    current = 1
    i = 1
    while i < termIndex:
       next = previous + current
       previous = current
       current = next
       i += 1
    
    return current


if __name__ == '__main__':
    num = int(input('What is the nth fibonacci number? \ne.g. 0 will return 0, 1 will return 1, 2 will return 1, \n3 will return 2, 4 will return 3, 5 will return 5, etc. \nGive me a positive integer: '))
    
    print(FibonacciNumber(num))