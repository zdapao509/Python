'''
时间的导入
'''

import time
print(time.time())#1661434267.9003227——从1970.1.1到现在一共经历了多久时间
print(time.localtime(time.time()))#time.struct_time(tm_year=2022, tm_mon=8, tm_mday=25, tm_hour=21, tm_min=31, tm_sec=7, tm_wday=3, tm_yday=237, tm_isdst=0)——当前时间
print(time.asctime(time.localtime(time.time())))#Thu Aug 25 21:33:40 2022

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))#2022-08-25 21:35:34

import calendar
print(calendar.month(2022,10))

print(help(calendar.month))