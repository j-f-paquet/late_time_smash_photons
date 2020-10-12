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

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_above, dN_music_above, v1_above, v2_above, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_smash_tot.dat")
pT_above_plus_smash, dN_music_above_plus_smash, v1_music_above_plus_smash, v2_music_above_plus_smash, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140, dN_music_above_plus_hydro140, v1_music_above_plus_hydro140, v2_music_above_plus_hydro140, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120, dN_music_above_plus_hydro120, v1_music_above_plus_hydro120, v2_music_above_plus_hydro120, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T100-150.dat")
pT_above_plus_hydro100, dN_music_above_plus_hydro100, v1_music_above_plus_hydro100, v2_music_above_plus_hydro100, *rest = raw.T

raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SP_v2_photons_total.txt")
pT_smash, v2_smash, v2_smash_err = raw.T

# Handle differences in the p_T bins
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/pT_photons_midy.txt")
pT_smash_dN, pre_dN_22, pre_dN_22_err, pre_dN_brem, pre_dN_brem_err = raw.T
dN_22=pre_dN_22/(2*np.pi*pT_smash_dN)
dN_22_err=pre_dN_22_err/(2*np.pi*pT_smash_dN)
dN_brem=pre_dN_brem/(2*np.pi*pT_smash_dN)
dN_brem_err=pre_dN_brem_err/(2*np.pi*pT_smash_dN)

pre_log_dN_smash=scipy.interpolate.interp1d(pT_smash_dN, np.log(dN_22+dN_brem), kind='linear',  fill_value=np.NaN, bounds_error=False)
dN_smash=np.exp(pre_log_dN_smash(pT_smash))

above_log_dN_interp = scipy.interpolate.interp1d(pT_above, np.log(dN_music_above), kind='linear',  fill_value=np.NaN, bounds_error=False)
above_dN_interp = lambda pT : np.exp(above_log_dN_interp(pT))
above_v2_interp = scipy.interpolate.interp1d(pT_above, v2_above, kind='linear',  fill_value=np.NaN, bounds_error=False)

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/tot_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_120_150, dN_music_120_150_tot, v1_music_120_150_tot, v2_music_120_150_tot, *rest = raw.T


plt.figure()
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,4)
plt.ylim(0,0.05)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$v_2^{\gamma}\{SP\}$')

plt.plot(pT_above, v2_above,"o", color='black', label=r"Hydro (T>150 MeV)") 

plt.plot(pT_above_plus_smash, v2_music_above_plus_smash,"D", color='green', label=r"Hydro (T>150 MeV) + SMASH") 
plt.plot(pT_smash, above_v2_interp(pT_smash)+dN_smash/above_dN_interp(pT_smash)*(v2_smash-above_v2_interp(pT_smash)),":", color='green', label=r"") 

plt.plot(pT_above_plus_hydro120, v2_music_above_plus_hydro120,"^", color='red', label=r"Hydro (T>120 MeV)") 
plt.plot(pT_music_120_150, above_v2_interp(pT_music_120_150)+dN_music_120_150_tot/above_dN_interp(pT_music_120_150)*(v2_music_120_150_tot-above_v2_interp(pT_music_120_150)),":", color='red', label=r"") 

plt.text(0.05, 0.55, "Points: Full calculations\n"r"Dashed lines: $v_2^{sum}=v_2^{ref}+\frac{dN/dp_T}{dN^{ref}/dp_T}(v_2-v_2^{ref})$", horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=12)

plt.legend(loc='upper left', fontsize=14)
plt.tight_layout()
plt.savefig("v2_sum_diagnostic.pdf")
plt.show()



plt.figure()
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,4)
plt.ylim(0,.5)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$(dN/dp_T)/(dN^{ref}/dp_T)$')

plt.plot(pT_smash, dN_smash/above_dN_interp(pT_smash),":", color='green', label="SMASH") 

plt.plot(pT_music_120_150, dN_music_120_150_tot/above_dN_interp(pT_music_120_150),":", color='red', label=r"Hydro (150>T>120 MeV)") 

plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.savefig("dN_ratio_diagnostic.pdf")
plt.show()



plt.figure()
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,4)
plt.ylim(0,.3)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$v_2-v_2^{ref}$')

plt.plot(pT_smash, v2_smash-above_v2_interp(pT_smash),":", color='green', label="SMASH") 

plt.plot(pT_music_120_150, v2_music_120_150_tot-above_v2_interp(pT_music_120_150),":", color='red', label=r"Hydro (150>T>120 MeV)") 

plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.savefig("v2_difference_diagnostic.pdf")
plt.show()
