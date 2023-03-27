def linearSearch(list, value):
    for i in list:
        if i == value:
            return True
    return False

def binarySearch(list, value):
    left, right = 0, len(list) - 1
    while left <= right:
        mid = (left + right) // 2
        print(left, mid, right)
        if list[mid] == value:
            return True
        elif list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return False




data = [10,20,30,40,50,60,70,80,90,100,110,120]
print(binarySearch(data, 10))