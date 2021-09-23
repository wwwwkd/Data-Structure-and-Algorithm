# keys() 该方法会返回字典的所有的key
#  该方法会返回一个序列，序列中保存有字典的所有的键
d = {'name':'孙悟空','age':18,'gender':'男'}
print('字典所有的键\n',d.keys())
for key in d.keys():
    print(key,'value:',d[key])
print('-'*25)

# values()
# 该方法会返回一个序列，序列中保存有字典的所有的值
d = {'name':'孙悟空','age':18,'gender':'男'}
print('字典所有的值\n',d.values())
for v in d.values():
  print(v)
print('-'*25)

# items()
# 该方法会返回字典中所有的项
# 它会返回一个序列，序列中包含有双值子序列
# 双值分别是，字典中的key和value
d = {'name':'孙悟空','age':18,'gender':'男'}
print('字典所有的项\n',d.items())
for k,v in d.items():
  print(k, '=', v)