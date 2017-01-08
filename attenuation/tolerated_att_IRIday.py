import numpy as np
import matplotlib.pyplot as plt
import attfncts

def SetMatplotlibParams():
#	plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    plt.rc('font',**{'family':'serif','serif':['Times New Roman']})
    plt.rc('font',size=30.)
    plt.rc('lines',linewidth=2,markeredgewidth=2.,markersize=10)
    plt.rc('axes',linewidth=1.5)
    plt.rcParams['xtick.major.size']=8.
    plt.rcParams['xtick.minor.size']=4.
    plt.rcParams['figure.subplot.bottom']=0.13
    plt.rcParams['figure.subplot.left']=0.17	

SetMatplotlibParams()
	
Re = 6371200.0 # earth's radius
c = 2.99792458e8 # speed of light
freq = []

infile2000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst2000.0.npz'
nphasedata2000 = np.load(infile2000)

freqb2000  = nphasedata2000['arr_0']
radius2000 = nphasedata2000['arr_1']
nphase2000 = nphasedata2000['arr_2']

infile4000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst4000.0.npz'
nphasedata4000 = np.load(infile4000)

freqb4000  = nphasedata4000['arr_0']
radius4000 = nphasedata4000['arr_1']
nphase4000 = nphasedata4000['arr_2']

infile6000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst6000.0.npz'
nphasedata6000 = np.load(infile6000)

freqb6000  = nphasedata6000['arr_0']
radius6000 = nphasedata6000['arr_1']
nphase6000 = nphasedata6000['arr_2']

infile8000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst8000.0.npz'
nphasedata8000 = np.load(infile8000)

freqb8000  = nphasedata8000['arr_0']
radius8000 = nphasedata8000['arr_1']
nphase8000 = nphasedata8000['arr_2']

infile10000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst10000.0.npz'
nphasedata10000 = np.load(infile10000)

freqb10000  = nphasedata10000['arr_0']
radius10000 = nphasedata10000['arr_1']
nphase10000 = nphasedata10000['arr_2']

infile12000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst12000.0.npz'
nphasedata12000 = np.load(infile12000)

freqb12000  = nphasedata12000['arr_0']
radius12000 = nphasedata12000['arr_1']
nphase12000 = nphasedata12000['arr_2']

infile14000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst14000.0.npz'
nphasedata14000 = np.load(infile14000)

freqb14000  = nphasedata14000['arr_0']
radius14000 = nphasedata14000['arr_1']
nphase14000 = nphasedata14000['arr_2']

infile16000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst16000.0.npz'
nphasedata16000 = np.load(infile16000)

freqb16000  = nphasedata16000['arr_0']
radius16000 = nphasedata16000['arr_1']
nphase16000 = nphasedata16000['arr_2']

infile18000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst18000.0.npz'
nphasedata18000 = np.load(infile18000)

freqb18000  = nphasedata18000['arr_0']
radius18000 = nphasedata18000['arr_1']
nphase18000 = nphasedata18000['arr_2']

infile20000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst20000.0.npz'
nphasedata20000 = np.load(infile20000)

freqb20000  = nphasedata20000['arr_0']
radius20000 = nphasedata20000['arr_1']
nphase20000 = nphasedata20000['arr_2']

infile22000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst22000.0.npz'
nphasedata22000 = np.load(infile22000)

freqb22000  = nphasedata22000['arr_0']
radius22000 = nphasedata22000['arr_1']
nphase22000 = nphasedata22000['arr_2']

infile24000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst24000.0.npz'
nphasedata24000 = np.load(infile24000)

freqb24000  = nphasedata24000['arr_0']
radius24000 = nphasedata24000['arr_1']
nphase24000 = nphasedata24000['arr_2']

infile26000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst26000.0.npz'
nphasedata26000 = np.load(infile26000)

freqb26000  = nphasedata26000['arr_0']
radius26000 = nphasedata26000['arr_1']
nphase26000 = nphasedata26000['arr_2']

