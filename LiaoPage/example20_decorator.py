# _*_ coding: utf-8 _*_
# ---------------example 1-------------------
import functools
import time


def log(func):
    @functools.wraps(func)  # make the name attribute of original function not change
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log
def now():
    print('2020-8-18')


now()
# ---------------example 2-------------------


def log2(text):
    def decorator(func):
        @functools.wraps(func)  # make the name attribute of original function not change
        def wrapper2(*arg, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*arg, **kw)
        return wrapper2
    return decorator


@log2('execute')
def now():
    print('2020-8-18')


now()
# ---------------exercise 1-------------------


def metric(fn):
    @functools.wraps(fn)
    def wrapper3(*arg, **kw):
        start = time.time()
        tmp = fn(*arg, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end-start))
        return tmp
    return wrapper3
# test


@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功!')
# ---------------exercise 2-------------------


def log3(func):
    @functools.wraps(func)
    def wrapper4(*arg, **kw):
        print('begin call %s()' % func.__name__)
        func(*arg, **kw)
        print('end call %s()' % func.__name__)
        return
    return wrapper4


@log3
def now():
    print('2020-8-18')


now()
# ---------------exercise 2-------------------


def log5(text):
    if isinstance(text, str):
        def decorator2(func):
            @functools.wraps(func)
            def wrapper5(*arg, **kw):
                print('%s %s:' % (text, func.__name__))
                return func(*arg, **kw)
            return wrapper5
        return decorator2
    else:
        def wrapper6(*arg, **kw):
            print('call %s():' % text.__name__)
            return text(*arg, **kw)
        return wrapper6


@log5
def now():
    print('2020-8-18')


now()


@log5('execute')
def now():
    print('2020-8-18')


now()
