#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
    if name != '':
        out = "Hello, {}!".format(name)
    else:
        out = "Hello, World!"
    return out

print(hello(""))
