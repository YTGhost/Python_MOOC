import time

'''
perf_counter()
返回一个CPU级别的精确时间计数值，单位为秒。
由于这个计数值的起点不确定，连续调用差值才有意义

sleep()
s为拟休眠的时间，单位是秒，也可以是浮点数
可以这样使用：
def wait():
    time.sleep(3.3)
这时调用wait()
程序将等待3.3秒后再退出
