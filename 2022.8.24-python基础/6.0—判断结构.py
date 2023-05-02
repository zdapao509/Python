'''
 判断结构
'''
tang=100
if tang>200:
    print('ok')
elif tang<1000:
    print(123)
else:
    print(465)

tang=[1,2,3,465]
if 1 in tang:
    print('ok')
elif 2 in tang:#结果只输出了OK，说明只要判断的语句执行了，下面的语句就不再执行
    print('hhh')
