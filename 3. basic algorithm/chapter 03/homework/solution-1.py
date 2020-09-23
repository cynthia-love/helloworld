# -*- coding: utf-8 -*-
# Author: Cynthia

"""
    画出8n, 4n*log(n), 2*n^2, n^3, 2^n的图形

    先画常数刻度的, 再画对数刻度的

    所谓对数刻度, n -> f(n)变成log(n) -> log(f(n))
    (比如本来是2->4, 通过对数化, 缩放为: 1->2)

    关于对数刻度, x = log(n), 那么n = 2^x

    y = log(8n) = log(8*2^x) = x+3
    y = log(4n*log(n)) = log(4*2^x*x) = 2+x+log(x)
    y = log(2*2^x*x^x) = 2x+1
    y = log(2^3x) = 3x
    y = log(2^(2^x)) = 2^x
"""
import math
import matplotlib.pyplot as plt

x = [1.1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = [8*e for e in x]
y2 = [4*e*math.log(e, 2) for e in x]
y3 = [2*e**2 for e in x]
y4 = [e**3 for e in x]
y5 = [2**e for e in x]

plt.figure(1)
plt.plot(x, y1, label='8n')
plt.plot(x, y2, label='4n*log(n)')
plt.plot(x, y3, label='2*n^2')
plt.plot(x, y4, label='n^3')
plt.plot(x, y5, label='2^n')
plt.legend()


x = [math.log(e, 2) for e in x]
y1 = [math.log(e, 2) for e in y1]
y2 = [math.log(e, 2) for e in y2]
y3 = [math.log(e, 2) for e in y3]
y4 = [math.log(e, 2) for e in y4]
y5 = [math.log(e, 2) for e in y5]

plt.figure(2)
plt.plot(x, y1, label='8n')
plt.plot(x, y2, label='4n*log(n)')
plt.plot(x, y3, label='2*n^2')
plt.plot(x, y4, label='n^3')
plt.plot(x, y5, label='2^n')
plt.legend()

plt.show()
