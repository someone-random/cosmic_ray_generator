import functions as cl
import numpy as np
c = 299792458

energies = np.logspace(-2,6, num=200)

for i in energies:
    print(i,end='\t')
    print(cl.ext_form(i ,0))
