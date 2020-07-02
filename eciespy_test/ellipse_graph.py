import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 100, 101)
# y = np.random.randn(101)
# #Y^2 = X^3 + X + 1

# plt.plot(x, y, color=(0,0,1))

# plt.show()

# x = np.linspace(-10,10,100)
# y = x*x
# plt.plot(x,y) 
# plt.show()

a = 1
b = 1 

y, x = np.ogrid[-5:5:100j, -5:5:100j] 
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0]) 
plt.grid() 
#plt.show() 

# https://tex2e.github.io/blog/crypto/point-of-elliptic-curve-over-GF

# def quadratic_residue(a, p):
#     return pow(a, (p - 1) // 2, p) == 1

# def f(x, p):
#     return (x**3 + x + 6) % p

# def calc_y(z, p):
#     res = z**3 % p
#     return res % p, -res % p

# p = 11
# points = []
# for x in range(p):
#     z = f(x, p)
#     if quadratic_residue(z, p):
#         y1, y2 = calc_y(z, p)
#         print('x = %2d, z = %d, QR(%2d, 11)? = True, y = %d, %d' % (x, z, x, y1, y2))
#         points.append((x, y1))
#         points.append((x, y2))
#     else:
#         print('x = %2d, z = %d, QR(%2d, 11)? = False' % (x, z, x))

# print("points:")
# print(sorted(points))

# E(F_11)={(2,4),(2,7),(3,5),(3,6),(5,2),(5,9),(7,2),(7,9),(8,3),(8,8),(10,2),(10,9),∞}

def quadratic_residue(a, p):
    return pow(a, (p - 1) // 2, p) == 1

def f(x, p):
    return (x**3 + x + 1) % p

def calc_y(z, p):
    res = z**3 % p
    return res % p, -res % p

p = 5
points = []
for x in range(p):
    z = f(x, p)
    if quadratic_residue(z, p):
        y1, y2 = calc_y(z, p)
        print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = True, y = %d, %d' % (x, z, x, p, y1, y2))
        points.append((x, y1))
        points.append((x, y2))
    else:
        print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = False' % (x, z, x, p))

print("points:")
print(sorted(points))

# x =  0, z = 1, quadratic_residue( 0, 5)? = True, y = 1, 4
# x =  1, z = 3, quadratic_residue( 1, 5)? = False
# x =  2, z = 1, quadratic_residue( 2, 5)? = True, y = 1, 4
# x =  3, z = 1, quadratic_residue( 3, 5)? = True, y = 1, 4
# x =  4, z = 4, quadratic_residue( 4, 5)? = True, y = 4, 1

# E(F_5)={(0, 1), (0, 4), (2, 1), (2, 4), (3, 1), (3, 4), (4, 1), (4, 4),∞}