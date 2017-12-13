# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import numpy as np
from common.util import im2col
if __name__ == '__main__':
    # x = np.random.randn(2, 3, 4, 5)
    # print(x.shape)
    # print(x)
    # print(x[0, 0])
    x = np.random.rand(2, 2, 3, 3)
    w = np.random.rand(2, 2, 2, 2)
    col = im2col(x, 2, 2, 1, 0)
    col_w = w.reshape(2, -1).T
    print(w)
    print(col_w.shape)
    print(col_w)
    print(x)
    print(col.shape)
    print(col)

    out = np.random.rand(8, 2)
    print(out.shape)
    print(out)
    out = out.reshape(2, 2, 2, -1).transpose(0, 3, 1, 2)
    print(out.shape)
    print(out)