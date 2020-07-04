# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def plot_ec(a, b, p):
    xlist = []
    ylist = []
    for x in range(p):
        for y in range(p):
            if((x**3 + a * x + b - y**2) % p == 0):
                # 方程式を満たす x,y の組をリストに格納
                xlist.append(x)
                ylist.append(y)
                #以下は表示のため
                plt.figure(figsize=(10,10))
                plt.axis([0,p,0,p])
            if(p < 55):
                point_style = 'o'
                plt.grid(which='major',linestyle=':'
                , color="black")
                plt.yticks( [i for i in range(p)] )
                plt.xticks( [i for i in range(p)] )
        else:
            point_style = '.'
    plt.plot(xlist, ylist, point_style , color="black")
    plt.show()
#plot_ec(1, 1, 17)
plot_ec(2, 17, 31)