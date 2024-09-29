#!/usr/bin/env python
# -*- coding: utf-8 -*-

def opFactory(oper, num):
    def operation(value):
        if oper == "**":
            return value ** num
        elif oper == "*":
            return value * num
        elif oper == "/":
            return value / num
        else:
            return "Not supported operation!"
    return operation

test = opFactory("**", 2)
print(test(5))
test = opFactory("*", 2)
print(test(5))
test = opFactory("$", 2)
print(test(5))