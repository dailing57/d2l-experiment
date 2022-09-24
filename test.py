import torch

a = torch.tensor(range(16), dtype = torch.float16).reshape((2, 2, 2, 2))
print(a.mean((0,2,3), keepdim=True))