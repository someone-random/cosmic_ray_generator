import numpy as np
import functions
from scipy import optimize

e = np.logspace(-3,8, num=100000000)
theory = functions.theory(E_mu=e,theta=0)*e**3
fit = functions.best_fit(E_mu=e)*e**3

delta = np.log10(np.abs(theory-fit))

stacked = np.stack((e,delta), axis=1)

print(stacked[np.argmin(stacked[:, 1]), 0])

