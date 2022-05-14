import scipy.integrate as integrate
import numpy as np
import functions
import matplotlib.pyplot as plt


def function(x,theta):
	return functions.composite(E_mu=x,theta=theta)

X = np.logspace(-2,5,num=40)

integral = np.array([integrate.quad(function,a=0,b=y,args=(0,)) for y in X])

results = np.concatenate((np.expand_dims(X,1),integral),axis=1)

plt.semilogx(X,results[:,1], label="results")
plt.legend()
plt.show()