infile28000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst28000.0.npz'
nphasedata28000 = np.load(infile28000)

freqb28000  = nphasedata28000['arr_0']
radius28000 = nphasedata28000['arr_1']
nphase28000 = nphasedata28000['arr_2']

infile30000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst30000.0.npz'
nphasedata30000 = np.load(infile30000)

freqb30000  = nphasedata30000['arr_0']
radius30000 = nphasedata30000['arr_1']
nphase30000 = nphasedata30000['arr_2']

infile32000 = 'nphaseIRI2012vsR_iono_iriri_2012_25962_day.lst32000.0.npz'
nphasedata32000 = np.load(infile32000)

freqb32000  = nphasedata32000['arr_0']
radius32000 = nphasedata32000['arr_1']
nphase32000 = nphasedata32000['arr_2']

#print(nphasedata['arr_2'])

#plt.semilogx(radius,nphase)

fig=plt.figure(1,figsize=(9,8))

xmin = 60.   # min x boundary for plotting
xmax = 4000. # max x boundary for plotting
ymin = 1.   # min y boundary for plotting 
ymax = 200.  # max y boundary for plotting

plt.axis([xmin,xmax,ymin,ymax])	

plt.semilogx((np.asarray(radius2000)-Re)/1.e3,np.asarray(nphase2000),label=r'freq 2000 Hz')
#plt.semilogx((np.asarray(radius4000)-Re)/1.e3,np.asarray(nphase4000),label=r'freq 4000 Hz')
#plt.semilogx((np.asarray(radius6000)-Re)/1.e3,np.asarray(nphase6000),label=r'freq 6000 Hz')
plt.semilogx((np.asarray(radius8000)-Re)/1.e3,np.asarray(nphase8000),label=r'freq 8000 Hz')
#plt.semilogx((np.asarray(radius10000)-Re)/1.e3,np.asarray(nphase10000),label=r'freq 10000 Hz')
#plt.semilogx((np.asarray(radius12000)-Re)/1.e3,np.asarray(nphase12000),label=r'freq 12000 Hz')
plt.semilogx((np.asarray(radius14000)-Re)/1.e3,np.asarray(nphase14000),label=r'freq 14000 Hz')
#plt.semilogx((np.asarray(radius16000)-Re)/1.e3,np.asarray(nphase16000),label=r'freq 16000 Hz')
#plt.semilogx((np.asarray(radius18000)-Re)/1.e3,np.asarray(nphase18000),label=r'freq 18000 Hz')
plt.semilogx((np.asarray(radius20000)-Re)/1.e3,np.asarray(nphase20000),label=r'freq 20000 Hz')
#plt.semilogx((np.asarray(radius22000)-Re)/1.e3,np.asarray(nphase22000),label=r'freq 22000 Hz')
#plt.semilogx((np.asarray(radius24000)-Re)/1.e3,np.asarray(nphase24000),label=r'freq 24000 Hz')
plt.semilogx((np.asarray(radius26000)-Re)/1.e3,np.asarray(nphase26000),label=r'freq 26000 Hz')
#plt.semilogx((np.asarray(radius28000)-Re)/1.e3,np.asarray(nphase28000),label=r'freq 28000 Hz')
#plt.semilogx((np.asarray(radius30000)-Re)/1.e3,np.asarray(nphase30000),label=r'freq 30000 Hz')
plt.semilogx((np.asarray(radius32000)-Re)/1.e3,np.asarray(nphase32000),label=r'freq 32000 Hz')

#for i in freqb:
#    plt.semilogx((np.asarray(radius)-ray_cmks.Re)/1.e3,np.asarray(nphase),label=r'freq [Hz]: '+str(freqb[i]))

plt.xlabel(r'r (km)')
plt.ylabel(r'phase refractive index')
plt.legend(loc=1,prop={'size':22})
plt.title(r'day')

