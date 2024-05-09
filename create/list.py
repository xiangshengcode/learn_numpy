import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([1,2,3])
print(x1)
##一维数组

x2 = np.array([[1,2.,3],[4,5,6]])
print(x2)
##二维数组,多维类似

x3 = np.array([1,2,3],dtype=np.float16)
print(x3)
##指定数据类型

x4 = np.array((1,2))
print(x4)
##元组转换

##一般使用list转换

x5 = np.asarray((1,2,3))
##转换而不是创建

## 即便你全是 True 它也不行
arr = np.array([1, 2, 3])
cond2 = arr > 0
cond2
cond2.any()
cond2.all()
##只要有一个True就返回True，全是True才返回True