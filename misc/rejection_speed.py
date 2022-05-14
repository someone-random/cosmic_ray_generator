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

generator = rs.generator(with_angles=False,ulim=10000)

data = pd.DataFrame(generator.create(n=1000))

print("Time taken for 10,000:",time.time() - start)