perigeum = 450. 
apogeum = 720.

plt.axvspan(perigeum, apogeum, color='y', alpha=0.5, lw=0)

dir='./'
name='phaserefindexday'

plt.savefig(dir+name+'.png')

nperigeum2000hz = round(np.interp(perigeum,(radius2000-Re)/1.e3,nphase2000),1)
nperigeum4000hz = round(np.interp(perigeum,(radius4000-Re)/1.e3,nphase4000),1)
nperigeum6000hz = round(np.interp(perigeum,(radius6000-Re)/1.e3,nphase6000),1)
nperigeum8000hz = round(np.interp(perigeum,(radius8000-Re)/1.e3,nphase8000),1)
nperigeum10000hz = round(np.interp(perigeum,(radius10000-Re)/1.e3,nphase10000),1)
nperigeum12000hz = round(np.interp(perigeum,(radius12000-Re)/1.e3,nphase12000),1)
nperigeum14000hz = round(np.interp(perigeum,(radius14000-Re)/1.e3,nphase14000),1)
nperigeum16000hz = round(np.interp(perigeum,(radius16000-Re)/1.e3,nphase16000),1)
nperigeum18000hz = round(np.interp(perigeum,(radius18000-Re)/1.e3,nphase18000),1)
nperigeum20000hz = round(np.interp(perigeum,(radius20000-Re)/1.e3,nphase20000),1)
nperigeum22000hz = round(np.interp(perigeum,(radius22000-Re)/1.e3,nphase22000),1)
nperigeum24000hz = round(np.interp(perigeum,(radius24000-Re)/1.e3,nphase24000),1)
nperigeum26000hz = round(np.interp(perigeum,(radius26000-Re)/1.e3,nphase26000),1)
nperigeum28000hz = round(np.interp(perigeum,(radius28000-Re)/1.e3,nphase28000),1)
nperigeum30000hz = round(np.interp(perigeum,(radius30000-Re)/1.e3,nphase30000),1)
nperigeum32000hz = round(np.interp(perigeum,(radius32000-Re)/1.e3,nphase32000),1)

nperigeum = []

nperigeum.append(nperigeum2000hz)
nperigeum.append(nperigeum4000hz)
nperigeum.append(nperigeum6000hz)
nperigeum.append(nperigeum8000hz)
nperigeum.append(nperigeum10000hz)
nperigeum.append(nperigeum12000hz)
nperigeum.append(nperigeum14000hz)
nperigeum.append(nperigeum16000hz)
nperigeum.append(nperigeum18000hz)
nperigeum.append(nperigeum20000hz)
nperigeum.append(nperigeum22000hz)
nperigeum.append(nperigeum24000hz)
nperigeum.append(nperigeum26000hz)
nperigeum.append(nperigeum28000hz)
nperigeum.append(nperigeum30000hz)
nperigeum.append(nperigeum32000hz)

napogeum2000hz = round(np.interp(apogeum,(radius2000-Re)/1.e3,nphase2000),1)
napogeum4000hz = round(np.interp(apogeum,(radius4000-Re)/1.e3,nphase4000),1)
napogeum6000hz = round(np.interp(apogeum,(radius6000-Re)/1.e3,nphase6000),1)
napogeum8000hz = round(np.interp(apogeum,(radius8000-Re)/1.e3,nphase8000),1)
napogeum10000hz = round(np.interp(apogeum,(radius10000-Re)/1.e3,nphase10000),1)
napogeum12000hz = round(np.interp(apogeum,(radius12000-Re)/1.e3,nphase12000),1)
napogeum14000hz = round(np.interp(apogeum,(radius14000-Re)/1.e3,nphase14000),1)
napogeum16000hz = round(np.interp(apogeum,(radius16000-Re)/1.e3,nphase16000),1)
napogeum18000hz = round(np.interp(apogeum,(radius18000-Re)/1.e3,nphase18000),1)
napogeum20000hz = round(np.interp(apogeum,(radius20000-Re)/1.e3,nphase20000),1)
napogeum22000hz = round(np.interp(apogeum,(radius22000-Re)/1.e3,nphase22000),1)
napogeum24000hz = round(np.interp(apogeum,(radius24000-Re)/1.e3,nphase24000),1)
napogeum26000hz = round(np.interp(apogeum,(radius26000-Re)/1.e3,nphase26000),1)
napogeum28000hz = round(np.interp(apogeum,(radius28000-Re)/1.e3,nphase28000),1)
napogeum30000hz = round(np.interp(apogeum,(radius30000-Re)/1.e3,nphase30000),1)
napogeum32000hz = round(np.interp(apogeum,(radius32000-Re)/1.e3,nphase32000),1)

