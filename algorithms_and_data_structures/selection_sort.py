def selection_sort(values: list or tuple):
    print(f'start: {values}')
    
    for i in range(len(values)):
        min_index = i

        for j in range(i+1, len(values)):
            if values[min_index] > values[j]:
                min_index = j
        if i != min_index:
            values[min_index], values[i] = values[i], values[min_index]
            print(f'{i} iteration: {values}')
    print(f'end: {values}')


print(selection_sort([0, 8, 9, 1, -3, -1, 1000000, -1000000, 5]))