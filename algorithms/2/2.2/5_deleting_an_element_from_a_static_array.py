class Array:
    """
    Линейный ститический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполненного массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.length == self.size:
            raise OverflowError
        self.data[self.length] = value
        self.length += 1

    def remove(self, value):
        for idx in range(len(self.data)):
            if self.data[idx] == value:
                self.data[idx] = None

                index = idx + 1
                while self.length > index and self.data[index] is not None:
                    self.data[index-1], self.data[index] = self.data[index], self.data[index-1]
                    index += 1

                self.length -= 1
                return

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


# print('------------------------------------')
# array = Array(4)
# print(array)
# print(array.size)
# print(array.length)
#
# print('------------------------------------')
# array.append(7)
# array.append(5)
# array.append(9)
# array.append(3)
# print(array)
# print(array.size)
# print(array.length)
#
# print('------------------------------------')
# array.remove(7)
# print(array)
# print(array.size)
# print(array.length)