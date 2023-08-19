# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 16:56:47 2023

@author: viktor
"""
#imports
import numpy as np
import matplotlib.pyplot as plt

#define constants
WA_0 = 532e-9
x_0 = 1    
D_0 = 2e-6 
y = 1   
l_0 = 4e-6
n = 100
x = np.linspace(-0.7,0.7,n)
D_vals = [D_0, 2*D_0, 3*D_0, 4*D_0]
WA_vals = [WA_0, 1.5*WA_0, 2*WA_0, 3*WA_0]
l_vals = [l_0, 1.2*l_0, 1.3*l_0, 1.4*l_0]
N_vals = [3, 4, 5]    

def plot_func(x, y, xlab, ylab, title, label = "", legend = False):
    plt.plot(x, y, label = label)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    if legend:
        plt.legend(loc = "upper right")
    
def single_slit(WA, D, x):
    return ((np.sin((np.pi*D*x)/(WA*y)))/((np.pi*D*x)/(WA*y)))**2

def double_slit(WA, D, x, l):
    return single_slit(WA, D, x)*(np.cos((np.pi*l*x)/(WA*y)))**2

def diffraction_slit(WA, D, x, l, N):
    return single_slit(WA, D, x)*(np.sin((N*np.pi*l*x)/(WA*y))/(N*np.sin((np.pi*l*x)/(WA*y))))**2

#Task 1

for D in D_vals:
    I = single_slit(WA_0, D, x)
    plot_func(x,I, "x", "Intensity", "Intesity as a function of x for single split with varying D", label = "D = " + str(D) , legend = True )
plt.show()

for WA in WA_vals:
    I = single_slit(WA, D_0, x)
    plot_func(x,I, "x", "Intensity", "Intesity as a function of x for single split with varying wavelength", label = "lambda = " + str(WA) , legend = True )
plt.show()

#Task 2
for l in l_vals:
    I = double_slit(WA_0, D_0, x, l)
    plot_func(x,I, "x", "Intensity", "Intesity as a function of x for double split with varying l", label = "l = " + str(l) , legend = True )
plt.show()

#Task 3
for N in N_vals:
    I = diffraction_slit(WA_0, D_0, x, l_0, N)
    plot_func(x,I, "x", "Intensity", "Intesity as a function of x for diffraction split with varying N", label = "N = " + str(N) , legend = True )
plt.show()

