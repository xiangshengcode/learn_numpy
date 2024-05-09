##常用于随机生成训练或测试数据，神经网路初始化等。
##需要注意的是：这里我们统一推荐使用新的 API 方式创建
##即通过 np.random.default_rng() 先生成 Generator，然后再在此基础上生成各种分布的数据。

import numpy as np

np.random.rand(2,3)
##生成[0,1)之间的随机数，均匀分布

np.random.rand()
##生成一个随机数

np.random.randn(2,3)
##生成标准正态分布的随机数

np.random.uniform(0,100,(2,3))
##生成[0,100)之间的随机数，均匀分布,指定上下限

##创建一个Generator，然后再在此基础上生成各种分布的数据
rng = np.random.default_rng()
rng.random.randint(0,100,(2,3))
##生成[0,100)之间的随机整数，均匀分布,指定上下限
rng.integers(0,100,(2,3))
##生成[0,100)之间的随机整数，均匀分布,指定上下限
rng.standard_normal((2,3))
##生成标准正态分布的随机数
rng.normal(0,1,(2,3))
##生成正态分布的随机数，指定均值和标准差