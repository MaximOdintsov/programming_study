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
        for idx in range(len(self.data)-1, -1, -1):
            if self.data[idx] == value:
                self.data.remove(self.data[idx])
                self.data.append(None)
                self.length -= 1

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


# print('------------------------------------')
# array = Array(5)
# array.append(6)
# array.append(2)
# array.append(1)
# array.append(2)
# array.append(9)
# print(array)
#
# print('------------------------------------')
# array.remove(2)
# print(array)
#
# print('------------------------------------')
# array.remove(6)
# print(array)
#
# print('------------------------------------')
# array = Array(6)
# print(array.__str__())
# print(array.size)
# print(array.length)
#
# print('------------------------------------')
# array.append(7)
# array.append(7)
# array.append(4)
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