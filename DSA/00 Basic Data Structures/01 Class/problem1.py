'''
Input: laboratory, rat
Output: true

Input: cat, meow
Output: false

Input: Understand, and
Output: True

Input: theory, joy
Output: False

Input: any, ""
Output: True

Input: "", word
Output: False
'''

def is_substring(word1, word2):
    if word1 == "" or word2 == "":
        return False
    if len(word1) > len(word2):
        return False
    for i in range(len(word2)):
        if word1[0] == word2[i]:
            if word1 == word2[i:i+len(word1)]:
                return True
    return False

print(is_substring("rat", "laboratory"))
