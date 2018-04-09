#  列表解析

from random import randint

data=[randint(-10,10) for i in range(10)]

print(filter(lambda x: x>0, data) )

# 字典解析
{ for k,v in d.iteritems if v>0}
# 集合解析
x= set(data)

{ i for i in x if x>0}

#  tuple 的存储空间比较小，
from collections import namedtuple

Student= namedtuple('student',['name','age','sex','email'])
s=Student('Jim,16,'male','sdf@qq.com')

