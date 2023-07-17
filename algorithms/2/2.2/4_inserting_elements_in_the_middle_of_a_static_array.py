class Array:
    """Линейный ститический массив."""
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

    def insert(self, index, value):
        """
        Добавление нового элемента со значением value на позицию index.
        """
        if self.length < self.size:
            self.append(value)
            idx = self.length - 1
            while idx > index:
                self.data[idx], self.data[idx - 1] = self.data[idx - 1], self.data[idx]
                idx -= 1
            return
        raise OverflowError

    def __str__(self):
        """Возвращает все элементы массива в виде строки."""
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


# array = Array(5)
# array.append(20)
# array.append(10)
# array.append(30)
# array.insert(1, 40)
# print(array)
# array.insert(20, 50)
# print(array)
# array.insert(2, 50)