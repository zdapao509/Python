'''
操作文件
'''


'''
读取文件：从open到close
'''
txt=open('test11')#注意：找文件的时候，一定要将文件名字用‘’括起来
print(txt)#<_io.TextIOWrapper name='test11' mode='r' encoding='cp936'>



#txt=open('./test11')#./表示当前文件夹下         打印出现乱码的问题：澶╂皵鐪熷ソ

txt=open('./test11',encoding='utf-8')#解决乱码问题，解码的方式定为utf-8就好了

#txt=open('./data/test11')#./data/表示当前文件夹中的data文件夹下



# txt_read=txt.read()
# print(txt_read)


lines=txt.readlines()#这里注意：read和Readlines两个函数是冲突的，read读完了之后，Readlines的指针直接对应到了文件的最后，也就是说，读不出数据，因此在读这一句的时候，要将前面的read函数注释掉
print(type(lines))#<class 'list'>
print(lines)#['hello\n', '天气真好\n', '天气真好']

for i in lines:#读取每一行
    print('当前行：',i)
    pass

txt.close()#关闭当前的文件，完成一次读取任务


'''
创建文件
'''
txt=open('test11.1','w')#w代表写入，w模式下会将原来的文件覆盖
txt.write('123')
txt.write('\n-*-*')
txt.write('456')
txt.close()

txt=open('test11.1','a')#a代表append，a模式下不会将原来的文件覆盖
txt.write('\n123')
txt.write('\n-*-*')
txt.write('456')
txt.close()

# txt=open('test11.1','w')
# for i in range(10):
#     txt.write(str(i)+'\n')
# txt.close()#如果没有将文件关闭，下面的读取就不能进行，虽然已经写入了，但是无法读取
# txt2=open('test11.1',encoding='utf-8')
# print(txt2.read())



'''
写文件最好按照以下的历程：避免出现错误
        try:
        except Exception:
        finally:
'''
txt=open('test11.1','w')
try:
    for i in range(100):
        10/(i-5)
        txt.write(str(i)+'\n')
except Exception:
    print('error:',i)
finally:
    txt.close()



'''
写文件的简便方法：with方法
    自动带了关闭文件
'''

with open('test11.1','w') as f:
    f.write('jin tian tian  qi xia yu ')