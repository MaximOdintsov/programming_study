class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.length = 0
        self.size = size

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


class Stack(Array):
    """
    Стек на базе статического массива.
    """

    def pop(self):
        """
        Извлекает элемент из стека.
        """
        value = self.data[self.length-1]
        if self.length:
            self.length -= 1
            self.data[self.length] = None
        return value

    def push(self, value):
        """
        Извлекает элемент со значением value в стек.
        """
        if self.size > self.length:
            self.data[self.length] = value
            self.length += 1
        else:
            raise OverflowError


stack = Stack(3)
stack.push(12)
stack.push(7)
stack.push(6)
# stack.push(8)
# ...
# OverflowError
print(stack.pop())
6
print(stack.pop())
7
print(stack.pop())
12
print(stack.pop())
None