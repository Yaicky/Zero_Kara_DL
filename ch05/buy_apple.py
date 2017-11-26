# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
from ch05.layer_naive import *

apple = 100
apple_num = 2
tax = 0.1

#layer
mul_apply_layer = MulLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apply_layer.forward(apple, apple_num)
all_price = mul_tax_layer.forward(apple_price, tax+1)
print(all_price)

#backward
dprice = 1
dapple_price, dtax = mul_tax_layer.backward(dprice)
dapple, dapple_num = mul_apply_layer.backward(dapple_price)
print(dapple_price, dapple, dapple_num, dtax)

'''
220.00000000000003
1.1 2.2 110.00000000000001 200
'''