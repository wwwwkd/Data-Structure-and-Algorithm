# class Fib():
#     def __init__(self):
#         self.a, self.b = 0, 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.a, self.b = self.b, self.a+self.b
#         if self.a > 10000:
#             raise StopIteration()
#         return self.a
# def fib():
#     a,b = 0,1
#     while 1:
#         a,b = b,a+b
#         yield a
# for f in fib():
#     if f < 10000:
#         print(f)
#     else:
#         break
# res = Fib()
# for i in res:
#     print(i)

# 斐波那契数列
'''
1
1
2
3
5
8
'''
class Fib():
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        cur = self.b
        self.b += self.a
        self.a = cur
        if self.a < 10000:
            return self.a
        else:
            raise StopIteration
def fib_yeid():
    a, b = 0, 1
    while 1:
        a, b = b, a+b
        yield a

def feild_2(n):
    a, b = 0, 1
    max = 0
    list = []
    while max <= n:
        a, b = b, a+b
        list.append(a)
        max += 1


fib = Fib()
for i in fib_yeid():
    print(i)