import traceback
# 不可变对象：不可变对象被修改会创建新的对象
# 不可变对象 int/float str/tuple set dice-key
i = 1
print('原始i的地址:',id(i))
i += 1
print('修改i后的地址:',id(i))

str = 'hello'
print('原始str的地址:',id(str))
str += 'world'
print('修改str后的地址:',id(str))


set_mutable = set([1,2,3])
print('原始set_mutable的地址:',id(set_mutable))
try:
    set_mutable = set([[1,2],[2,3],[3,4]])
    print('修改set_mutable后的地址:', id(set_mutable))
except:
    info = traceback.format_exc()
    print(info)
print('-'*25)

# 可变对象：可变对象被修改不会创建新的对象
set = set()
print('原始set的地址:',id(set))
set.add(1)
print('修改set后的地址:',id(set))