napogeum = []

napogeum.append(napogeum2000hz)
napogeum.append(napogeum4000hz)
napogeum.append(napogeum6000hz)
napogeum.append(napogeum8000hz)
napogeum.append(napogeum10000hz)
napogeum.append(napogeum12000hz)
napogeum.append(napogeum14000hz)
napogeum.append(napogeum16000hz)
napogeum.append(napogeum18000hz)
napogeum.append(napogeum20000hz)
napogeum.append(napogeum22000hz)
napogeum.append(napogeum24000hz)
napogeum.append(napogeum26000hz)
napogeum.append(napogeum28000hz)
napogeum.append(napogeum30000hz)
napogeum.append(napogeum32000hz)

print('nperigeum2000hz,napogeum2000hz',nperigeum2000hz,napogeum2000hz)
print('nperigeum4000hz,napogeum4000hz',nperigeum4000hz,napogeum4000hz)
print('nperigeum6000hz,napogeum6000hz',nperigeum6000hz,napogeum6000hz)
print('nperigeum8000hz,napogeum8000hz',nperigeum8000hz,napogeum8000hz)
print('nperigeum10000hz,napogeum10000hz',nperigeum10000hz,napogeum10000hz)
print('nperigeum12000hz,napogeum12000hz',nperigeum12000hz,napogeum12000hz)
print('nperigeum14000hz,napogeum14000hz',nperigeum14000hz,napogeum14000hz)
print('nperigeum16000hz,napogeum16000hz',nperigeum16000hz,napogeum16000hz)
print('nperigeum18000hz,napogeum18000hz',nperigeum18000hz,napogeum18000hz)
print('nperigeum20000hz,napogeum20000hz',nperigeum20000hz,napogeum20000hz)
print('nperigeum22000hz,napogeum22000hz',nperigeum22000hz,napogeum22000hz)
print('nperigeum24000hz,napogeum24000hz',nperigeum24000hz,napogeum24000hz)
print('nperigeum26000hz,napogeum26000hz',nperigeum26000hz,napogeum26000hz)
print('nperigeum28000hz,napogeum28000hz',nperigeum28000hz,napogeum28000hz)
print('nperigeum30000hz,napogeum30000hz',nperigeum30000hz,napogeum30000hz)
print('nperigeu32000hz,napogeum32000hz',nperigeum32000hz,napogeum32000hz)

#fig=plt.figure(2,figsize=(9,8))

#plt.plot(freq)

power_min = 0.1e9 # 0.1 GW
power_max = 1.e9  # 1 GW

freq.append(freqb2000)
freq.append(freqb4000)
freq.append(freqb6000)
freq.append(freqb8000)
freq.append(freqb10000)
freq.append(freqb12000)
freq.append(freqb14000)
freq.append(freqb16000)
freq.append(freqb18000)
freq.append(freqb20000)
freq.append(freqb22000)
freq.append(freqb24000)
freq.append(freqb26000)
freq.append(freqb28000)
freq.append(freqb30000)
freq.append(freqb32000)

fig=plt.figure(2,figsize=(9,8))

