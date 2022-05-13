"""
Rejection sampler for production of sea-level cosmic rays using the functions described in functions.py. 
"""

import numpy as np
import sys
import numpy.random as random
import functions
import scipy.optimize as opt



class generator:
	def __init__(self,llim=0,ulim=1000, with_angles=True, sim_angles=False):
		self.with_angles = with_angles
		self.sim_angles = sim_angles
		self.llim = llim
		self.ulim = ulim
		self.function = functions.theory_supressed if with_angles else functions.theory
		
	def wrapper(self,x,theta):
		"""
		Wrapper (for maximum finding) for the correct PDF in functions.py depending on self.with_angles boolean.
		"""
		output = -functions.theory_supressed(E_mu=x,theta=theta) if self.with_angles else -functions.composite(E_mu=x)
		return output

	def angle_generator(self,n=1):
		"""
		Generates n angles according to cos^2 distribution or simulation data
		"""
		isfinished = False
		return_angles = []

		if self.sim_angles:
			return_angles = np.zeros(n)
		else:
			while not isfinished:
				thetamin = 0
				thetamax = np.pi/2
				random_theta = random.uniform(low=thetamin,high=thetamax)
				random_y = random.rand()
				if random_y <= np.cos(random_theta)**2:
					return_angles.append(random_theta)
				isfinished = False if len(return_angles) < n else True
		
		return return_angles

	def create(self,n=1):
		"""
		Wrapper for the with_angle or no_angle generator methods.
		"""
		output = self.create_with_angle(n=n) if self.with_angles else self.create_no_angle(n=n)
		return output
	

	def create_no_angle(self,n=1):
		"""
		Creates n particles, returns nx1 NumPy array of momenta (GeV/c) and zenith angle (rad) (zenith angles all zero) from functions.composite_function.
		"""
		isfinished = False
		output_arr = []
		maximum = opt.fmin(self.wrapper,x0=20,disp=False,full_output=True,args=(0,))

		while not isfinished:
			random_x = random.uniform(low=self.llim,high=self.ulim)
			#random_x = random.triangular(left=self.llim, mode=maximum[0], right=self.ulim)
			random_y = random.uniform(low=0,high=-maximum[1])
			if random_y <= self.function(E_mu = random_x):
				output_arr.append([random_x,0])
			isfinished = False if len(output_arr) < n else True
		
		return np.array(output_arr)

	def create_with_angle(self,n=1):
		"""
		Creates n particles, returns nx2 array of momenta (GeV/c) and zenith angle (rad) sampled from functions.theory_supressed.
		"""
	
		output_arr = []

		angles = self.angle_generator(n=n)

		for angle in angles:
			maximum = opt.fmin(self.wrapper,x0=20,disp=False, full_output=True,args=(angle,))
			isfinished = False

			while not isfinished:
				random_x = random.triangular(left=self.llim, mode=maximum[0], right=self.ulim)
				random_y = random.uniform(low=0,high=-maximum[1])
				if random_y <= self.function(E_mu = random_x, theta=angle):
					output_arr.append(np.append(random_x,angle))
					isfinished = True
			
	
		return np.array(output_arr)


