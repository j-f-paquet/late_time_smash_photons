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

# SMASH
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/pT_photons_midy.txt")
pT_smash, pre_dN_22, pre_dN_22_err, pre_dN_brem, pre_dN_brem_err = raw.T
dN_22=pre_dN_22/(2*np.pi*pT_smash)
dN_22_err=pre_dN_22_err/(2*np.pi*pT_smash)
dN_brem=pre_dN_brem/(2*np.pi*pT_smash)
dN_brem_err=pre_dN_brem_err/(2*np.pi*pT_smash)

# Hydro+rate
#photons_T140-150_nx200/vn_rate_hg_ideal_Turbide_fit_noPiPi_tabulated.dat
#photons_T140-150_nx200/vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated.dat
#photons_T140-150_nx200/vn_rate_thermal_ideal.dat
#photons_above_Tfr_nx200/vn_rate_hg_ideal_Turbide_fit_noPiPi_tabulated.dat
#photons_above_Tfr_nx200/vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated.dat
#photons_above_Tfr_nx200/vn_rate_qgp_ideal_LO_AMYfit.dat
#photons_above_Tfr_nx200/vn_rate_thermal_ideal.dat

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_above, dN_music_above, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_smash_tot.dat")
pT_above_plus_smash, dN_music_above_plus_smash, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140, dN_music_above_plus_hydro140, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120, dN_music_above_plus_hydro120, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T100-150.dat")
pT_above_plus_hydro100, dN_music_above_plus_hydro100, *rest = raw.T



plt.figure()
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-5,1e2)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$P^0 d^3{N_\gamma}/d3p$ $(GeV^{-2})$')

plt.text(0.2, 0.9, 'Points: SMASH\nLight bands:    Hydro, 100<T<150 MeV\nDarker bands: Hydro, 120<T<150 MeV', horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=14)

plt.plot(pT_above, dN_music_above,"-", color='black', label=r"Hydro (T>150 MeV)") 

plt.plot(pT_above_plus_smash, dN_music_above_plus_smash,"D", color='green', label=r"Hydro (T>150 MeV) + SMASH") 
#ax3.fill_between(x, y1, y2)
#plt.errorbar(x=pT_above_plus_smash, y=::3], yerr=dN_brem_err[::3], fmt='D', color='red') 
#plt.errorbar(x=pT_smash[::3], y=dN_22[::3], yerr=dN_22_err[::3], fmt='D', color='blue') 

plt.fill_between(pT_above_plus_hydro100, dN_music_above_plus_hydro140, dN_music_above_plus_hydro100, color='green', alpha=0.4) 
plt.fill_between(pT_above_plus_hydro100, dN_music_above_plus_hydro140, dN_music_above_plus_hydro120, color='green', alpha=0.3) 

plt.legend(loc='lower left', fontsize=10)
plt.tight_layout()
plt.savefig("spectra_photon_sum.pdf")
plt.show()



