def countingsort(values):
    """
    Сортировка подсчетом.
    """
    # Вычисляем max_value.
    min_value = max_value = values[0]
    for value in values[1:]:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    # Вычисляем размер массива.
    array_size = abs(min_value) + abs(max_value) + 1


    # Создаем массив-счетчик.
    # Складываем абсолютные значения min_value и max_value.
    counts = [0] * array_size

    # Считаем количество значений основного массива.
    for value in values:
        counts[value] += 1

    # Копируем значения обратно в массив.
    index = 0
    for i in range(array_size):
        for j in range(counts[i]):
            values[index] = i - abs(min_value)
            index += 1

    return values


print(countingsort([-1, -2, -3, 1, 1, -1, -2, 1, -1, 0, 0]))