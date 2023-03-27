def rob(n):
    if len(n) == 0:
        return 0
    for i in range(len(n)):
        first = n[i] + rob(n[i+2:])
        second = rob(n[i+1:])
        return max(first, second)

houses = [6,7,1,30,8,2]
print(rob(houses))