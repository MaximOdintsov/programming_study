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
    Двойной стек на базе статического массива.
    """

    def __init__(self, size):
        super().__init__(size)
        self.top_left = 0
        self.top_right = -1

    def push_left(self, value):
        """
        Добавляет элемент со значением value в стек слева.
        """
        if self.data[self.top_left] is None:
            self.data[self.top_left] = value
            self.length += 1
            return self.data[self.top_left]

        if self.top_left+1 <= self.size-1 and self.data[self.top_left+1] is None:
            self.data[self.top_left+1] = value
            self.top_left += 1
            self.length += 1
        else:
            raise OverflowError

    def push_right(self, value):
        """
        Добавляет элемент со значением value в стек справа.
        """
        if self.data[self.top_right] is None:
            self.data[self.top_right] = value
            self.length += 1
            return self.data[self.top_right]

        if self.top_right-1 <= self.size-1 and self.data[self.top_right-1] is None:
            self.data[self.top_right-1] = value
            self.top_right -= 1
            self.length += 1
        else:
            raise OverflowError

    def pop_left(self):
        """
        Извлекает элемент из стека слева.
        """
        if self.top_left >= 0 and self.data[self.top_left] is not None:
            value = self.data[self.top_left]
            self.data[self.top_left] = None
            self.top_left -= 1 if self.top_left >= 1 else 0
            self.length -= 1
            return value
        return None

    def pop_right(self):
        """
        Извлекает элемент из стека справа.
        """
        if self.top_right <= -1 and self.data[self.top_right] is not None:
            value = self.data[self.top_right]
            self.data[self.top_right] = None
            self.top_right += 1 if self.top_right <= -2 else 0
            self.length -= 1
            return value
        return None

    def clear(self):
        """
        Очищает стек.
        """
        self.__init__(self.size)

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        Используем size, так как массив теперь заполняется с двух сторон.
        """
        return "[" + ", ".join(map(str, self.data[:self.size])) + "]"

#
# stack = Stack(4)
# stack.push_left(12)
# stack.push_left(7)
# stack.push_left(6)
# stack.push_right(8)
# stack.push_left(3)
# ...
# OverflowError
# print(stack.pop_left())
# 6
# print(stack.pop_right())
# 8
# print(stack.pop_right())
# None