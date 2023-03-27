"""
Reverse given number 
example 
42 -> 24
-123 -> 321
"""

def reverse(num):
    new = abs(num)
    result = 0
    placeholder = 0
    while new:
        placeholder = new % 10
        result *= 10
        result += placeholder
        new //= 10
    return -result if num < 0 else result

print(reverse(-12223))