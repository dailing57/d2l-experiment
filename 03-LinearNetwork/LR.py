import random
import torch
def synthetic_data(w,b,num):
    X = torch.normal(0, 1, (num, len(w)))
    y:torch.Tensor = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))
true_w = torch.tensor([10, -10.])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)
def data_iter(batch_size, features, labels):
    num = len(features)
    indices = list(range(num))
    random.shuffle(indices)
    for i in range(0, num, batch_size):
        batch_indices = torch.tensor(indices[i : min(i + batch_size, num)])
        print(batch_indices)
        print(features[batch_indices])
        yield features[batch_indices], labels[batch_indices]
batch_size = 10
for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    break
