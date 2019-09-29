ls = ["python", 123, ".io"]
lt = [789, 156]
print(ls[::-1])  # 列表取反
s = "python123.io"
print(s[::-1])  # 字符串取反
len(s)  # 返回序列s的长度
min(s)  # 返回序列s的最小元素，s中元素需要可比较
max(s)  # 返回序列s的最大元素，s中元素需要可比较
s.index("X")  # 返回序列s从i开始到j位置中第一次出现元素x的位置
s.index("x", 2, 3)
s.count("x")  # 返回序列s中出现x的总次数
# ls[i] = x     替换列表ls第i元素为x
# ls[i:j:k] = lt    用列表lt替换ls切片后所对应的元素字列表
# del ls[i]         删除列表ls中第i元素
# del ls[i:j:k]     删除列表ls中第i到第j以k为步长的元素
# ls += lt          更新列表ls，将列表lt元素增加到列表ls中
# ls.append(x)      在列表ls最后增加一个元素x
# ls.clear()        删除列表ls中所有元素
# ls.copy()         生成一个新列表i，赋值ls中所有元素
# ls.insert(i,x)    在列表ls的第i位置增加元素x
# ls.pop(i)         将列表ls中第i位置元素取出并删除该元素
# ls.remove(x)      将列表ls中出现的第一个元素x删除
# ls.reverse()      将列表ls中的元素反转
# x in ls           判断列表ls中是否包含x元素
# ls.index(x)       返回元素x所在列表ls中的索引
# len(ls)           ls的长度
# max(ls)           ls中最大元素
# tuple(ls)         将列表ls转换成元祖类型
