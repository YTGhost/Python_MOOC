f = open("f.txt", "r", encoding='utf8')
s = f.read(6)  # 没有参数或参数为-1时读入全部内容，如果给出参数，则读入前size长度。
t = f.readline()  # 读入一行内容，如果给出参数，读入该行前size长度
y = f.readlines()  # 读入文件所有行，以每行为元素形成列表，如果给出参数，读入前参数行
print(s)
print(t)
###################
# 遍历全文本：方法一
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
txt = fo.read()
# 对全文txt进行处理
fo.close()
# 遍历全文本：方法二
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
txt = fo.read(2)
while txt != "":
    # 对txt进行处理
    txt = fo.read(2)
fo.close()

# 逐行遍历文件：方法一：一次读入，分行处理
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
for line in fo.readlines():
    print(line)
fo.close()
# 逐行遍历文件：方法二：分行读入，逐行处理
fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
for line in fo:
    print(line)
fo.close()




