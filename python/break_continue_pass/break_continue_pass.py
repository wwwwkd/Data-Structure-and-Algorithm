# break 强制终止
def break_test():
    number = 0
    for number in range(10):
        if number == 5:
            break
        print('Number is' + str(number))

    print('Out of loop')

# continue 继续循环，但是把本次循环continue以后的句子忽略，然后开始下次循环
def continue_test():
    number = 0
    for number in range(10):
        if number == 5:
            continue
        print('Number is ' + str(number))

    print('Out of loop')

#continue_test()

# exit()直接结束程序
for element in "Python":
     if element == "t":
         exit()
     else:
        print(element)
print('a')