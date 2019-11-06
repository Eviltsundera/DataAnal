from functools import wraps

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if wrapper.level == 0:
            wrapper.ncalls = 0
            wrapper.rdepth = 0
        wrapper.ncalls += 1
        wrapper.level += 1
        wrapper.rdepth = max(wrapper.rdepth, wrapper.level)
        res = func(*args, **kwargs)
        #print ("{0} была вызвана: {1}".format(func.__name__, func.count))
        wrapper.level -= 1
        return res
    wrapper.ncalls = 0
    wrapper.rdepth = 0
    wrapper.level = 0
    return wrapper

@counter
def func2(n, steps):
    if steps == 0:
        return

    func2(n + 1, steps - 1)
    func2(n - 1, steps - 1)

if __name__ == "__main__":
    func2(0, 5)
    print(func2.ncalls, func2.rdepth)

    func2(0, 3)
    print(func2.ncalls, func2.rdepth)