
class Solution():
    def sequential_search(self, alist, target):
        pos = 0
        find = False
        while not find and pos < len(alist):
            if int(alist[pos]) == target:
                find = True
                return find
            else:
                pos += 1

alist = list(map(int, input().split()))
res = Solution()

print(res.sequential_search(alist, 0))
