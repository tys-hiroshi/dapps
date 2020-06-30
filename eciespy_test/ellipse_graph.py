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
plt.show() 
