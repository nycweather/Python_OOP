import hashlib

salt = '544e8fb402fc'
hashed = 'a35dfd0ece389f56c12cdd9f5a8eaa96'

# check if word plus salt is equal to the hashed password
with open('/Users/alif/Documents/code/Python_OOP/Ramp/word-list-7-letters.txt', 'r') as f:
    for line in f:
        word = line.strip().lower()
        if hashlib.md5((word + salt).encode()).hexdigest() == hashed:
            print("Password found:", word)
            break
