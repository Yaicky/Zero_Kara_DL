# -*- coding: utf-8 -*-
__author__ = 'Yaicky'

from ch04.function_test import function_test
class Test():
    def function_test(self):
        print('class_function')
        s = function_test()
        return s


t = Test()
print(t.function_test())