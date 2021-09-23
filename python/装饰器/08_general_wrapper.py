def general_wrapper(func):

    def improved_func(*args, **kwargs):    # 接收函数参数
        # 增强功能
        ret = func(*args, **kwargs)        # 传入参数并记录返回值
        # 增强功能
        return ret                         # 返回未增强函数的返回值

    return improved_func
