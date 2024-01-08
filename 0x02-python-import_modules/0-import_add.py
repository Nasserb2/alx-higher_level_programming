#!/usr/bin/python3
a = 1
b = 2
add_0 = __import__("0-add").add
print("{:d} + {:d} = {:d}\n".format(a, b, add_0(a, b)))

