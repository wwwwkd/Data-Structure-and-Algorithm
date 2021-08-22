# 二分查找

def find(alist, item):
    find = False
    mid_index = len(alist)//2
    first = 0
    last = len(alist)-1

    while first <= last:
        mid_index = (first+last)//2
        if alist[mid_index] < item:
            first = mid_index + 1
        if alist[mid_index] > item:
            last = mid_index - 1
        else:
            find = True
            break
    return find

alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(find(alist, 2))