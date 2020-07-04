import numpy as np
import matplotlib.pyplot as plt

# F_p 上の y^2=x^3+ax+b での p, a, b
p, a, b = 23, 1, 1
G=(0,1)
def inv(n, p):
    return pow(n, p-2, p)

def ec_double(A):
    l = (((3 * A[0] **2) + a) * inv(2*A[1], p)) % p
    x = (l ** 2 - A[0] - A[0]) % p
    y = (l * (A[0] - x) - A[1]) % p
    return x, y

G2=ec_double(G)
print(G2) # (6, 19)

def ec_add(A, B):
    l = ((B[1] - A[1]) * inv(B[0] - A[0], p)) % p
    x = (l ** 2 - B[0] - A[0]) % p
    y = (l * (A[0] - x) - A[1]) % p
    return x, y
G3 = ec_add(G2, G)
print(G3) # (3, 13)

from ecdsa.ellipticcurve import CurveFp, Point

# F_p 上の y^2=x^3+ax+b の意味での p, a, b
p, a, b = 23, 1, 1
c = CurveFp(p,a,b)
# G を c 上の点(0,1)とする
G = Point(c, 0, 1)
current = G
for i in range(1,28):
    print("{}G:¥t{}".format(i,current))
    current = current + G

# F_p 上の y^2=x^3+ax+b の意味での p, a, b
p, a, b = 31, 2, 17
c = CurveFp(p,a,b)
# G を c 上の点(10,13)とする
G = Point(c, 10, 13)
current = G
for i in range(1,91):
    print("{}G:¥t{}".format(i,current))
    current = current + G
