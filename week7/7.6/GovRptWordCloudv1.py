import jieba
import wordcloud
# from scipy.misc import imread     这个函数在scipy1.30版已经没有了
from matplotlib.pylab import imread

mask = imread("fivestar.jpg")
f = open("新时代中国特色社会主义.txt", "r", encoding="utf-8")
# f = open("关于实施乡村振兴战略的意见.txt", "r", encoding="utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
w = wordcloud.WordCloud(font_path="msyh.ttc", mask=mask,
                        width=1000, height=700, background_color="white",
                        max_words=15)
w.generate(txt)
w.to_file("WordCloud1.png")
# w.to_file("WordCloud2.png")
