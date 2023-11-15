#该代码用作将某npy文件包装成npz文件，方便ASTGCN直接读取

import numpy as np
arr = np.load(r"D:\报告\model_refined\data\China\China.npy")
print(arr.shape)
arr = arr.transpose(1,0,2)
#arr: [N, T, F]
np.savez_compressed(r"D:\报告\model_refined\data\China\China",data=arr)