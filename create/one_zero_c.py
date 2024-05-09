##使用创建全 1/0 array 的快捷方式。
##需要注意的是 np.zeros_like 或 np.ones_like，二者可以快速生成给定 array 一样 shape 的 0 或 1 向量，这在需要 Mask 某些位置时可能会用到。
##需要注意的是：创建出来的 array 默认是 float 类型。
import numpy as np

x1 = np.zeros(5)
print(x1)

x2 = np.zeros((2,3))
print(x2)

x3 = np.ones((2,3,4))
print(x3)

x4 = np.zeros_like(x3)
print(x4)