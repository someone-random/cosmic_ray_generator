import numpy as np
import functions
from matplotlib import pyplot as plt
 
e = np.logspace(-2,6, num=120)
theory = functions.theory(E_mu=e,theta=0)*e**3
fit = functions.best_fit(E_mu=e)*e**3
combined = (functions.composite(e))*e**3

le = np.log10(e)
lfit = np.log10(fit)
ltheory = np.log10(theory)
delta = np.log10(np.abs(theory-fit))
lcombined = np.log10(combined)

fig = plt.figure()
ax = plt.axes()
ax.plot(le,lfit,label="fit")
ax.plot(le,ltheory,label="theory")
ax.plot(le,lcombined,label="combined")

ax.set_ylim([-2,5])

plt.legend()

np.savetxt("combined_data.csv", np.stack((e,combined), axis=1), delimiter='\t')


plt.show()