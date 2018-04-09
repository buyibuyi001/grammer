def consumer():

    res = ''
    while True:
        n = yield res
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        res = '200 OK'

def produce(c):

    c.send(None)

    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        res = c.send(n)
        print('[PRODUCER] Consumer return: %s' % res)
    c.close()

c = consumer()
produce(c)

#先生产后消费所以先调用produce，且用None启动，这时候没有生产
#所以第一次consumer，也先初始化为0，
#在yield 等号前后切断，先返回yield右边的等式，然后左边变量接收另一个函数
#的发送值。
#f.send,f.close
def func():

    n=0
    while n<10:
        x=yield n
        n+=1

def funca():
    y=func()
    t= yield from func()

    print(t)
