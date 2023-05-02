'''
赋值机制：

'''

tang=1000
yudi=tang
print(id(tang))#1842098213232
print(id(yudi))#1842098213232

print(yudi is tang)#True

tang=1000000000
yudi=1000000000
print(id(tang))#2472866161008
print(id(yudi))#2472866161008——为了节省内存空间，对于两个不一样的变量的值相同时，内存地址将指向同一地址