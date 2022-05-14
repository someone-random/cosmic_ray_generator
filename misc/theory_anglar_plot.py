import numpy as np
import time
import functions
from matplotlib import pyplot as plt
from matplotlib import rc
import matplotlib

matplotlib.rcParams['font.family'] = 'CMU Serif'
#rc('mathtext', fontset="custom")
e = np.logspace(2,5,base=10, num=4)

labels = []

for i in e:
	theta = np.linspace(0,np.pi/2,num=120)
	z = functions.theory(E_mu=i,theta=theta)

	znorm = np.log10(z - z.min() + 10)

	label = r"$10^{%.2f}$ GeV" % np.log10(i)
	plt.plot(theta*180/np.pi,znorm,label=label)


plt.xlabel("Zenith Angle/degrees")
plt.ylabel("log10(Flux) normalised to 1 at horizon")
plt.legend(bbox_to_anchor=(1,1), loc="upper left")
plt.tight_layout()
plt.savefig(str(round(time.time())), bbox_inches="tight")
plt.show()