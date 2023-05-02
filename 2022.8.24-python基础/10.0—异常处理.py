'''
异常处理部分

    try:
    
    except :
    
'''
import math
# for i in range(10):
#     input_number=input('请输入：')
#     if input_number=='q':
#         break
#     result=math.log(float(input_number))
#     print(result)


# for i in range(10):
#     try:
#         input_number=input('请输入：')
#         if input_number=='q':
#             break
#         result=math.log(float(input_number))
#         print(result)
#     except ValueError:
#         print('输入有误')

#
# for i in range(10):
#     try:
#         input_number=input('请输入：')
#         if input_number=='q':
#             break
#         result=1/math.log(float(input_number))
#         print(result)
#     except ValueError:
#         print('输入有误')
#     except ZeroDivisionError:
#         print('0不能做分母')
#     except Exception:#不能确定所有的错误类型的时候，先将你知道的几种类型写出来，之后用Exception总写
#         print('异常了啦')


'''
自己定义一个异常，利用继承
'''
# class TangError(ValueError):
#     pass
# cur=['1',5,89,656,46,3]
# while True:
#     cur_test=input('输入：')#这里有一个搞不懂的点，为什么用int类型的数据去匹配就不行，用字符串类型的去匹配就不报错
#     #cur_test = int(input('输入：'))  #明白了，这里的input默认为字符串类型，需要转换一下，才能按照整数类去识别
#     if cur_test not in cur:
#         raise TangError('Invalid input:%s'%cur_test)#raise抛出一个异常（为保证程序执行的安全性，需要将异常抛出来）；try except相当于捕捉异常


'''
finally关键字
'''

try:
    1/0
except:
    print('0000')
finally:
    print('不论这个报错是否执行，我都能保证finally里面的语句执行')

