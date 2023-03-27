'''
Write a function to determine if a number is odd
'''

def is_odd(num):
    return bin(num)[-1] == 1

def parity(x):
    result = 0
    while x:
        print(x)
        result ^= x & 1
        print(result)
        x &= x - 1
    return result


print(parity(202))