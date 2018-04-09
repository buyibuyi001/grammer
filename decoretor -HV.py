# 如何实现属性可修改的函数装饰器
# 1 统计被装饰函数单次调用运行时间
# 2 时间大于参数timeout的，记录到log日志中
# 3 运行时可修改timeout的值

import time
import logging
from functools  import wraps


def warn(timeout):   #这一层取得装饰器的参数

    def decorator(func):  # 这一层取得 被装饰函数的名字

        def wrapper(*args,**kargs): # 这一层取得 被装饰函数的参数

            start =time.time()

            res= func(*args,**kargs)
            used = time.time()-start

            if used >timeout:
                msg= " %s %s > %s"%(func.__name__,used,timeout)
                logging.warn(msg)
            return res

        def settimeout(k):
            nonlocal timeout
            timeout =k

        wrapper.settimeout = settimeout

            
        return wrapper   # 这是被装饰函数的引用对象
    return decorator

from random import randint
@warn(1.5)
def test():
    print("In test")

    while randint(0,1):
        time.sleep(0.5)
for i in range(30):
    test()

#  对python2 可以用列表改timeout值。
test.settimeout(1)
for i in range(30):
    test()
