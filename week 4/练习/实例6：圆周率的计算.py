from random import *
N = eval(input())
seed(123)
hits = 0.0
for i in range(1,N+1) :
    x,y = random(),random()
    dist = pow((x**2+y**2),0.5)
    if dist <= 1 :
        hits += 1
pi = 4 * hits/N
print("{:.6f}".format(pi))
