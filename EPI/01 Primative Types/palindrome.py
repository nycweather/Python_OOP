"""
Return if a decimal number is a palindrome
131 -> True
123 -> False
"""
def palindrome(num: int)-> bool:
    if num < 10:
        return True
    return False

print(palindrome(11))
    
