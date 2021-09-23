import time


def count_time_wrapper(func):
    """
    闭包,用于增强函数func: 给函数func增加统计时间的功能
    """

    def improved_func():
        start_time = time.clock()  # 起始时间
        func()  # 执行函数
        end_time = time.clock()  # 结束时间
        print("it takes {} s to find all the olds".format(end_time - start_time))

    return improved_func


def log_wrapper(func):
    """
    闭包,用于增强函数func: 给func增加日志功能
    """

    def improved_func():
        start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 起始时间
        func()  # 执行函数
        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 结束时间
        print("Logging: func:{} runs from {} to {}".format(func.__name__, start_time, end_time))

    return improved_func


@count_time_wrapper
@log_wrapper
def count_odds():
    """
    输出0~100之间所有奇数,并统计函数执行时间
    """
    cnt = 0
    for i in range(100):
        if i % 2 == 1:
            cnt += 1
    return cnt


if __name__ == '__main__':
    count_odds()
