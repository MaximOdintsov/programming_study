def merge(list1, list2):
    merge_list = []
    for _ in range(len(list1)+len(list2)):
        rm_l1 = False

        if list1 and list2:
            if list1[0] <= list2[0]:
                merge_list.append(list1[0])
                rm_l1 = True
            elif list1[0] >= list2[0]:
                merge_list.append(list2[0])

        elif list1:
            merge_list.append(list1[0])
            rm_l1 = True
        elif list2:
            merge_list.append(list2[0])

        # Удаляем значение, которое уже вставили в новый массив
        list1.remove(list1[0]) if rm_l1 else list2.remove(list2[0])

    return merge_list


# array1 = [3, 4, 7, 8, 9]
# array2 = [1, 4, 5, 9]
# array = merge([1, 3, 5, 7, 9], [2, 4, 6])
# print(array)