import functions
import numpy as np

test_range = np.linspace(-100,100,num=50)

output = functions.composite(test_range)

print(np.stack((test_range,output), axis=1))