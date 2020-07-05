# -*- coding: utf-8 -*-

def gcd_ext(a, b):
    """
    # 拡張ユークリッドの互除法
    # a*x + b*y = gcd(a,b) となる (x,y) を求める.
    http://www.tbasic.org/reference/old/ExEuclid.html
    """
    x, y, lastx, lasty = 0, 1, 1, 0
    while b != 0:
        q = a // b
        a, b = b, a % b
        x, y, lastx, lasty = lastx - q * x, lasty - q * y, x, y
    return (lastx, lasty)

result = gcd_ext(111, 30)

print(result) #(3, -11)



