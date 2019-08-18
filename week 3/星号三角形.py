N = eval(input(""))
i = 1
while i<=N:
    star = '*' * i
    print("{0:^{1}}".format(star,N))
    i +=2
'''
n = eval(input())
for i in range(1,n+1,2):
    print("{0:^{1}}".format('*'*i, n))
'''