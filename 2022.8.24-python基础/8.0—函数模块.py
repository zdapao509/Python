'''
函数
'''

a=10
b=30
def print_value():
    print('a=',a)

print_value()

def abb(a,b):
    print(a + b)
    return a+b
    #print(a+b)     #有了return之后，print语句就不再执行

abb(3,5)#8
print(abb(3,5))#8 8


def abbc(a=89,b=5):
    print(a + b)
    return a+b
abbc()
abbc(5)
abbc(5,56)

def number(a,*args):#当所需要的参数数量不确定的时候，可以先将用*args代替
    b=0
    for i in args:
        a+=i
        b+=a
    return a,b
(a,b)=number(1,5,5,5,6)
print(a,b)

def abcd(**kwargs):
    for arg,value in kwargs.items():
        print(arg,value)
abcd(x=2,y=6)#    x 2     y 6
