from math import *

print("{0:>3} {1:>10} {2:>10} {3:>25}".format("x", "sin(x)", "cos(x)", "tan(x)"))
print("="*52)

for x in range(0, 91, 10) :
    s = sin(radians(x))
    c = cos(radians(x))
    t = tan(radians(x))
    print("{0:3d} {1:10.4f} {2:10.4f} {3:25.4f}".format(x, s, c, t))
