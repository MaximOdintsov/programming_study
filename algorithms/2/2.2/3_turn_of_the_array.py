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

    def reverse(self):
        """
        Разворачивает массив.
        """
        new_data = [elem for elem in self.data if elem is not None]
        for idx, val in enumerate(new_data):

            if idx < self.length / 2:
                new_data[idx], new_data[-idx-1] = new_data[-idx-1], new_data[idx]
            else:
                break
        self.data = new_data

    def __str__(self):
        """Возвращает все элементы массива в виде строки."""
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


# array = Array(6)
# print(array.__str__())
# print(array.size)
# print(array.length)
# array.append(7)
# array.append(5)
# array.append(9)
# array.append(3)
# array.reverse()
# array.reverse()
# print(array.__str__())