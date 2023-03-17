# ГЕНЕРАТОРЫ СПИСКА

one_cycle = [i for i in range(1, 11) if i % 2 == 0]
print(one_cycle)

# Сначала идет первый цикл и условие, применяемое к нему, после чего идет 2 цикл с условием
two_cycles = [[i, j] for i in range(1, 11) if i % 2 != 0 for j in range(1, 11) if j % 2 == 0]
print(two_cycles)


string = 'fsfkopFK3029KRpKF031{pef-1]dp21das'

string_filter = [int(symbol) for symbol in string if symbol.isdigit()]
print(string_filter)

