class IT(object):
    def __init__(self):
        self.counter = 0
    def __iter__(self):
        return  self
    def __next__(self):
        self.counter += 1
        if self.counter == 3:
            raise StopIteration()
        return self.counter

#根据实例化创建一个迭代器对象
obj1 = IT()

v1 = next(obj1)
print(v1)

v2 = next(obj1)
print(v2)

v3 = next(obj1)
print(v3)

obj2 = IT()
for item in obj2:
    print(item)
