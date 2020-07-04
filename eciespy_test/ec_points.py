# -*- coding: utf-8 -*-

def quadratic_residue(a, p):
    return pow(a, (p - 1) // 2, p) == 1

def f(x, a, b, p):
    return (x**3 + a*x + b) % p

def calc_y(z, p):
    res = z**3 % p
    return res % p, -res % p

def disply_points(a, b, p):
    points = []
    for x in range(p):
        z = f(x, a, b, p)
        if quadratic_residue(z, p):
            y1, y2 = calc_y(z, p)
            print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = True, y = %d, %d' % (x, z, x, p, y1, y2))
            points.append((x, y1))
            points.append((x, y2))
        else:
            print('x = %2d, z = %d, quadratic_residue(%2d, %d)? = False' % (x, z, x, p))

    print("points:")
    print(sorted(points))
    print(len(points))

p = 31
disply_points(2, 17, p)

# x =  0, z = 17, quadratic_residue( 0, 31)? = False
# x =  1, z = 20, quadratic_residue( 1, 31)? = True, y = 2, 29
# x =  2, z = 29, quadratic_residue( 2, 31)? = False
# x =  3, z = 19, quadratic_residue( 3, 31)? = True, y = 8, 23
# x =  4, z = 27, quadratic_residue( 4, 31)? = False
# x =  5, z = 28, quadratic_residue( 5, 31)? = True, y = 4, 27
# x =  6, z = 28, quadratic_residue( 6, 31)? = True, y = 4, 27
# x =  7, z = 2, quadratic_residue( 7, 31)? = True, y = 8, 23
# x =  8, z = 18, quadratic_residue( 8, 31)? = True, y = 4, 27
# x =  9, z = 20, quadratic_residue( 9, 31)? = True, y = 2, 29
# x = 10, z = 14, quadratic_residue(10, 31)? = True, y = 16, 15
# x = 11, z = 6, quadratic_residue(11, 31)? = False
# x = 12, z = 2, quadratic_residue(12, 31)? = True, y = 8, 23
# x = 13, z = 8, quadratic_residue(13, 31)? = True, y = 16, 15
# x = 14, z = 30, quadratic_residue(14, 31)? = False
# x = 15, z = 12, quadratic_residue(15, 31)? = False
# x = 16, z = 22, quadratic_residue(16, 31)? = False
# x = 17, z = 4, quadratic_residue(17, 31)? = True, y = 2, 29
# x = 18, z = 26, quadratic_residue(18, 31)? = False
# x = 19, z = 1, quadratic_residue(19, 31)? = True, y = 1, 30
# x = 20, z = 28, quadratic_residue(20, 31)? = True, y = 4, 27
# x = 21, z = 20, quadratic_residue(21, 31)? = True, y = 2, 29
# x = 22, z = 14, quadratic_residue(22, 31)? = True, y = 16, 15
# x = 23, z = 16, quadratic_residue(23, 31)? = True, y = 4, 27
# x = 24, z = 1, quadratic_residue(24, 31)? = True, y = 1, 30
# x = 25, z = 6, quadratic_residue(25, 31)? = False
# x = 26, z = 6, quadratic_residue(26, 31)? = False
# x = 27, z = 7, quadratic_residue(27, 31)? = True, y = 2, 29
# x = 28, z = 15, quadratic_residue(28, 31)? = False
# x = 29, z = 5, quadratic_residue(29, 31)? = True, y = 1, 30
# x = 30, z = 14, quadratic_residue(30, 31)? = True, y = 16, 15
# points:
# [(1, 2), (1, 29), (3, 8), (3, 23), (5, 4), (5, 27), (6, 4), (6, 27), (7, 8), (7, 23), (8, 4), (8, 27), (9, 2), (9, 29), (10, 15), (10, 16), (12, 8), (12, 23), (13, 15), (13, 16), (17, 2), (17, 29), (19, 1), (19, 30), (20, 4), (20, 27), (21, 2), (21, 29), (22, 15), (22, 16), (23, 4), (23, 27), (24, 1), (24, 30), (27, 2), (27, 29), (29, 1), (29, 30), (30, 15), (30, 16)]
# 40