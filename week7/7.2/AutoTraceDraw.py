# AuroTraceDraw.py
import turtle as t

t.title('自动轨迹绘制')
t.setup(800, 600, 0, 0)
t.pencolor("red")
t.pensize(5)
# 数据处理
datals = []
f = open("data.txt", encoding='utf8')
for line in f:
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
    # 这里map函数的作用是将第一个参数的功能作用到第二参数中的每个元素上
    # 即就是对一个列表或者一个集合这样的组合数据类型的每一个元素都执行一次第一个参数所对应的函数
f.close()
# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])
