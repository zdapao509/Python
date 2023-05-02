"""
简单运算符号：
    %——取余
    **——次方
    abs——绝对值
    round——取整：round（15.3）
    max——最大值：max（1,2,5,6）
    min——最小值
    1.3e-5——科学记数法
    
类型查看：（python中给变量赋值不需要先定义数值的数据类型；比如：a=3即可将数字3赋值给变量a）
    type(变量)——查看变量的类型
    
字符串操作：
    字符串的拼接：
        tang='hello'+'python'
        print(tang)
        
        tang6=tang
        print(tang6)
        
        print(len(tang6))#计算字符串中的字符个数
        
    字符串的切分：见下面62-116
        
    
"""
tang=1.5
print(type(tang))

tang2=int(tang)
print(type(tang2))
print(tang2)

tang3=float(tang2)
print(tang3)

tang_str='123'
print(type(tang_str))

tang4=int(tang_str)
print(tang4)

tang_str1='桂英'
print(type(tang_str1))

#tang5=int(tang_str1)——报错：ValueError: invalid literal for int() with base 10: '桂英'
#print(tang5)

print(3>54)#输出bool类型的结果

#字符串拼接方法：
tang='hello'+'python'
print(tang)

tang6=tang*3
print(tang6)

print(len(tang6))#计算字符串中的字符个数


#字符串的切分：
tang='1 2 3 4 5'
print(tang.split())


tang='1,2,3,4,5'
tang7=tang.split(',')
print(tang.split(','))#用逗号切分

#字符串的合并：
tang8=''
tang8.join(tang7)
print(tang8.join(tang7))

#字符串的替换：
tang="hello"+'world'
tang2=tang.replace('world','python')
print(tang2)

#字符串转换为大写：
print(tang2.upper())

#字符串转换为小写：
print(tang2.lower())

#字符串去除空格：
tang2='          nihso     '
print(tang2.strip())

#字符串去除左边空格：
tang2='          nihso   123       '
print(tang2.lstrip())

#字符串去除右边空格：
tang2='          nihso   123       '
print(tang2.rstrip())


#字符串值的传递：
tang2='nihso   123     {} {} {}  '.format('tang','yu','di')
print(tang2)

#字符串值的传递：
tang2='nihso   123     {2} {1} {0}  '.format('tang','yu','di')
print(tang2)

#字符串值的传递—按照参数传递：
tang2='nihso   123     {tang} {yu} {di}  '.format(tang=1,yu=2,di=3)
print(tang2)

#字符串值的传递—以%形式：
tang2='nihso：'
a=45
b=4.5
print('%s %f %d'%(tang2,b,a))