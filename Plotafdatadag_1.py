import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt
import uncertainties as uc
from uncertainties import unumpy as unp
from matplotlib import rc
import matplotlib.pyplot as pyplt

Am=np.loadtxt("day1/Am241_426s.txt",comments="#")[:]
plt.plot(np.linspace(1,np.size(Am),np.size(Am)),Am)


Cs=np.loadtxt("day1/Cs137_1152s.txt", comments="#")[:]
plt.plot(np.linspace(1,np.size(Cs),np.size(Cs)),Cs)

samlet=np.array([np.linspace(1,2048,2048),Cs])
plt.plot(samlet[0,:],samlet[1,:])
plt.show()
