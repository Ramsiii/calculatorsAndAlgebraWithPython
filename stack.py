class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        else:
            raise IndexError("Stack is empty.")

    def is_empty(self):
        return len(self.elements) == 0

if __name__ == '__main__':
    stack = Stack()

    # stack.pop()
    # print(stack.pop())

    stack.push(1)
    stack.push(2)

    print(stack.pop())
    print(stack.is_empty())
