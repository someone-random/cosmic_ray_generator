import numpy as np
import matplotlib.pyplot as plt
import functions
import matplotlib
matplotlib.rcParams['font.family'] = 'CMU Serif'

fracs = [0,0.9,0.92,0.96,0.98,1]

E = np.linspace(0,50, num=100)

thetas = [frac * np.pi/2 for frac in fracs]

for theta in thetas:
	Y = functions.theory_supressed(E_mu=E,theta=theta)
	Y = Y/np.nanmax(Y)
	plt.plot(E,Y,label="Theta = {theta:.2f}".format(theta = np.rad2deg(theta)))

plt.legend()
plt.xlabel("Muon Energy/(Gev/c)")
plt.ylabel("PDF (normalised to 1 at maximum)")
plt.tight_layout()
plt.xlim([0,50])
plt.ylim([0,1.1])
plt.show()