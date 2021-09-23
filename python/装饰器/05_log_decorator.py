import time

"""
通过装饰器进行函数增强,只是一种语法糖,本质上跟上个程序完全一致.
"""


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


@log_wrapper
def print_odds():
    """
    输出0~100之间所有奇数,并统计函数执行时间
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)

if __name__ == '__main__':
    print_odds()
