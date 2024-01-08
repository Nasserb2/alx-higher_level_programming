#!/usr/bin/python3
a = 1
b = 2
add_0 = __import__("add_0").add
print("{:d} + {:d} = {:d}\n".format(a, b, add(a, b)))

