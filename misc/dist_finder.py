import scipy.optimize as opt
import functions
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stat


import rejection_sampler as rs

a=0.5

e = np.linspace(0,20,num=1000)
X = functions.composite(E_mu=e)
power = a*e**(a-1)

plt.loglog(e,X)
plt.loglog(e,power)

plt.show()