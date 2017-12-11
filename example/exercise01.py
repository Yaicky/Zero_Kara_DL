# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import numpy as np

x = np.array([[2, 3, 4, 5], [2, 3, 4, 5]])
t = np.array([1, 2])
y = x.T
#
# print(x.shape)
# print(x.ndim)
# print(x.size)
# print(y.shape)
# print(y.ndim)
# print(y.size)
print(t.shape[0])
print(x[np.arange(t.shape[0]), t])