def compound(amount, year_percent, months):
    """
    Вычисление сложного процента
    (НЕОПТИМАЛЬНЫЙ)
    """
    month_percent = year_percent/12 

    for _ in range(months):
        percent = amount * (month_percent / 100)
        amount += percent
    return amount

print(compound(100000, 10, 12))


def compound(amount, year_percent, months):
    """
    Вычисление сложного процента
    (ОПТИМАЛЬНЫЙ)
    """
    month_percent = year_percent/12 
    return amount * (1 + month_percent / 100)**months

print(compound(100000, 10, 12))