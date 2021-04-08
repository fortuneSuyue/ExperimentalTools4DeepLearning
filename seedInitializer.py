import torch
import numpy as np


# https://zhuanlan.zhihu.com/p/104019160
def randomSeedInitial(seed=256, cudnnDeterministic=True, cudnnBenchmark=False):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    # 为了保证可复现性, defaul True False; False True 可能可以提升gpu运行效率
    torch.backends.cudnn.deterministic = cudnnDeterministic
    torch.backends.cudnn.benchmark = cudnnBenchmark