plt.plot(np.asarray(freq)/1.e3,np.asarray(nperigeum),label=r'n perigeum')
plt.plot(np.asarray(freq)/1.e3,np.asarray(napogeum),label=r'n apogeum')

plt.xlabel(r'frequency (kHz)')
plt.ylabel(r'phase refractive index')
plt.legend(loc=1,prop={'size':22})
plt.title(r'')

dir='./'
name='phaserefindexvsfrequencyday'

plt.savefig(dir+name+'.png')

bmaxPowerMin2000HzPer = attfncts.skcubeatt(power_min,nperigeum2000hz,perigeum*1.e3)
bmaxPowerMin4000HzPer = attfncts.skcubeatt(power_min,nperigeum4000hz,perigeum*1.e3)
bmaxPowerMin6000HzPer = attfncts.skcubeatt(power_min,nperigeum6000hz,perigeum*1.e3)
bmaxPowerMin8000HzPer = attfncts.skcubeatt(power_min,nperigeum8000hz,perigeum*1.e3)
bmaxPowerMin10000HzPer = attfncts.skcubeatt(power_min,nperigeum10000hz,perigeum*1.e3)
bmaxPowerMin12000HzPer = attfncts.skcubeatt(power_min,nperigeum12000hz,perigeum*1.e3)
bmaxPowerMin14000HzPer = attfncts.skcubeatt(power_min,nperigeum14000hz,perigeum*1.e3)
bmaxPowerMin16000HzPer = attfncts.skcubeatt(power_min,nperigeum16000hz,perigeum*1.e3)
bmaxPowerMin18000HzPer = attfncts.skcubeatt(power_min,nperigeum18000hz,perigeum*1.e3)
bmaxPowerMin20000HzPer = attfncts.skcubeatt(power_min,nperigeum20000hz,perigeum*1.e3)
bmaxPowerMin22000HzPer = attfncts.skcubeatt(power_min,nperigeum22000hz,perigeum*1.e3)
bmaxPowerMin24000HzPer = attfncts.skcubeatt(power_min,nperigeum24000hz,perigeum*1.e3)
bmaxPowerMin26000HzPer = attfncts.skcubeatt(power_min,nperigeum26000hz,perigeum*1.e3)
bmaxPowerMin28000HzPer = attfncts.skcubeatt(power_min,nperigeum28000hz,perigeum*1.e3)
bmaxPowerMin30000HzPer = attfncts.skcubeatt(power_min,nperigeum30000hz,perigeum*1.e3)
bmaxPowerMin32000HzPer = attfncts.skcubeatt(power_min,nperigeum32000hz,perigeum*1.e3)

bmaxPowerMinPer = []

bmaxPowerMinPer.append(bmaxPowerMin2000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin4000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin6000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin8000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin10000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin12000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin14000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin16000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin18000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin20000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin22000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin24000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin26000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin28000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin30000HzPer)
bmaxPowerMinPer.append(bmaxPowerMin32000HzPer)

