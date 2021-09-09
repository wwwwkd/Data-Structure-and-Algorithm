# 最初想法，没有优化，会产生overlapping
def lcs(str1, str2, m, n):
    if m == 0 or n == 0:
        return 0
    if str1[m-1] == str2[n-1]:
        case1 = 1 + lcs(str1,str2,m-1,n-1)
        return case1
    else:
        case2 = max(lcs(str1,str2,m,n-1),lcs(str1,str2,m-1,n))
        return case2

# 从上到下，拿空间换时间，把运行运行过的结果，放在一个m,n的矩阵中
def lcs_updown(str1, str2, m, n):
    if m == 0 or n == 0:
        dp[m][n] = 0
        return 0
    if str1[m - 1] == str2[n - 1]:
        case1 = 1 + lcs(str1, str2, m - 1, n - 1)
        return case1
    else:
        case2 = max(lcs(str1, str2, m, n - 1), lcs(str1, str2, m - 1, n))
        return case2
str1 = 'ASD'
str2 = 'AXD'
m, n = len(str1), len(str2)
dp = [[-1] * (n-1) for _ in range(m+1)]
print(dp)
