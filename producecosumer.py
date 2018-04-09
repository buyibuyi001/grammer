def consumer():
    product = 'firt'
    while True:
        n = yield product

        print('[CONSUMER] Consuming %s...' % n)
        product = '200 OK  %s'%(n)

def produce(c):
    first=next(c)   # to start up the generator
    print(first)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)

#函数只要包含yield则成为生成器，生成器必须由None 开启
#func().send(None);func().send(1) is not the same as c=func();c.send(None);c.send(1)
#c.send(None),c.close(),成一对，因为cnsumer是个死循环，所有不会有结束
#生成器第一次不会执行，必须初始化None才能执行到yield，或者使用next（c），yield必须前后都有变量，
#前面的变量用来取调用者发送来的信息，后面的对象是生成器给调用者的信息，有来有回

# 生成器的生成值是直接放在生成器中的，而不是通过yield返回给调用者的
