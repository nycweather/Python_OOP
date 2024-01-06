"""
Write a program to print out the number of bits set to one from a non negative integer
num = 1000 -> 0b1111101000 or 1000
Shifting down two places
num = num >> 2 -> 0b11111010 or 250
print(6 & 4) # 4
print(1 | 2) # 3
print(8 >> 1) # 4
print(-16 >> 2) # -4
print(~0) # -1
print(15 ^ 1) # 14
"""

def count_bits(num: int) -> int:
    num_bits = 0
    while num:
        print("before", num_bits, num)
        num_bits += num | 0
        num >>= 1
        print("after", num_bits, num)
    return num_bits

def flip_bits(num):
    print("Binary:", bin(num))
    print("Bitwise | OR:", bin(num | 0))
    print("Bitwise & AND:", bin(num & 0))
    print("Bitwise ^ XOR:", bin(num ^ 0))
    print("Bitwise ~ NOT:", bin(~num))
    print("Bitwise >> Right Shift:", bin(num >> 1))
    print("Bitwise << Left Shift:", bin(num << 1))



print(flip_bits(0))
