import time
"""
通过闭包增强主要功能函数print_odds,给它增加一个统计时间功能
缺点: 需要显式进行闭包增强
"""


def print_odds():
    """
    输出0~100之间所有奇数,并统计函数执行时间
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


# 闭包本质上是一个函数
# 闭包函数的传入参数和返回值也都是函数
# 闭包函数的返回值函数是对传入函数进行增强后的结果
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


if __name__ == '__main__':
    # 调用count_time_wrapper增强函数
    print_odds = count_time_wrapper(print_odds)
    print_odds()# improved
    print_odds()# improved
    print_odds()# improved
    print_odds()# improved
    print_odds()# improved







