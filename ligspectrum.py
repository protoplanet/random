# Lightning illumination model Bortnik 2004 and references therein

# Author: Miroslav Mocak
# Date: 13/August/2016

import numpy as np
import matplotlib.pyplot as plt
#import ccgs
#from scipy.integrate import odeint
from scipy.integrate import ode

def SetMatplotlibParams():
#   this routine sets some standard values for matplotlib to obtain publication-quality figures
	
#	plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
    plt.rc('font',size=22.)
    plt.rc('lines',linewidth=2,markeredgewidth=2.,markersize=10)
    plt.rc('axes',linewidth=1.5)
    plt.rcParams['xtick.major.size']=8.
    plt.rcParams['xtick.minor.size']=4.
    plt.rcParams['figure.subplot.bottom']=0.13
    plt.rcParams['figure.subplot.left']=0.17

# ------------------------------------ #
# MAIN 
# ------------------------------------ #
	
# mks units 

z0 = 377. # intrinsic impedance in Ohms
mu0 = 8.854e-12 # permeability of free space 
he = 5.e3 # height of the cloud above the ground (set to 5 km)
i0_1 = -8.e3 # magnitude of the downward moving current 10.53 kA
i0_2 = -10.53e3 # magnitude of the downward moving current 10.53 kA
i0_3 = -12.e3 # magnitude of the downward moving current 10.53 kA
a = 5.e3 # model parameter
b = 1.e5 # model parameter
dgr_kappa = 10.   # angle of observer with respect to zenith
kappa = dgr_kappa*np.pi/180.
R = 500.e3 # distance to observer 100 km

fStop = 3.e4
fInc = 1.e2
freq = np.arange(0., fStop, fInc)
omg = 2.*np.pi*freq

tmp = ((omg**2)*(a-b)**2)/((omg**2+a**2)*(omg**2+b**2))
s1 = (1./z0)*(((mu0*he*i0_1)/(2.*np.pi))**2)*((np.sin(kappa)/R)**2)*tmp
s2 = (1./z0)*(((mu0*he*i0_2)/(2.*np.pi))**2)*((np.sin(kappa)/R)**2)*tmp
s3 = (1./z0)*(((mu0*he*i0_3)/(2.*np.pi))**2)*((np.sin(kappa)/R)**2)*tmp

a = 1.e3 # model parameter
b = 1.e5 # model parameter
tmp = ((omg**2)*(a-b)**2)/((omg**2+a**2)*(omg**2+b**2))
s2_a = (1./z0)*(((mu0*he*i0_2)/(2.*np.pi))**2)*((np.sin(kappa)/R)**2)*tmp

a = 2.e4 # model parameter
b = 1.e5 # model parameter
tmp = ((omg**2)*(a-b)**2)/((omg**2+a**2)*(omg**2+b**2))
s2_b = (1./z0)*(((mu0*he*i0_2)/(2.*np.pi))**2)*((np.sin(kappa)/R)**2)*tmp


# set parameters for plotting
SetMatplotlibParams()

xmin = 0.   # min x boundary for plotting
xmax = 30. # max x boundary for plotting
ymin = 0.   # min y boundary for plotting 
ymax = 2.  # max y boundary for plotting

plt.figure(1,figsize=(8,7))
plt.axis([xmin,xmax,ymin,ymax])	
	
#plt.text(6.,31.,r"Xm = "+str(Xm))
#plt.text(6.,28.,r"Y  = "+str(round(Y,1)))
#plt.text(6.,25.,r"$\Delta$ = i = "+str(dgr_delta0))
#plt.text(6.,22.,r"$\chi$ = " +str(90.-dgr_delta0))
#plt.text(6.,19.,r"f = "+str(round(freq0,1))+" Hz")
#plt.text(6.,16.,r"B = "+str(Bmag)+" Gauss")

plt.plot(freq/1.e3,s1/1.e-24,label=r'-8 kA, a = $5 \times 10^3$, b = $1 \times 10^{5}$')
plt.plot(freq/1.e3,s2/1.e-24,label=r'-10.53 kA, a = $5 \times 10^3$, b = $1 \times 10^{5}$')
plt.plot(freq/1.e3,s3/1.e-24,label=r'-12 kA, a = $5 \times 10^3$, b = $1 \times 10^{5}$')
plt.plot(freq/1.e3,s2_a/1.e-24,color='g',linestyle='--',label=r'-10.53 kA, a = $1 \times 10^3$, b = $1 \times 10^{5}$')
plt.plot(freq/1.e3,s2_b/1.e-24,color='g',linestyle=':',label=r'-10.53 kA, a = $2 \times 10^4$, b = $1 \times 10^{5}$')


plt.xlabel(r"frequency (10$^3$ Hz)")
plt.ylabel(r"S (10$^{-24}$ W m$^{-2}$ Hz$^{-1}$)")
plt.legend(loc=1,prop={'size':16})
#plt.title(r'$\kappa = 10^{o}$')

name='lig1'
#dir='results/'
plt.savefig(name+'.png')

plt.show()