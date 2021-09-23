import time


def count_time_wrapper(func):
    """
    闭包,用于增强函数func: 给函数func增加统计时间的功能
    """

    def improved_func():
        start_time = time.clock()   # 起始时间
        func()                      # 执行函数
        end_time = time.clock()     # 结束时间
        print("it takes {} s to find all the olds".format(end_time - start_time))


    return improved_func


def count_odds(lim=100):
    """
    输出0~lim之间所有奇数,并统计函数执行时间
    """
    cnt = 0
    for i in range(lim):
        if i % 2 == 1:
            cnt+=1
    return cnt


# 对于含有返回值的函数,调用闭包增强后,不能成功返回,但是成功增强了辅助功能
# 对于含有参数的函数,调用闭包增强后,不能成功接收参数
# if __name__ == '__main__':
#     print('增强前')
#     print(count_odds())         # 装饰前函数能正常返回,能接收参数
#     print('----------------------')
#     print('增强后')
#     count_odds = count_time_wrapper(count_odds)
#     print(count_odds())         # 装饰后函数不能正常返回,不能接收参数

if __name__ == '__main__':
    print('增强前')
    print(count_odds(lim=10000))         # 装饰前函数能正常返回,能接收参数
    print('----------------------')
    print('增强后')
    count_odds = count_time_wrapper(count_odds)
    print(count_odds(lim=10000))         # 装饰后函数不能正常返回,不能接收参数
