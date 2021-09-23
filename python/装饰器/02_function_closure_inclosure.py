import time

"""
将辅助功能(记录时间)抽离成一个辅助函数count_time,在辅助函数count_time中调用主要功能函数print_odds.
- 优点: 解耦,函数职责分离.
- 缺点: 要通过辅助函数来调用主要功能函数,不方便.
> 我们的目标: 能不能在调用主要功能函数时自动完成对时间的统计?
"""


def count_time(func):
    """
    统计某个函数的运行时间
    """
    start_time = time.clock()  # 起始时间
    func()  # 执行函数
    end_time = time.clock()  # 结束时间
    print("it takes {} s to find all the olds".format(end_time - start_time))


def print_odds():
    """
    输出0~100之间所有奇数,并统计函数执行时间
    """
    for i in range(100):
        if i % 2 == 1:
            print(i)


if __name__ == '__main__':
    # print_odds()
    count_time(print_odds)
