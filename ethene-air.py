import numpy as np
import cantera as ct
import math
import csv
import matplotlib.pyplot as plt

mech = 'gri30.cti' 
gas = ct.Solution('gri30.xml')

#mieszanka
T = 1000.0
P = 200000
X = 'C2H4:0.5 O2:3 N2:11.28' 
gas.TPX = T,P,X

r=ct.Reactor(gas)
sim=ct.ReactorNet([r])

times=np.zeros(2000)
data=np.zeros([2000,4])

tk=0.5

dt=tk/2000
time=0
n=0

while n<2000:
        time+=dt
        sim.advance(time)
        times[n]=time
        data[n,0]=r.T
        #data[n,1]=r.thermo('OH')
        #data[n,2]=r.thermo('C2H4')
        #data[n,3]=r.thermo('O2')
        data[n,1:]=r.thermo['O2', 'H' , 'C2H4'].X
    
        #print('%10.3e %10.3f %10.3f %14.6e' % (sim.time, r.T, r.thermo.v, r.thermo.u))
        n += 1
    
    
plt.plot(times,data[:,0])
plt.show()

plt.plot(times,data[:,1])
plt.show()

plt.plot(times,data[:,2])
plt.show()

plt.plot(times,data[:,3])
plt.show()