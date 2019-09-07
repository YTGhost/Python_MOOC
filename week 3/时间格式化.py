import time

''' strftime(tpl,ts)
tpl格式化的格式
ts输入的计算机时间格式的时间'''
t = time.gmtime()
print("{}".format(time.strftime("%Y-%m-%d %H:%M:%S", t)))
'''
%Y 年份 0000~9999
%m 月份 01~12
%B 月份名称 January~December
%b 月份名称简写 Jan~Dec
%d 日期 01~31
%A 星期名称 Monday~Sunday
%a 星期名称简写 Mon~Sun
%H 小时(24h制) 00~23
%I 小时(12h制) 01~12
%p 上午/下午 AM,PM
%M 分钟 00~59
%S 秒 00~59'''
timeStr = '2018-01-26 12:55:20'
print("{}".format(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S")))
'''
time.strftime 与 time.strptime 是一对
前者将计算机的时间格式转换成我们所想要的格式
后者将用户输入进来的一串关于时间的字符串转换为计算机能读懂时间类型
