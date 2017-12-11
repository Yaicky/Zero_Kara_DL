# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import numpy as np


def softmax(x):

    # if x.ndim == 2:
    #     x = x.T
    #     x = x - np.max(x, axis=0)
    #     y = np.exp(x) / np.sum(np.exp(x), axis=0)
    #     return y.T

    x = x - np.max(x, axis=1)
    return np.exp(x) / np.sum(np.exp(x))


x = np.array([[2, 3, 4, 5], [1, 2, 3, 4], [1, 4, 5, 6]])
t = np.array([1, 2])
y = x.T

print(x.ndim)
x1, x2 = x, x.T
print(x1, x2)
x1, x2 = x1 - np.max(x1), x2 - np.max(x2, axis=0)
# rlt1 = x - np.max(x)
# rlt2 =
print(x1)
print(x2)
# [[ 0.0320586   0.08714432  0.23688282  0.64391426]]
# [[ 0.0320586   0.08714432  0.23688282  0.64391426]]
# print(x.shape)
# print(x.ndim)
# print(x.size)
# print(y.shape)
# print(y.ndim)
# print(y.size)
# print(t.shape[0], t.ndim)
# print(x[np.arange(t.shape[0]), t])

