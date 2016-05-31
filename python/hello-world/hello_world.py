#
# Skeleton file for the Python "Hello World" exercise.
#
# -*- coding: utf-8 -*-
# Works with python3 but not with 2.7. Even after adding the utf 8 above


def hello(name=''):
    if name != '':
        out = "Hello, {}!".format(name)
    else:
        out = "Hello, World!"
    return out

print(hello(""))
