# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 09:44:28 2019

@author: Nicklas
"""

import numpy as np
from scipy import sin, cos, pi
import scipy as sp
import matplotlib as mp
import matplotlib.pyplot as pp
from matplotlib.pyplot import plot

pp.close('all')
channels = np.linspace(1,2048,2048);
E = -0.0722955 + 0.0311853 * channels
dataCs = np.loadtxt("Cs137_1152s.txt", comments="#")     
dataAm = np.loadtxt("Am241_426s.txt", comments="#") 
dataFe = np.loadtxt("Fe55_1200s.txt", comments="#") 


pp.figure(1,figsize=(12,8))
pp.subplot(3,1,1)
plot(E,dataCs, label="Cs137")
#pp.title("Cs137")
pp.legend()
pp.xlabel("E [kEv]")

pp.subplot(3,1,2)
plot(E,dataAm, label="Am241")
#pp.title("Am241")
pp.legend()
pp.xlabel("E [kEv]")

pp.subplot(3,1,3)
plot(E,dataFe, label="Fe55")
#pp.title("Fe55")
pp.legend()
pp.xlabel("E [kEv]")

pp.suptitle("Spectra of sources")
#pp.close('all')

#%%
pp.close('all')
data12kV = np.loadtxt("x-spectra/12kV.txt")
data24kV = np.loadtxt("x-spectra/24kV.txt")
data36kV = np.loadtxt("x-spectra/36.1kV.txt")

pp.figure(2,figsize=(12,8))
pp.subplot(3,1,1)
plot(E, data12kV, label="12kV")
pp.legend()
pp.xlabel("E [kEv]")
pp.yscale("log")

pp.subplot(3,1,2)
plot(E, data24kV, label="24kV")
pp.legend()
pp.xlabel("E [kEv]")
pp.yscale("log")

pp.subplot(3,1,3)
plot(E, data36kV, label="36kV")
pp.legend()
pp.xlabel("E [kEv]")
pp.yscale("log")
