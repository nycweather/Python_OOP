def numFactor(num):
    if num < 3:
        return 1
    elif num == 3:
        return 2
    else:
        case1 = numFactor(num-1)
        case2 = numFactor(num-3)
        case3 = numFactor(num-4)
        return case1+case2+case3


print(numFactor(4))
