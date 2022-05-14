import numpy as np
import functions
from matplotlib import pyplot as plt
 
e = np.logspace(-3,5, num=50)
theta = np.linspace(-np.pi/4,np.pi/4,num=50)

E, THETA = np.meshgrid(e,theta)

Z = functions.theory(E,THETA)*E**3

elog = np.log10(E)
zlog = np.log10(Z)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(elog,THETA,zlog)



plt.show()