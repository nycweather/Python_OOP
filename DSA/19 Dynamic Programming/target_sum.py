def target_sum(num, arr):
    if num == 0:
        return 1
    if num < 0:
        return 0
    for n in arr:
        if target_sum(num-n, arr):
            return 1 + target_sum(num-n, arr)
    return 0

print(target_sum(3, [1,1,1,1,1]))