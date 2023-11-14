def sum_of_digit(nums):
    if nums == 0:
        return 0
    return (nums % 10) + sum_of_digit(nums // 10)

print(sum_of_digit(1234))
