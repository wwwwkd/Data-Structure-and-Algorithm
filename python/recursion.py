'''

     1. ` 调用自身 `
     2. ` 结束条件 `

'''

def func1(x):
    if x > 0:
        print(x)
        func1(x - 1)

def func2(x):
    if x > 0:
        func2(x - 1)
        print(x)


func1(3)
func2(3)

# 汉诺塔问题
def hanoi(n,a,b,c):
    if n > 0: # 终止条件
        hanoi(n-1,a,c,b)
        print('把 %s 圆盘 从 %s 位置移动到 %s 位置'%(n, a, c))
        hanoi(n-1,b,a,c)

hanoi(1,'a', 'b', 'c')

