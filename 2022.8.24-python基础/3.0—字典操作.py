'''
字典操作：
    tang={}——创建字典
    tang=dict()——创建字典
    
字典的结构操作：
    key-value

结论：字典里面的值是通过对应的键来调的，不需要索引号，也就是不需要索引值，顺序不重要
'''
tang={}
print(type(tang))

tang1=dict()
print(type(tang1))

print(tang)#{}

tang['first']=123
print(tang)#{'first': 123}

tang['second']=456
print(tang)#{'first': 123, 'second': 456}

tang[123]=789
print(tang)#{'first': 123, 'second': 456, 123: 789}

print(tang['second'])#456——通过键来找到值

tang[123]=963
print(tang)#{'first': 123, 'second': 456, 123: 963}

a={'c':456,'b':898,'a':963}
print(a)#{'c': 456, 'b': 898, 'a': 963}

a={}
a[123]=456
a['qiu']=[1,2,23]
print(a)#{123: 456, 'qiu': [1, 2, 23]}——也就是说，字典里面的值也是任何类型都可以的

tang={}
tang1={1:456,2:789}
tang2={'1':456,'3':963}
tang['456']=tang1
tang['789']=tang2
print(tang)#{'456': {1: 456, 2: 789}, '789': {'1': 456, '3': 963}}——字典里面嵌套字典

tang=dict([('tang',1),('yu',2)])#——通过这种形式来创建一个字典
print(tang)#{'tang': 1, 'yu': 2}

tang['tang']+=1
print(tang)#{'tang': 2, 'yu': 2}

print(tang.get('tang'))#2——拿出tang这个键对应的值
print(tang['tang'])#2——拿出tang这个键对应的值

print(tang.get('tang3','meiyou'))#meiyou——对于原来的字典中没有的数，可以自己定义再访问，虽然觉得没什么卵用
print(tang)#{'tang': 2, 'yu': 2}——原名的字典并没有改变

print(tang.pop('tang'))#2--弹出tang对应的值，并且返回这个弹出的值
print(tang)#{'yu': 2}——弹出后，原来的值被删除掉了

del tang['yu']
print(tang)#--直删除


'''复杂的操作：字典的更新：'''

tang={'tang':123,'yu':456}
tang2={'tang':45888,'di':963}
tang.update(tang2)
print(tang)#{'tang': 45888, 'yu': 456, 'di': 963}——将原来的tang对应的值修改，并且将不存在的di键值加入进来

print('tang' in tang)#True——对应的值是否在字典里面

print(tang.keys())#dict_keys(['tang', 'yu', 'di'])——打印所有的键值
print(tang.values())#dict_values([45888, 456, 963])
print(tang.items())#dict_items([('tang', 45888), ('yu', 456), ('di', 963)])