bmaxPowerMax2000HzPer = attfncts.skcubeatt(power_max,nperigeum2000hz,perigeum*1.e3)
bmaxPowerMax4000HzPer = attfncts.skcubeatt(power_max,nperigeum4000hz,perigeum*1.e3)
bmaxPowerMax6000HzPer = attfncts.skcubeatt(power_max,nperigeum6000hz,perigeum*1.e3)
bmaxPowerMax8000HzPer = attfncts.skcubeatt(power_max,nperigeum8000hz,perigeum*1.e3)
bmaxPowerMax10000HzPer = attfncts.skcubeatt(power_max,nperigeum10000hz,perigeum*1.e3)
bmaxPowerMax12000HzPer = attfncts.skcubeatt(power_max,nperigeum12000hz,perigeum*1.e3)
bmaxPowerMax14000HzPer = attfncts.skcubeatt(power_max,nperigeum14000hz,perigeum*1.e3)
bmaxPowerMax16000HzPer = attfncts.skcubeatt(power_max,nperigeum16000hz,perigeum*1.e3)
bmaxPowerMax18000HzPer = attfncts.skcubeatt(power_max,nperigeum18000hz,perigeum*1.e3)
bmaxPowerMax20000HzPer = attfncts.skcubeatt(power_max,nperigeum20000hz,perigeum*1.e3)
bmaxPowerMax22000HzPer = attfncts.skcubeatt(power_max,nperigeum22000hz,perigeum*1.e3)
bmaxPowerMax24000HzPer = attfncts.skcubeatt(power_max,nperigeum24000hz,perigeum*1.e3)
bmaxPowerMax26000HzPer = attfncts.skcubeatt(power_max,nperigeum26000hz,perigeum*1.e3)
bmaxPowerMax28000HzPer = attfncts.skcubeatt(power_max,nperigeum28000hz,perigeum*1.e3)
bmaxPowerMax30000HzPer = attfncts.skcubeatt(power_max,nperigeum30000hz,perigeum*1.e3)
bmaxPowerMax32000HzPer = attfncts.skcubeatt(power_max,nperigeum32000hz,perigeum*1.e3)

bmaxPowerMaxPer = []

bmaxPowerMaxPer.append(bmaxPowerMax2000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax4000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax6000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax8000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax10000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax12000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax14000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax16000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax18000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax20000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax22000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax24000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax26000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax28000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax30000HzPer)
bmaxPowerMaxPer.append(bmaxPowerMax32000HzPer)

bmaxPowerMin2000HzApo = attfncts.skcubeatt(power_min,napogeum2000hz,apogeum*1.e3)
bmaxPowerMin4000HzApo = attfncts.skcubeatt(power_min,napogeum4000hz,apogeum*1.e3)
bmaxPowerMin6000HzApo = attfncts.skcubeatt(power_min,napogeum6000hz,apogeum*1.e3)
bmaxPowerMin8000HzApo = attfncts.skcubeatt(power_min,napogeum8000hz,apogeum*1.e3)
bmaxPowerMin10000HzApo = attfncts.skcubeatt(power_min,napogeum10000hz,apogeum*1.e3)
bmaxPowerMin12000HzApo = attfncts.skcubeatt(power_min,napogeum12000hz,apogeum*1.e3)
bmaxPowerMin14000HzApo = attfncts.skcubeatt(power_min,napogeum14000hz,apogeum*1.e3)
bmaxPowerMin16000HzApo = attfncts.skcubeatt(power_min,napogeum16000hz,apogeum*1.e3)
bmaxPowerMin18000HzApo = attfncts.skcubeatt(power_min,napogeum18000hz,apogeum*1.e3)
bmaxPowerMin20000HzApo = attfncts.skcubeatt(power_min,napogeum20000hz,apogeum*1.e3)
bmaxPowerMin22000HzApo = attfncts.skcubeatt(power_min,napogeum22000hz,apogeum*1.e3)
bmaxPowerMin24000HzApo = attfncts.skcubeatt(power_min,napogeum24000hz,apogeum*1.e3)
bmaxPowerMin26000HzApo = attfncts.skcubeatt(power_min,napogeum26000hz,apogeum*1.e3)
bmaxPowerMin28000HzApo = attfncts.skcubeatt(power_min,napogeum28000hz,apogeum*1.e3)
bmaxPowerMin30000HzApo = attfncts.skcubeatt(power_min,napogeum30000hz,apogeum*1.e3)
bmaxPowerMin32000HzApo = attfncts.skcubeatt(power_min,napogeum32000hz,apogeum*1.e3)

bmaxPowerMinApo = []

bmaxPowerMinApo.append(bmaxPowerMin2000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin4000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin6000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin8000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin10000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin12000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin14000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin16000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin18000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin20000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin22000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin24000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin26000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin28000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin30000HzApo)
bmaxPowerMinApo.append(bmaxPowerMin32000HzApo)


