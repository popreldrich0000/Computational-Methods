# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 02:27:27 2021

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt

T=[]
for i in range(100):
    T.append(1)
t = np.asarray(T)
x = np.linspace(0, 10, 100)
fig = plt.figure()
ax = fig.add_subplot()
plt.ylim(-2.5,2.5)
plt.xlim(-0.5,10.5)


for i in range(100000):
    t = t + 0.00001*i
    y = np.sin(-x + 4 * t)
    y1 = np.sin(x + 4 * t)
    y2 = y + y1
    ln, = plt.plot(x,y)
    ln1, = plt.plot(x,y1)
    ln2, = plt.plot(x,y2)
    plt.pause(0.00001)
    ln.remove()
    ln1.remove()
    ln2.remove()
    

