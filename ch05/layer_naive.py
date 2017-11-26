# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y

        return self.x * self.y

    def backward(self, dout):
        dx = self.y * dout
        dy = self.x * dout

        return dx, dy

class AddLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y

        return self.x + self.y

    def backward(self, dout):
        dx = dout * 1
        dy = dout * 1

        return dx, dy