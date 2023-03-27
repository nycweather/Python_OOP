'''
Write a function that takes x and y, then returns x^y
'''

def power(x: float, y:int) -> int:
    result = x
    while y-1:
        result *= x
        y -= 1
    return result


print(3**4)
print(power(3, 4))