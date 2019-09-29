A = {"p", "y", 123}
B = set("pypy123")
print(A - B)
print(A & B)
print(A | B)
print(A ^ B)
A.add("x")  # 如果x不在集合S中，将x增加到S
A.discard("x")  # 移除S中元素x，如果x不在集合S中,不报错
# A.remove("x")     #移除S中元素x,如果x不在集合S中，产生KeyError异常
# A.clear() 移除S中所有元素
# A.pop()   随机返回S的一个元素，更新S，若S为空产生KeyError异常
# A.copy()  返回集合S的元素个数
# len(A)    返回集合S的元素个数
# sign = "x" in A   判断S中元素x，x在集合S中，返回True，否则返回False
# sign = "x" not in A   判断S中元素x，x不在集合S中，返回True，否则返回False
# set("x")将其他类型变量x转变为集合类型

