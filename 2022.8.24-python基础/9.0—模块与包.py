'''
模块与包
'''
tang_v=10
def tang(list1):
    tang_sum=0
    for i in range(len(list1)):
        tang_sum+=list1[i]
    return tang_sum
list2=[1,2,3,4,5]
print(tang(list2))

import test09
print(test09)#<module 'test09' from 'G:\\python学习\\2022.8.24\\test09.py'>
print(test09.tang_v)

test09.tang_v =156
print(test09.tang_v)

ttt=[56,45,65]
print(test09.tang(ttt))


import test09 as t9
print(t9)#<module 'test09' from 'G:\\python学习\\2022.8.24\\test09.py'>
print(t9.tang_v)

from test09 import tang_v,tang#以这种方式导入的话，引用相应的参数以及函数时，不再需要以文件名.的方式来调用，直接用就行
print(tang_v)
li=[56,45,78,89]
print(tang(li))

from test09 import *        #直接将所有的属性和方法导入进来，不需要依次填写
print(tang_v)
li=[56,45,78,89]
print(tang(li))

import os   #os:操作系统
# os.remove('test.py')#删除包test.py

print(os.path.abspath('.'))#G:\python学习\2022.8.24————调用系统路径