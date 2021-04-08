from torch import nn


class EasyModel(nn.Sequential):
    def __init__(self):
        super(EasyModel, self).__init__()
        self.add_module('fc1', nn.Linear(1, 10))
        self.add_module('relu', nn.ReLU(inplace=False))
        self.add_module('fc2', nn.Linear(10, 1))

