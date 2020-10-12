import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
#from matplotlib import colors, ticker, cm
#import scipy.interpolate
#from matplotlib.mlab import bivariate_normal
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as mtick
#from scipy.stats import linregress
import os.path
#from scipy.interpolate import InterpolatedUnivariateSpline
import scipy.interpolate


###########################################################################
########################## Plotting calculations ##########################
###########################################################################

font = {'family' : 'URW Gothic',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)
#
#legend_params={
#'framealpha' : 1,
#'fontsize':14, 
#'handletextpad':0.3, 
#'labelspacing':0.1, 
#'borderaxespad':0.1
#}
#
#plt.rc('legend', **legend_params)




######################################
############ Total rate ##############
######################################

raw=np.loadtxt("from_anna_T150/PhotonRate_Brems.txt")
pT_brem = raw[:,0]
dN_brem = raw[:,-2]
dN_brem_err = raw[:,-1]
dN_brem[dN_brem < 1e-100] = 1e-100
pre_interp_brem = scipy.interpolate.interp1d(pT_brem, np.log(dN_brem), kind='linear')
pre_interp_brem_err = scipy.interpolate.interp1d(pT_brem, np.log(dN_brem_err), kind='linear')
interp_brem=lambda x: np.exp(pre_interp_brem(x))
interp_brem_err=lambda x: np.exp(pre_interp_brem_err(x))

raw=np.loadtxt("from_anna_T150/PhotonRate_2to2.txt")
pT_22 = raw[:,0]
dN_22=raw[:,-2]-(raw[:,1]+raw[:,3])
dN_22_err=raw[:,-1]+(raw[:,2]+raw[:,4])
dN_22[dN_22<1e-100]=1e-100
pre_interp_22 = scipy.interpolate.interp1d(pT_22, np.log(dN_22), kind='linear')
pre_interp_22_err = scipy.interpolate.interp1d(pT_22, np.log(dN_22_err), kind='linear')
interp_22 = lambda x: np.exp(pre_interp_22(x))
interp_22_err = lambda x: np.exp(pre_interp_22_err(x))

raw=np.loadtxt("thermal_photons/pi_rho_to_pi_gamma.dat")
pT_jf_22 = raw[:,0]
dN_jf_22 = raw[:,1]

raw=np.loadtxt("thermal_photons/pion_brem_rapp.dat")
pT_jf_brem = raw[:,0]
dN_jf_brem= raw[:,1]

raw=np.loadtxt("thermal_photons/total_hadronic_rate_for_test.dat")
pT_jf_total = raw[:,0]
dN_jf_total = raw[:,1]
#interp_jf = scipy.interpolate.interp1d(pT_jf, np.log(dN_jf), kind='linear')

plt.figure()
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,3.8)
plt.ylim(1e-15,1e-3)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$P^0 d^3{\Gamma}/d3p$ $(GeV^{-2} fm^{-4})$')

plt.text(0.28, 0.9, 'Line: Analytical\nPoint: SMASH', horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes)

resampled_smash_pT=np.linspace(np.max([pT_brem[0],0.2]),np.max(pT_brem),20)
plt.errorbar(x=resampled_smash_pT, y=interp_brem(resampled_smash_pT)+interp_22(resampled_smash_pT), yerr=interp_brem_err(resampled_smash_pT)+interp_22_err(resampled_smash_pT),fmt="D", color='black', label="Total") 
plt.errorbar(x=resampled_smash_pT, y=interp_brem(resampled_smash_pT), yerr=interp_brem_err(resampled_smash_pT),fmt="D", color='red', label=r"$\pi \pi \to \pi \pi \gamma$") 
plt.errorbar(x=resampled_smash_pT, y=interp_22(resampled_smash_pT), yerr=interp_22_err(resampled_smash_pT),fmt="D", color='blue', label=r"$\pi \rho \to \pi \gamma$") 

plt.plot(pT_jf_total,dN_jf_total,"-", color='black') 
plt.plot(pT_jf_brem,dN_jf_brem,"-.", color='red') 
plt.plot(pT_jf_22,dN_jf_22,":", color='blue') 

plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.savefig("thermal_photon_comparison.pdf")
plt.show()



#plt.figure()
#plt.title("Total hadronic rate comparison")
#plt.xscale('linear')
#plt.yscale('linear')
#plt.xlim(0,4)
#plt.ylim(0.5,2.0)
#plt.xlabel(r'$p_T$ $(GeV)$')
#plt.ylabel(r'Ratio of rates')
#
#plt.plot(pT_jf,dN_jf/(interp_brem(pT_jf)+interp_22(pT_jf)),"-", color='black', label="JF/SMASH") 
#
#plt.legend(loc='upper right')
#plt.tight_layout()
#plt.savefig("ratio_thermal_photon_total_rate_used_for_comparison_hydro_vs_smash.pdf")
#plt.show()
