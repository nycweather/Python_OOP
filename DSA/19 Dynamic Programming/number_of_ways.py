def number_of_ways(n, m, table={}):
    key = f'{n},{m}'
    if key in table:
        return table[key]
    if n == 0 or m == 0:
        return 0
    elif n == 1 and m == 1:
        return 1
    table[key] = number_of_ways(n-1, m, table) + number_of_ways(n, m-1, table)
    return table[key]


print(number_of_ways(100, 100))
