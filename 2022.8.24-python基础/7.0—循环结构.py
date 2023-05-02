'''
循环结构
continue
break
'''

tang=0
while tang<10:
    print(tang)
    tang+=1

tang=set([1,2,3])
while tang:
    tangs=tang.pop()
    print(tangs)#1  2   3——这里是将原来的集合里面的数都弹出来，直到原来的集合变成一个空集合，不再执行

tang=set(['tang','yu','di'])
for name in tang:
    print(name)

for i in range(10):
    print(i)

tang=[123,4,456,7898,5,412,3,45,61,310,354,5]
for i in range(len(tang)):
    print(tang[i])
'''
break 和 continue
'''
for k in tang:
    if k%2==0:
        print('这个数是：{}{}'.format(k,'偶数'))
    else:
        continue#本次循环不再执行，继续下一次的循环
    print('这个数是：%s,%d'%('偶数',k))

for k in tang:
    if k%3==0:
        print('这个数是：{},,,{}'.format(k,'3的倍数'))
    else:
        break#整体的循环过程停止，不再继续
    print('这个数是：%s,%d'%('3的倍数',k))

