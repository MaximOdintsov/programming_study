def bubblesort(array):
    """
    Алгоритм пузырьковой сортировки массива в прямом порядке.
    """

    # Модифицируйте алгоритм.
    is_sorted = False
    while not is_sorted:

        is_sorted = True
        n = 1

        for i in range((len(array) - n), 0, -1):
            if array[i] > array[i - 1]:
                array[i], array[i - 1] = array[i - 1], array[i]
                is_sorted = False

        n += 1
    return array


# array = [1, 2, 3, 4, 349494, -2, -129223, -1, 3933, 9999999999999, -99999999999999, 0, -122]
# print(bubblesort(array=array))
