##主要用于加载实现存储好的权重参数或预处理好的数据集，有时候会比较方便
##比如训练好的模型参数加载到内存里用来提供推理服务，或者耗时很久的预处理数据直接存起来，多次实验时不需要重新处理。
##需要注意的是：存储时不需要写文件名后缀，会自动添加。

import numpy as np 

np.save('./data/a', np.array([[1, 2, 3], [4, 5, 6]]))
##保存为.npy文件

np.savez("./data/b", a=np.arange(12).reshape(3, 4), b=np.arange(12.).reshape(4, 3))
##多个矩阵保存

np.savez_compressed("./data/c", a=np.arange(12).reshape(3, 4), b=np.arange(12.).reshape(4, 3))
##压缩保存

np.load('./data/a.npy')
                    