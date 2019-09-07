try:
    num = eval(input("请输入一个数："))
    print(num ** 2)
except:
    print("输入不是数")

'''
除了try except
还可以有 else 和 finally
else 对应的语句块在不发生异常时执行
finally对应的语句块一定执行
也就是说如果try对应的语句块1不发生异常，
那么就可以“奖励”他去执行else对应的语句块
但是finally对应的语句块不管发不发生异常都会执行
'''
