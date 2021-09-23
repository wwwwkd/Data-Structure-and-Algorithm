import time

"""
通过装饰器进行函数增强,只是一种语法糖,本质上跟上个程序完全一致.
"""


def count_time_wrapper(func):
    """
    闭包,用于增强函数func: 给函数func增加统计时间的功能
    """

    def improved_func():
        start_time = time.clock()  # 起始时间
        func()  # 执行函数
        end_time = time.clock()  # 结束时间
        print(
            "it takes {} s to find all the olds".format(end_time - start_time))

    return improved_func


@count_time_wrapper
def print_odds():
    """
    输出0~100之间所有奇数,并统计函数执行时间
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    # 装饰器等价于在第一次调用函数时执行以下语句:
    # print_odds = count_time_wrapper(print_odds)
    print_odds()
