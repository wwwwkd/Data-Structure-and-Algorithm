import time


def count_time_wrapper(func):
    """
    闭包,用于增强函数func: 给函数func增加统计时间的功能
    """

    def improved_func(*args, **kwargs):     # 增强函数应该把就饿收到的所有参数传给原函数
        start_time = time.clock()   # 起始时间
        ret = func(*args, **kwargs)                     # 执行函数
        end_time = time.clock()     # 结束时间
        print("it takes {} s to find all the olds".format(end_time - start_time))
        return ret      # 增强函数的返回值应该是原函数的返回值

    return improved_func


def count_odds(lim=100):
    """
    输出0~100之间所有奇数,并统计函数执行时间
    """
    cnt = 0
    for i in range(lim):
        if i % 2 == 1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(count_odds(lim=100000))  # 装饰前函数能正常返回,能接收参数
    print('-----------')
    count_odds = count_time_wrapper(count_odds)
    print(count_odds(lim=100000))  # 装饰后函数不能正常返回,不能接收参数
