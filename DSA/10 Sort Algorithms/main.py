def bubbleSort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    print(list)

def selectionSort(list):
    for i in range(len(list)):
        min = i
        for j in range(i, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    print(list)

def insertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        prev = i - 1
        while prev >= 0 and key < list[prev]:
            list[prev+1] = list[prev]
            prev -= 1
        list[prev+1] = key
    print(list)

def merge(list, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    Left = [0] * (n1)
    Right = [0] * (n2)

    for i in range(0, n1):
        Left[i] = list[l+i]

    for j in range(0, n2):
        Right[j] = list[m+1+j]
    
    i = 0
    j = 0
    k = l
    while i < n1 and j<n2:
        if Left[i] and Right[j]:
            list[k] = Left[i]
            i += 1
        else:
            list[k] = Right[j]
            j += 1
        k += 1
    while i < n1:
        list[k] = Left[i]
        i += 1
        k += 1
    while j < n2:
        list[k] = Right[j]
        j += 1
        k += 1

def mergeSort(list, l, r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(list, l, m)
        mergeSort(list, m+1, r)
        merge(list, l, m, r)
    return list


my_list = [7,8,5,2,4,6,7,8,9]
print(mergeSort(my_list, 0, 8))