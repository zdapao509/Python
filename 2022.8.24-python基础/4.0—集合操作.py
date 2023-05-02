'''
集合操作：集合会保留唯一的元素，也就是将重复的元素去除掉
    tang=set()
集合常用与将list中的重复的数清除掉，保留干净的list值
'''

tang=[123,123,456,798,798]
tang=set(tang)
print(tang)#{456, 123, 798}
tang=list(tang)
print(tang)#[456, 123, 798]——将重复的数据清除掉之后，任然恢复为list数据类型

tang=set()
print(type(tang))#<class 'set'>

tang=set([1,1,1,2,2,2,3,3,3])
print(tang)#{1, 2, 3}

tang={1,2,2,3,3,3,3,74,5,6}
print(tang)#{1, 2, 3, 5, 6, 74}

'''
集合的操作
'''
a={1,2,3,4}
b={2,3,4,5}
print(a.union(b))#{1, 2, 3, 4, 5}——求并集
print(a|b)#{1, 2, 3, 4, 5}——求并集

print(a.intersection(b))#{2, 3, 4}——求交集
print(a&b)#{2, 3, 4}

print(a.difference(b))#{1}——a与b的不同之处
print(b.difference(a))#{5}
print(a-b)#{1}

a={1,2,3,4,5}
b={2,3,4}
print(b.issubset(a))#True——判断b是a的子集
print(b<=a)#True
print(a<=a)#True——自己是自己的子集

c={78,98}
a.update(c)
print(a)#{1, 2, 3, 4, 5, 98, 78}

a.remove(1)
print(a)#{2, 3, 4, 5, 98, 78}

a.pop()
print(a)#{3, 4, 5, 98, 78}——这里的弹出就没有索引来指定了。因为集合里面的数据是没有顺序的，所以只能是从第一个数往出弹