bmaxPowerMax2000HzApo = attfncts.skcubeatt(power_max,napogeum2000hz,apogeum*1.e3)
bmaxPowerMax4000HzApo = attfncts.skcubeatt(power_max,napogeum4000hz,apogeum*1.e3)
bmaxPowerMax6000HzApo = attfncts.skcubeatt(power_max,napogeum6000hz,apogeum*1.e3)
bmaxPowerMax8000HzApo = attfncts.skcubeatt(power_max,napogeum8000hz,apogeum*1.e3)
bmaxPowerMax10000HzApo = attfncts.skcubeatt(power_max,napogeum10000hz,apogeum*1.e3)
bmaxPowerMax12000HzApo = attfncts.skcubeatt(power_max,napogeum12000hz,apogeum*1.e3)
bmaxPowerMax14000HzApo = attfncts.skcubeatt(power_max,napogeum14000hz,apogeum*1.e3)
bmaxPowerMax16000HzApo = attfncts.skcubeatt(power_max,napogeum16000hz,apogeum*1.e3)
bmaxPowerMax18000HzApo = attfncts.skcubeatt(power_max,napogeum18000hz,apogeum*1.e3)
bmaxPowerMax20000HzApo = attfncts.skcubeatt(power_max,napogeum20000hz,apogeum*1.e3)
bmaxPowerMax22000HzApo = attfncts.skcubeatt(power_max,napogeum22000hz,apogeum*1.e3)
bmaxPowerMax24000HzApo = attfncts.skcubeatt(power_max,napogeum24000hz,apogeum*1.e3)
bmaxPowerMax26000HzApo = attfncts.skcubeatt(power_max,napogeum26000hz,apogeum*1.e3)
bmaxPowerMax28000HzApo = attfncts.skcubeatt(power_max,napogeum28000hz,apogeum*1.e3)
bmaxPowerMax30000HzApo = attfncts.skcubeatt(power_max,napogeum30000hz,apogeum*1.e3)
bmaxPowerMax32000HzApo = attfncts.skcubeatt(power_max,napogeum32000hz,apogeum*1.e3)

bmaxPowerMaxApo = []

bmaxPowerMaxApo.append(bmaxPowerMax2000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax4000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax6000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax8000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax10000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax12000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax14000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax16000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax18000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax20000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax22000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax24000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax26000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax28000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax30000HzApo)
bmaxPowerMaxApo.append(bmaxPowerMax32000HzApo)

fig=plt.figure(3,figsize=(9,8))

xmin = 0.   # min x boundary for plotting
xmax = 35. # max x boundary for plotting
ymin = 0.   # min y boundary for plotting 
ymax = 70.  # max y boundary for plotting

plt.axis([xmin,xmax,ymin,ymax])	

plt.plot(np.asarray(freq)/1.e3,np.asarray(bmaxPowerMinPer),label=r'0.1 GW (perigeum 450 km)')
plt.plot(np.asarray(freq)/1.e3,np.asarray(bmaxPowerMaxPer),label=r'1.0 GW (perigeum 450 km)')
plt.plot(np.asarray(freq)/1.e3,np.asarray(bmaxPowerMinApo),label=r'0.1 GW (apogeum 720 km)',linestyle='--')
plt.plot(np.asarray(freq)/1.e3,np.asarray(bmaxPowerMaxApo),label=r'1.0 GW (apogeum 720 km)',linestyle='--')

plt.xlabel(r'frequency (kHz)')
plt.ylabel(r'tolerated attenuation (dB)')
plt.legend(loc=1,prop={'size':22})
plt.title(r'day')

dir='./'
name='toleratedattenuationday'

plt.savefig(dir+name+'.png')




#print(bmaxPowerMin2000Hz,bmaxPowerMax2000Hz)


plt.show()