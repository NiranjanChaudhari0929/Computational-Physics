import numpy as np
from matplotlib import pyplot as plt
import random

N_particle=int(input('number of particle :'))
Tot_energy=float(input('enter total amount of energy :'))
MCS=int(input('enter number of MCS steps: '))
dvmax=float(input('enter max change in velocity : '))
demon_energy=0
vo=np.sqrt(Tot_energy/N_particle)  #initial velocity
velocity=np.zeros(N_particle,float)    #N_particle number of zeroes
ipart=0   #just initialising it
vtrial=0
de=0

delta_v=np.zeros(MCS,dtype=float) #array of zeroes


for i in range(N_particle):
    velocity[i]=vo     #the first velocity element of the particles

for i in range(MCS):
    for j in range(N_particle):
        dv=(2*random.random()-1)*dvmax
        ipart=np.random.randint(1,N_particle) #selecting a random integer between 1 and N_particle
        vtrial=velocity[ipart]+dv         #velocity change for that part
        delta_v[i]=dv                     
        de=0.5*(vtrial**2-(velocity[ipart])**2)

        if de<0 :
            demon_energy=demon_energy+ abs(de)
            velocity[ipart]=vtrial
        if 0<de and de<demon_energy :
            demon_energy=demon_energy-de
            velocity[ipart]=vtrial


plt.plot(np.arange(MCS),delta_v)   #isnt dv chnge in velcoity ...and MCS is arranged between 0 to MCS
plt.show()
