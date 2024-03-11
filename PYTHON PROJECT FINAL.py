#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:10:13 2022

@author: ethangrella
"""

fp = open('/Users/ethangrella/Dropbox/Mac/Downloads/gaussian.csv', 'r')
x = "Null"
n = 0
sum = 0
while(x != ""):
    x = fp.readline()
    if x != "":
        y = float(x)
        n += 1
        sum = sum + y
average = sum/n
fp.close()

print(average)


import matplotlib.pyplot as plt
import numpy as n

def histogram_(list_x, list_y):
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(list_x, list_y)
    plt.show()
    
fp = open('/Users/ethangrella/Dropbox/Mac/Downloads/gaussian.csv', 'r')
x = "NA"
d = dict()
while(x != ""):
    x = fp.readline()
    if x != "":
        if x[-1] == '\n':
            y = float(x[:-1])
            d[y] = d.get(y, 0) + 1
        else:
            y = float(x)
            d[y] = d.get(y, 0) + 1
print(d)
fp.close()

histogram_(d.keys(), d.values())
    











