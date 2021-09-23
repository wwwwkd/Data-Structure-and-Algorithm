# 递归的两个特点，1.调用自身，2.终止条件

# 先print 后递归
def func1(x):
    if x > 0:
        print(x)
        func1(x-1)

# 先递归，后print
def func2(x):
    if x > 0:
        func2(x-1)
        print(x)

print(func1(3))
print(func2(3))

# 汉诺塔问题
count = 0
def hanoi(n, a, b, c):
    global count
    if n>0:
        hanoi(n-1, a, c, b)
        count += 1
        print('第 %s 步： 从 %s 位置移动到 %s 位置' % (count, a, c))
        hanoi(n-1, b, a, c)

hanoi(2, "a", "b", "c")


def hanoi2(n, a, b, c):
    global count
    if n > 0:
        hanoi2(n-1, a, c, b)
        count += 1
        print('第 %s 步，从 %s 柱子 ----> %s 柱' % (count, a, c))
        hanoi2(n-1, b, a, c)

print(hanoi2(2, "a", "b", "c"))