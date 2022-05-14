import numpy as np
import functions
import matplotlib.pyplot as plt

E = np.logspace(-2, 6,num=200)

theory = functions.theory(E_mu=E)*E**3
comp = functions.composite(E_mu=E) * E**3
supressed = functions.theory_supressed(E_mu=E)*E**3

plt.loglog(E,theory)
plt.loglog(E,comp)
plt.loglog(E,supressed)

plt.show()

#for i in range(len(E)):
#	print(E[i],comp[i],sep='\t')

