import time


def get_the_fastest_func(funcs: list, arg):
    result = float('inf')
    result_func = ''
    for func in funcs:
        stat = time.perf_counter()
        n = func(arg)
        end = time.perf_counter()
        func_time = end - stat
        if func_time < result:
            result = func_time
            result_func = func
    return result_func



