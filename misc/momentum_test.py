import numpy as np
import functions

E = np.logspace(-2, 6,num=120)
p = np.sqrt(E**2 - 0.105658**2)
Y = functions.theory_supressed(E_mu=E)*E**3

for i in range(len(E)):
	print(p[i],Y[i],sep='\t',end='\n')