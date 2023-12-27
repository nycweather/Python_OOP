lookup = {}


def number_factor_top_down(num, lookup):
    if num in (0, 1, 2):
        return 1
    elif num == 3:
        return 2
    else:
        if num not in lookup:
            case1 = number_factor_top_down(num-1, lookup)
            case2 = number_factor_top_down(num-3, lookup)
            case3 = number_factor_top_down(num-4, lookup)
            lookup[num] = case1+case2+case3
        return lookup[num]


def number_factor_bottom_up(num):
    arr = [1, 1, 1, 2]
    for i in range(4, num+1):
        arr.append(arr[i-1]+arr[i-3]+arr[i-4])
    return arr[num]


print(number_factor_top_down(29, lookup))
print(number_factor_bottom_up(29))
