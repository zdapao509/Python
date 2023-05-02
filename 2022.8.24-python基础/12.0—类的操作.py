'''
类的操作
类：面向对象

'''

class people:
    ' 帮助信息：  ****'
    #实例属性，所有的实例都会共享
    number=100
    #构造方法：实例化的时候，先调用它
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print('number=',people.number)
    def display_name(self):
        print(self.name)

print(people.__doc__)# 帮助信息：  ****

p1=people('zhangwieming ',23)
print(p1.number,p1.name,p1.age)
#p1.display()#NameError: name 'number' is not defined
p1.display()

p1.name='zhang'
print(p1.name)

# del p1.name
# print(p1.name)#AttributeError: 'people' object has no attribute 'name'

print(hasattr(p1,'name'))#True——hasattr判断p1是否有这个属性
print(hasattr(p1,'sex'))#False

print(getattr(p1,'name'))#zhang

setattr(p1,'name','yuditang')#修改属性

print(getattr(p1,'name'))#yuditang

# delattr(p1,'name')#删除属性
# getattr(p1,'name')#AttributeError: 'people' object has no attribute 'name'

'''
相关的内置属性
'''
print(people.__doc__)# 帮助信息：  ****
print(people.__name__)# people——类名
print(people.__module__)# __main__——类所在的模块的定义
print(people.__bases__)# (<class 'object'>,)——类的父类的构成元素
print(people.__dict__)# {'__module__': '__main__', '__doc__': ' 帮助信息：  ****', 'number': 100, '__init__': <function people.__init__ at 0x000001C7DFC8BD90>, 'display': <function people.display at 0x000001C7DFC8BE18>, 'display_name': <function people.display_name at 0x000001C7DFC8BEA0>, '__dict__': <attribute '__dict__' of 'people' objects>, '__weakref__': <attribute '__weakref__' of 'people' objects>}


class Parent:
    number=100
    def __init__(self):
        print('调用父类构造方法')
    def parentM(self):
        print('调用父类的方法')
    def setAttr(self,A):
        Parent.parentattr=A
    def getAttr(self):
        print('父类属性：',Parent.parentattr)
    def newM(self):
        print('父类的定义了')

class child(Parent):
    def __init__(self):
        print('调用子类的构造函数')
    def childM(self):
        print('调用子类的方法')
    def newM(self):
        print('子类改掉了')

c=child()
c.childM()
c.parentM()
c.setAttr(100)
c.getAttr()
c.newM()



