# this calculates probability of detection of gigantic jet and sprites
# assuming skCUBE detection of 1 signal from lightning per orbit

nligs = 3000. # estimated number of classical lightning per minute (Christian et al., 2003). 
ngiganticjets = 0.01 # estimated number of gigantic jets per minute  (Chen et al, 2010). 
nsprites = 0.5 # estimated number of sprits per minute (Chen et al, 2010). 

probLIG_vs_GJ =  nligs/ngiganticjets # detection probability of classical lightning relative to gigantic jets
probLIG_vs_SP =  nligs/nsprites # detection probability classical lightning relative to sprites

print('Detection probability of classical lightning relative to gigantic jets: ',probLIG_vs_GJ)
print('Detection probability of classical lightning relative to sprites: ',probLIG_vs_SP)

# let us assume a whistler detection of 1 lighting per 1 orbit of skCUBE over 2 years (life expectancy of skCUBE)

nminutes = 60. # number of minutes per hour
nhours = 24.   # number of hours per day
ndays = 365.   # number of days per year
nyears = 2.    # number of years of skCUBE on orbit
orbit_duration = 90. # 90 minutes LEO

nwhistlers_per_day =  nhours*nminutes/orbit_duration
nwhistlers_per_year = ndays*nwhistlers_per_day
nwhistlers_per_two_years = nyears*nwhistlers_per_year # Total number of whistlers detection in 2 years (assumed 1 detection per orbit)

print('Total number of whistlers detection in 2 years (assumed 1 detection per orbit): ',nwhistlers_per_two_years)

# the detection probability of gigantic jet will be nwhistlers_per_two_years/probLIG_vs_GJ

# we make the assumption that 1 detected whistler per orbit is directly proportional to total number of classical lightning per minute
# detection probability of classical lightning (3000 per min) relative to detection of gigantic jet (0.01 per min) is ratio 3000/0.01 = 300000.
# THIS MEANS THAT DETECTION OF A CLASSICAL LIGHTNING IS 300000x MORE PROBABLE THAN DETECTION OF A GIGANTIC JET
# BUT DETECTION OF GIGANTIC JET IS 300000x LESS PROBABLE
# detection probability of classical lightning (3000 per min) relative to detection of sprite (0.5 per min) is ration 3000/0.5 = 6000.
# THIS MEANS THAT DETECTION OF A CLASSICAL LIGHTNING is 6000x MORE PROBABLE THAN DETECTION OF A SPRITE   
# BUT DETECTION OF A SPRITE IS 6000x LESS PROBABLE

print('Detection probability of a gigantic jet will be nwhistlers_per_two_years/probLIG_vs_GJ: ',nwhistlers_per_two_years/probLIG_vs_GJ)
print('Detection probability of a sprite will be nwhistlers_per_two_years/probLIG_vs_GJ: ',nwhistlers_per_two_years/probLIG_vs_SP) 








