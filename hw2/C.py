import time
from functools import wraps

def timeout(rps):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            t_beg = time.time()
            ans = func(*args, **kwargs)
            dtime = 1 / rps + t_beg - time.time()
            if dtime > 0:
                time.sleep(dtime)
            return ans
        return wrapper
    return decorator
