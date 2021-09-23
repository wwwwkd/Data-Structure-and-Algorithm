def chooseSort(alist):
    for j in range(len(alist)-1):
        max_index = 0
        for i in range(1, len(alist)-j):
            if alist[max_index] < alist[i]:
                max_index = i
        alist[len(alist)-1-j], alist[max_index] = alist[max_index], alist[len(alist)-1-j]
    return alist
alist = [3, 8, 5, 7, 6]
print(chooseSort(alist))