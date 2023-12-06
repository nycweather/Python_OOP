def fib(num):
    arr = [0,1]
    for _ in range(num-1):
        temp = arr[0] + arr[1]
        arr[0] = arr[1]
        arr[1] = temp
    return arr[1]

print(fib(100_000))