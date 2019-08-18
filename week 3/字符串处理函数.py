'''for i in range(125):
    print("{:s}".format(chr(i)))'''
print("{:s}".format(chr(9801)))
print("{:s}".format(chr(10004)))
for i in range(12):
    '''print("{:s}".format(chr(9800+i)))'''
    print(chr(9800+i),end="")

''' 
len(x) 返回字符串x的长度
str(x) 任意类型x所对应的字符串形式 与eval(x)是一对
hex(x) 或oct(x)整数x的十六进制或八进制小写形式字符串
chr(u) u为Unicode编码，返回其对应的字符
ord(x) x为字符，返回其对应的Unicode编码
 

