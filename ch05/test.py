# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import numpy as np

x = np.array([[1.0, -0.5], [-2.0, 3.0]])
print(x)
mask = (x <= 0)
print(mask)
out = x.copy()
out[mask] = 0
print(out)

y = np.array([1.0, 20.01])
print(y.shape)