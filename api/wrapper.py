from .rejection_sampler import generator

def create(n=1,llim=0,ulim=1000, with_angles=True,times=False,detector_area=None):
    gen=generator(llim=llim,ulim=ulim,with_angles=with_angles, times=times, detector_area=detector_area)
    return gen.create(n)