# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.functions import softmax, cross_entropy_error
from common.gradient import numerical_gradient

class simpleNet:
    def __init__(self):
        # self.W = np.random.randn(2, 3)
        self.W = np.array([[ 1.16747888, -1.54896546,  0.02434254],
                [ 0.18342776, -1.95447207,  0.62683599]])

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])
net = simpleNet()

f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)

print(dW)

# net = simpleNet()
# x = np.array([0.6, 0.9])
# p = net.predict(x)
# print(p)
# print(np.argmax(p))
# t = np.array([0, 0, 1])
# print(net.loss(x, t))
