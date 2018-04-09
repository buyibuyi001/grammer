class ClassA(object):

    def __init__(self, classname):
        self.classname = classname

    def __getattr__(self, attr):
        return('invoke __getattr__', attr)

insA = ClassA('ClassA')
print(insA.__dict__) # 实例insA已经有classname属性了
