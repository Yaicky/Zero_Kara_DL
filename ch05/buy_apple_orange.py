# -*- coding: utf-8 -*-
__author__ = 'Yaicky'
from ch05.layer_naive import *

apple = 100
apple_num = 2
orange = 150
orange_num = 3
tax = 0.1 + 1

#layer
mul_apple_layer, mul_orange_layer = MulLayer(), MulLayer()
add_apple_orange_layer = AddLayer()
mul_tax_layer = MulLayer()

#forward
apple_price = mul_apple_layer.forward(apple, apple_num)
orange_price = mul_orange_layer.forward(orange, orange_num)
add_apple_orange = add_apple_orange_layer.forward(apple_price, orange_price)
all_price = mul_tax_layer.forward(add_apple_orange, tax)

#backward
dprice = 1
dall_price, dtax = mul_tax_layer.backward(dprice)
dapple_price, dorange_price = add_apple_orange_layer.backward(dall_price)
dapple, dapple_num = mul_apple_layer.backward(dapple_price)
dorange, dorange_num = mul_orange_layer.backward(dorange_price)

print("price:", int(all_price))
print("dApple:", dapple)
print("dApple_num:", int(dapple_num))
print("dOrange:", dorange)
print("dOrange_num:", int(dorange_num))
print("dTax:", dtax)

'''
price: 715
dApple: 2.2
dApple_num: 110
dOrange: 3.3000000000000003
dOrange_num: 165
dTax: 650
'''