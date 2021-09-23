name=('jack','beginman','sony','pcky')
age=(2001,2003,2005,2000)
x = zip(name,age)
print(list(x))
for a,b in x:
    print(a)
    print(b)
    x = 1
print(x)
