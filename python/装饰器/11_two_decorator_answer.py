def wrapper1(func1):
    print('set func1')

    def improved_func1():
        print('call func1')
        func1()     # 封装了improve_func2(original_func)

    return improved_func1


def wrapper2(func2):
    print('set func2')

    def improved_func2():
        print('call func2')
        func2()     # 封装了original_func

    return improved_func2


# @wrapper1
# @wrapper2
def original_func():
    pass


if __name__ == '__main__':
    # original_func = wrapper1(wrapper2(original_func))

    original_func = wrapper2(original_func)
    print(original_func.__name__)
    original_func = wrapper1(original_func)
    print(original_func.__name__)
    # original_func封装了improved_func1(improve_func2(original_func))


    original_func()
    print('-----')
    original_func()

