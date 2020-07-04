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

# a = 1
# b = 1 

# y, x = np.ogrid[-5:5:100j, -5:5:100j] 
# plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x - b, [0]) 
# plt.grid() 
# plt.show() 

import sympy as sym
sym.init_printing()
Pi = sym.S.Pi # 円周率
E = sym.S.Exp1 # 自然対数の底

# 使用する変数の定義(小文字1文字は全てシンボルとする)
(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')

def generator_p(start): # 引数が指定されればその色をそうでないときは順番に色を生成するためのジェネレーター
    prime = 37 # リストの数 (素数なのでprimitiveに何を指定しても必ず最大周期になる)
    primitive = 8 # 生成元 (1ステップ当たり色相がprimitive * 37/360度進む)
    g0 = start # 開始元 (実際に返されるのは g0 * primitive)
    while True:
        val = yield g0
        if val: # ジェネレーターに引数が渡されるとそれを開始元としてリセットする
            g0 = val
        g0 += primitive
        if g0 >= prime: # 剰余を取る
            g0 -= prime
gen_hexnum = generator_p(0) # 引数に初期色を入れる
gen_hexnum.__next__() # ジェネレーターの初期化

def hexNum(num, type): # 色のリスト
    # 基本色(白背景で汎用的に使える落ち着いた色)
    color_basic = ['#9c1954', '#9e1a46', '#9d1e38', '#9a252a', '#962d1c', '#8f350d', '#873c00',
                   '#7d4300', '#734900', '#674f00', '#5b5300', '#4d5700', '#3e5b00', '#2b5d00',
                   '#0f6009', '#00611c', '#00632b', '#00643a', '#006449', '#006558', '#006567',
                   '#006575', '#006482', '#00648e', '#006298', '#0060a0', '#005ea6', '#005baa',
                   '#0056aa', '#0051a9', '#2f4ca4', '#50459d', '#673d94', '#78358a', '#862d7d', '#902470', '#981e62']
    # 彩度の高い色(目立つが多用はしないほうがよい。)
    color_vivid = ['#ffadc7', '#ffadbc', '#ffaeb2', '#ffb0a8', '#ffb29e', '#ffb596', '#f9b88f',
                   '#f1bc8a', '#e9bf86', '#dfc385', '#d5c685', '#caca87', '#becd8b', '#b2cf90',
                   '#a6d298', '#99d4a0', '#8dd5aa', '#80d7b4', '#74d7bf', '#6ad8ca', '#61d8d5',
                   '#5bd7e0', '#59d6e9', '#5dd5f2', '#65d3f9', '#71d1ff', '#7fceff', '#8ecbff',
                   '#9ec8ff', '#afc4ff', '#bec1ff', '#cdbdfd', '#dab9f7', '#e6b6ef', '#f0b3e6', '#f9b0dc', '#ffaed2']
    # 薄い色(白背景では使わない。黒背景で使うことを想定。)
    color_thin = ['#ffc3d5', '#ffc3cd', '#ffc3c5', '#ffc4be', '#ffc6b7', '#ffc8b1', '#fbcaac',
                  '#f5cca9', '#efcfa6', '#e8d2a5', '#e0d4a5', '#d8d7a6', '#cfd9a9', '#c6dbad',
                  '#bdddb3', '#b5deb9', '#ace0c0', '#a5e0c7', '#9ee1cf', '#98e1d7', '#94e1df',
                  '#92e1e6', '#92e0ed', '#94dff4', '#99def9', '#9fdcfd', '#a7daff', '#b1d8ff',
                  '#bbd5ff', '#c5d3ff', '#cfd0ff', '#dacdfc', '#e3cbf7', '#ecc8f2', '#f3c6eb', '#f9c5e4', '#fec4dc']

    if (type == 'thin'):
        hex_list = color_thin
    elif (type == 'vivid'):
        hex_list = color_vivid
    else:
        hex_list = color_basic
    if num is not None:
        gen_hexnum.send(num)
    return hex_list[gen_hexnum.__next__()]

F = y**2 - x**3 - x -1
sym.plot_implicit(F, (x, -2, 2), (y, -2, 2), line_color=hexNum(2, 'thin'))
