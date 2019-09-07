'''
初始化给定的随机数种子，默认为当前系统时间
random.seed(10) *产生种子10对应的序列

生成一个【0.0,1.0）之间的随机小数
random.random()

拓展随机数函数

randint()
生成一个[a,b]之间的整数

randrange(m,n[,k])
生成一个[m,n)之间以k为步长的随机整数

getrandbits(k)
生成一个k比特长的随机整数

uniform(a,b)
生成一个[a,b]之间的随机小数(精度小数点后16位)

choice(seq)
从序列seq中随机选择一个元素

shuffle(seq)
将序列seq中元素随机排列，返回打乱后的序列
