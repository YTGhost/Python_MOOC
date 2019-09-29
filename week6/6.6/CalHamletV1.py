# CalHamletV1.py
def getText():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getText()
words = hamletTxt.split()  # 以列表类型返回
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
# 这里先让列表类型的counts转换为dict_items型的键值
# 再通过list()转换成有元组构成的列表
items.sort(key=lambda x: x[1], reverse=True)
# key = lambda x: x[1]
# 在这里x表示一个元组,x[1]表示元组里的第二个元素，即指这里的value
# 所以这条命令的意思就是按照列表中每个元组的第二个元素来进行从小到大的排序
# 但因为后面有reverse=True，所以这里反过来变成了从大到小
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
# 左对齐并占十个位置  右对齐并占五个位置
