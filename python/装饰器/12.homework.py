import time

def log_wrapper(info='Everything works'):
    def internal_log_wrapper(func):
        def improved_func():
            start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 起始时间
            func()  # 执行函数
            end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 结束时间
            print("Logging: func:{} runs from {} to {}, info:[{}]".format(func.__name__, start_time, end_time, info))

        return improved_func
    return internal_log_wrapper


@log_wrapper(info='informmmmmmmm')
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
