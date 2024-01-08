import time


def timer(func: callable):
    def wrapper(**kwargs):
        template = 'time taken for {}: {:3.2f} ms'
        start = time.time()
        res = func(**kwargs)
        end = time.time()
        print(template.format(func.__name__, (end-start)*1000))
        return res
    return wrapper
