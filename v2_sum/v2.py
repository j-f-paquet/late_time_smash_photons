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

raw=np.loadtxt("../../photon_calcs/averaged_hydro_calcs/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_above, dN_music_above, v1_above, v2_above, *rest = raw.T

raw=np.loadtxt("../../photon_calcs/averaged_hydro_calcs/combined/average_sp_smash_tot.dat")
pT_above_plus_smash, dN_music_above_plus_smash, v1_music_above_plus_smash, v2_music_above_plus_smash, *rest = raw.T

raw=np.loadtxt("../../photon_calcs/averaged_hydro_calcs/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140, dN_music_above_plus_hydro140, v1_music_above_plus_hydro140, v2_music_above_plus_hydro140, *rest = raw.T

raw=np.loadtxt("../../photon_calcs/averaged_hydro_calcs/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120, dN_music_above_plus_hydro120, v1_music_above_plus_hydro120, v2_music_above_plus_hydro120, *rest = raw.T

raw=np.loadtxt("../../photon_calcs/averaged_hydro_calcs/combined/average_sp_hydro_tot_T100-150.dat")
pT_above_plus_hydro100, dN_music_above_plus_hydro100, v1_music_above_plus_hydro100, v2_music_above_plus_hydro100, *rest = raw.T


plt.figure()
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,4)
plt.ylim(0,0.05)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$v_2^{\gamma}\{SP\}$')

plt.plot(pT_above, v2_above,"-", color='black', label=r"Hydro (T>150 MeV)") 

plt.plot(pT_above_plus_smash, v2_music_above_plus_smash,"D", color='green', label=r"Hydro (T>150 MeV) + SMASH") 

plt.fill_between(pT_above_plus_hydro100,  v2_music_above_plus_hydro140,  v2_music_above_plus_hydro100, color='green', alpha=0.4) 
plt.fill_between(pT_above_plus_hydro100,  v2_music_above_plus_hydro140,  v2_music_above_plus_hydro120, color='green', alpha=0.3) 

plt.text(0.02, 0.7, 'Light bands:    Hydro (T>100 MeV)\nDarker bands: Hydro (T>120 MeV)', horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=14)
#plt.text(0.05, 0.7, 'Points: SMASH\nLight bands:    Hydro, 100<T<150 MeV\nDarker bands: Hydro, 120<T<150 MeV', horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=14)
#
##plt.hlines(psi2_h, 0, 4, color='', linestyle='', label='0
#
##pT_smash, v2_tot, v2_tot_err = raw.T
##pT_smash_22, v2_tot_22, v2_tot_err_22 = raw.T
##pT_smash_brem, v2_tot_brem, v2_tot_err_brem = raw.T
#
#
##ax3.fill_between(x, y1, y2)
##plt.errorbar(x=pT_smash[::3], y=dN_brem[::3], yerr=dN_brem_err[::3], fmt='D', color='red') 
##plt.errorbar(x=pT_smash[::3], y=dN_22[::3], yerr=dN_22_err[::3], fmt='D', color='blue') 
##
#music_calc=tmp_dict['music_calcs']
#label=tmp_dict['label']
#plt.fill_between(music_calc[0], music_calc[1], music_calc[2], color='red', alpha=0.3, label=r"Hydrodynamics") #r"$\pi \pi \to \pi \pi \gamma$") 
##plt.fill_between(pT_music, dN_music_140_150_22, dN_music_100_150_22, color='blue', alpha=0.3, label=r"$\pi \rho \to \pi \gamma$") 
##
##plt.fill_between(pT_music, dN_music_140_150_brem, dN_music_120_150_brem, color='red', alpha=0.4) 
##plt.fill_between(pT_music, dN_music_140_150_22, dN_music_120_150_22, color='blue', alpha=0.4) 

#plt.text(tmp_dict['plot_text_position'][0], tmp_dict['plot_text_position'][1], tmp_dict['plot_text'], horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=13)

plt.legend(loc='upper left', fontsize=14)
plt.tight_layout()
plt.savefig("v2_sum.pdf")
plt.show()



