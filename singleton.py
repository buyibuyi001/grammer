# module edition
class Mysingle0():
    def fo(self):pass

singleton=Mysingle0()


# __new__ edition
class Mysingleton1(object):

    def __new__(cls):
        if not hasattr(cls,'_instance'):
            cls._instance=super(Mysingleton1,cls).__new__(cls)
        return cls._instance

#对比ton1 和 ton2  ，  *args,**kwargs 可有可无，但必须对应，有因为传参要一致
class Mysingleton2():
	_instance =None
	def __new__(cls,*args,**kwargs):
	    if  not cls._instance:cls._instance =super(Mysingleton2,cls).__new__(cls,*args,**kwargs)
	    return cls._instance
#  decorator edition
from functools import wraps
def singleton3(cls):
    instances={}
    @wraps(cls)
    def getinstance(*args,**kwargs):
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls]
    return getinstance

@singleton3
class Myclass():pass

#  __metaclass__ edition
class Singleton4(type):
    def __init__(self,*args,**kwargs):
        self.__instance= None
        super(Singleton4,self).__init__(*args,**kwargs)
        print("init")

    def __call__(self,*args,**kwargs):
        if self.__instance is not None:
            self.__instance =super(Singleton4,self).__call__(*args,**kwargs)
            print("call")
        return self.__instance

#metaclass 在python3中写法如下，写的不对，不起作用。
#class Mysingleton5(metaclass=Singleton4): pass
#metaclass 似乎元类里没有new方法，然后从type继承，没有new方法，所以用metaclass格式来嗲用new方法


class Singleton6(type):
    __instance={}

    def __call__(cls,*args,**kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] =super(Singleton6,cls).__call__(*args,**kwargs)
            print("call")
        return cls.__instance[cls] 

class Mysingleton7(metaclass=Singleton6): pass


class Singleton8(type):
    __instance=None

    def __call__(cls,*args,**kwargs):
        if not cls.__instance:
            cls.__instance =super(Singleton8,cls).__call__(*args,**kwargs)
            print("call")
        return cls.__instance

class Mysingleton9(metaclass=Singleton8): pass






