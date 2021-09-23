def bubbleSort(alist):
    for j in range(len(alist)-1):
        for i in range(len(alist)-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
    return alist

alist = [3, 8, 5, 7, 6]
print(bubbleSort(alist))
