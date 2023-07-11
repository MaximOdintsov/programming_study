class Array:
    """
    Линейный ститический массив.
    """

    def __init__(self, size):
        # Данные массива, изначально массив пустой и все его элементы заполнены None.
        # То есть сразу выделяем массив фиксированного объема.
        self.data = [None] * size

        # Длина заполнненого массива.
        # По умолчанию 0, так как массив пустой.
        self.length = 0

        # Полный размер массива.
        self.size = size

    def append(self, value):
        """
        Добавление нового элемента в конец линейного массива.
        Время работы O(1).
        """
        if self.size >= self.length + 1:
            self.data[self.length] = value
            self.length += 1
            return
        raise OverflowError

    def __str__(self):
        """
        Возвращает все элементы массива в виде строки.
        """
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


# array = Array(3)
# print(array.size)
# print(array.length)
# print(array)
# array.append(20)
# array.append(10)
# array.append(30)
# print(array)
# array.append(40)