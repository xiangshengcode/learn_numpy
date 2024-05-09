import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(0,12,2).reshape(3,2)
print(x1)
##创建数组并reshape,arrange可以指定步长，并使用reshape改变形状，注意reshape时元素个数要一致

##使用linspace/logspace创建等差/等比数列 线性/对数
x2 = np.linspace(0,30,20).reshape(4,5)
print(x2)
##需要传递三个参数，起始，终止，个数
x3 = np.logspace(0,30,20,base=np.e).reshape(4,5)
print(x3)
##需要传递三个参数，起始，终止，个数，底数 默认10

N = 20
x = np.arange(N)
y1 = np.linspace(0, 10, N) * 100
y2 = np.logspace(0, 10, N, base=2)

plt.plot(x, y1, '*')
plt.plot(x, y2, 'o')

##不能使用if判断，因为if判断是逐个元素判断，而数组是整体判断

print(np.alltrue(2 ** np.linspace(0, 10, N)  == y2))