import numpy as np

def skcubeatt(power,n,R):

    Iavg = power/(4.*np.pi*(R**2))

    permeability_vacuum = 4.*np.pi*1.e-7 # in T . V/m
    c = 3.e8 # speed of light in vacuum in m/s

    Em = 2.*Iavg*permeability_vacuum*c
    Bm = (n/c)*Em

    Bmeasured = 53.e-12 # in T # 53 pT

    damping = 11. # in dB due to skelet (upper limit)
    dmp     = 10**(damping/20.)
#    print("damping " + str(damping) + " dB: amplitude ratio",str(np.round(dmp,1)))

    Bmdmp = Bm/dmp
    dBatt = 20.*np.log10(Bmdmp/Bmeasured)

#    print(Bmdmp*1.e12,Bmeasured*1.e12,Bmdmp/Bmeasured)	  
	
    return dBatt

