def linear_search(lst, search):
    for idx, value in enumerate(lst):
        if value == search:
            return idx
    return -1