def linear_search(lst, search):
    idx_lst = []
    for idx, value in enumerate(lst):
        if value == search:
            idx_lst.append(idx)
    return idx_lst or -1
