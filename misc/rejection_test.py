import scipy.optimize as opt
import functions
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import rejection_sampler as rs
import matplotlib


matplotlib.rcParams['font.family'] = 'CMU Serif'
start = time.time()

generator = rs.generator(with_angles=True,ulim=1000)

data = pd.DataFrame(generator.create(n=20000))

print("Time taken for 10,000:",time.time() - start)

data.columns = ["Energies","Angles"]
data["log10ek"] = data.apply(lambda row: np.log10(row.Energies),axis=1)
data['zenithdeg'] = data.apply(lambda row: np.rad2deg(row.Angles),axis=1)

hist_data_ek,bins_ek = np.histogram(data["log10ek"],bins=60)
hist_data_angle, bins_angle = np.histogram(data["zenithdeg"],bins=60)

data.to_csv("cos2.csv")

hist_data_angle.tofile("angle.csv",sep='\t')
hist_data_ek.tofile("energy.csv",sep='\t')

bins_angle.tofile("angle_bins.csv",sep='\t')
bins_ek.tofile("energy_bins.csv",sep='\t')


fig,ax = plt.subplots(1,2)

data.hist(column = "log10ek",ax=ax[0],bins=60)
data.hist(column = "zenithdeg",ax=ax[1],bins=60)

plt.tight_layout()

plt.show()