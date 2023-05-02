'''
list结构——列表结构

    tang=[]

    通过[]来创建一个list结构
    里面放任何类型的东西都可以，没有类型的限制，也没有长度的限制
    
    也可以通过：
        tang=list([1,2,3])——来创建一个list结构
        
'''
tang=[]
print(type(tang))

tang=[1,2,3,4]
print(tang)

tang=['1','2',3,4]
print(tang)

tang=list([1,2,3])
print(tang)#结果：[1, 2, 3]
print(len(tang))#——计算list中的数据数

a=[123,456]
b=['nihao','hahah']
print(a+b)#结果：[123, 456, 'nihao', 'hahah']
print(a*3)#[123, 456, 123, 456, 123, 456]
print(a[0])#123
print(a[1])#456
print(a[-1])#456
print(b[-1])#hahah
print(a[0:])#[123, 456]——从第一个数一直到最后的所有值
print(a[1:])#[456]——从第二个数一直到最后的所有值
a[0]=789
print(a)#[789, 456]
a[:]=['tang','zhang','123']
print(a)#['tang', 'zhang', '123']

a=[1,2,3,4,5,6,7]
print(a[4:7])#[5, 6, 7]——这个索引是左闭右开，第七位不算

del a[0]
print(a)#[2, 3, 4, 5, 6, 7]

del a[0]
print(a)#[3, 4, 5, 6, 7]

del a[3:]
print(a)#[3, 4, 5]——从第四个数开始全部删除

print(4 in a)#True——判断4是否在a这个列表里面
print(6 in a)#False
print(6 not in a)#True

tang='tang yu di'
print('tang' in tang)#True

a=[1,2,[3,4,2]]
print(a[2])#[3, 4]
print(a[2][1])#4——结构比较复杂的时候，先找第一层，再找第二层
print(a.count(2))#1——计数操作：统计列表里面的2的数量

a=['af','fa','qpp']
print(a.index('af'))#0——找索引
#print(a.index('afdf'))#ValueError: 'afdf' is not in list——没有就找不到索引

b=[]
b.append(123)
#b.append(123,456)#TypeError: append() takes exactly one argument (2 given)——每次只能添加一个值
print(b)

b.append('tang ')
print(b)#[123, 'tang ']

b.append([1,2,3])
print(b)#[123, 'tang ', [1, 2, 3]]

b.insert(2,'python')
print(b)#在第3个位置插入字符python，原来的第三个值后移——[123, 'tang ', 'python', [1, 2, 3]]

b.remove([1,2,3])
print(b)#[123, 'tang ', 'python']——移除其中的[1,2,3]

c=[1,2,3,1,2,5]
c.remove(1)
print(c)#[2, 3, 1, 2, 5]——当里面有很多的1的时候，默认将第一个1删除

print(c.pop(2))#1——弹出位于第3个的值：1，并且将它返回出来，原来的列表里面就没有了
print(c)##[2, 3, 2, 5]

c.sort()
print(c)#[2, 2, 3, 5]——排序之后，原始的数据改变

d=[5,4,123,8,54,85]
e=sorted(d)
print(d)#[5, 4, 123, 8, 54, 85]——排序之后，原始的数据没有变化
print(e)#[4, 5, 8, 54, 85, 123]——排序数据

e.reverse()
print(e)#[123, 85, 54, 8, 5, 4]——将原始数据直接倒过来排序

