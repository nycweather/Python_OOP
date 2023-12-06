def rob(nums):
    choice1 = choice2 = 0
    for n in nums:
        temp = max(n+choice1, choice2)
        print("top        1:", choice1, "  2:", choice2, "  temp:", temp)
        choice1 = choice2
        choice2 = temp
        print("bottom     1:", choice1, "  2:", choice2, "  temp:", temp, end='\n\n')
    return choice2


houses = [6, 7, 99, 30, 8, 2, 19]
print(rob(houses))
