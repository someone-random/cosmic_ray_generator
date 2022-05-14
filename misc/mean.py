import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

import functions

E = np.linspace(0.01,500,num=500)
y = functions.composite(E_mu=E)
x = E * y

plt.plot(E,y)
plt.plot(E,x)

def wrapper(x):
	return (x * functions.composite(E_mu=x))

def norm(x):
	return (functions.composite(E_mu=x))

print("Mean and error of composite()")

print(integrate.quad(wrapper,0,np.inf)[0]/integrate.quad(norm,0,np.inf)[0])
print(integrate.quad(wrapper,0,np.inf)[1]/integrate.quad(norm,0,np.inf)[0])

print("Mean and error of supressed theory()")

def wrapper(x):
	return (x * functions.theory_supressed(E_mu=x))

def norm(x):
	return (functions.theory_supressed(E_mu=x))

print(integrate.quad(wrapper,0,np.inf)[0]/integrate.quad(norm,0,np.inf)[0])
print(integrate.quad(wrapper,0,np.inf)[1]/integrate.quad(norm,0,np.inf)[0])

plt.ylim([0, 10])
plt.show()