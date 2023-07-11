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

    def min(self):
        """Минимальное значение в массиве."""
        min_v = self.data[0]
        for idx in range(1, self.length):
            val = self.data[idx]
            if val < min_v:
                min_v = val
        return min_v

    def max(self):
        """Максимальное значение в массиве."""
        max_v = self.data[0]
        for idx in range(1, self.length):
            val = self.data[idx]
            if val > max_v:
                max_v = val
        return max_v

    def avg(self):
        """Среднее значение в массиве."""
        if self.length > 0:
            avg_v = sum(self.data[idx] for idx in range(self.length))
            return avg_v / self.length

    def __str__(self):
        """Возвращает все элементы массива в виде строки."""
        return "[" + ", ".join(map(str, self.data[:self.length])) + "]"


# array = Array(6)
# print(array.__str__())
# print('size', array.size)
# print('ln', array.length)
# array.append(0)
# array.append(-8000000000)
# array.append(99999999999)
# print(array.__str__())
# print('size', array.size)
# print('ln', array.length)
# print('min', array.min())
# print('max', array.max())
# print('avg', array.avg())