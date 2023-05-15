"""
Rejection sampler for production of sea-level cosmic rays using the functions described in functions.py. This revolves around the generator class and its methods.
"""

import numpy as np
import numpy.random as random
from .functions import *
import scipy.optimize as opt
from scipy import integrate



class generator:
	def __init__(self,llim=0,ulim=1000, with_angles=True,times=False,detector_area=None):
		"""
		Initialisation of cosmic ray generator. User can supply upper and lower limit energy values, and specify whether to calculate at the zenith or at any angle with the with_angles boolean, and wether to create times with the times boolean
		"""
		self.with_angles = with_angles
		self.llim = llim
		self.ulim = ulim
		self.times = times
		self.detector_area = detector_area
		self.function = integrated_fast if with_angles else composite
		
	def wrapper(self,x):
		"""
		Wrapper (for maximum finding) for the correct PDF in functions.py depending on self.with_angles boolean.
		"""
		output = -integrated_fast(E_mu=x) if self.with_angles else -composite(E_mu=x)
		return output
	
	def wrapper2(self,theta,x):
		"""
		Wrapper (for maximum finding) for the correct PDF in functions.py depending on self.with_angles boolean.
		"""
		output = -theory_supressed(E_mu=x,theta=theta)
		return output

	def create(self,n=1):
		"""
		Wrapper for the with_angle or no_angle generator methods. Also creates and stacks particle times. Returns nx3 array with columns energy,angle,time, with the relevant zeros if not selected. Units are GeV, rad and s.
		"""
		output = self.create_with_angle(n=n) if self.with_angles else self.create_no_angle(n=n)
		output = np.concatenate((output,self.time_creator(n)),axis=1)
		return output
	

	def create_no_angle(self,n=1):
		"""
		Creates n particles, returns nx1 NumPy array of momenta (GeV/c) and zenith angle (rad) (zenith angles all zero) from functions.composite_function.
		"""
		isfinished = False
		output_arr = []
		maximum = opt.fminbound(self.wrapper,x1=self.llim, x2=self.ulim,disp=False,full_output=True)
		
		while not isfinished:
			random_x = random.uniform(low=self.llim,high=self.ulim)
			#random_x = random.triangular(left=self.llim, mode=maximum[0], right=self.ulim)
			random_y = random.uniform(low=0,high=-maximum[1])
			if random_y <= self.function(random_x):
				output_arr.append([random_x,0])
			isfinished = False if len(output_arr) < n else True
		return np.array(output_arr)

	def create_with_angle(self, n=1):
		'''
		New function for creating muons with angles.
		'''
		output_arr=[]
		energies=self.create_no_angle(n=n)
		
		for E in energies:
			maximum = opt.fmin(self.wrapper2,x0=20,disp=False, full_output=True,args=(E[0],))
			
			finished=False
			while not finished:
				random_x=random.uniform(low=0,high=np.pi/2)
				random_y=random.uniform(low=0,high=-maximum[1])

				if random_y<=theory_supressed(E_mu=E[0],theta=random_x):
					output_arr.append(np.append(E[0],random_x))
					finished=True
		return np.array(output_arr)

	def time_creator(self,n):
		"""
		Creates the times for particles to arrive, 
		"""
		if isinstance(self.detector_area, type(None)) & self.times:
			raise Exception("If you specify times = True you must provide a detector area with the detector_area argument")
		if self.times:
			scaling=64.12300/integrate.quad(integrated_fast, a=self.llim, b=self.ulim)[0]
			rate = 86.607*2*np.pi * self.detector_area*10**-4 /scaling
			scale = 1/rate
			times = np.cumsum(random.exponential(scale=scale,size=n))
		else:
			times = np.zeros(shape=n)
		return np.expand_dims(times, axis=1)


