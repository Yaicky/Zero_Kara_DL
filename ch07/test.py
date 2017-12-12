# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
import numpy as np

if __name__ == '__main__':
    x = np.random.randn(2, 3, 4, 5)
    print(x.shape)
    print(x)
    print(x[0, 0])