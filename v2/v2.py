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
# SP_v2_photons_2to2.txt  SP_v2_photons_Brems.txt  SP_v2_photons_total.txt
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SP_v2_photons_total.txt")
pT_smash, v2_tot, v2_tot_err = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SP_v2_photons_2to2.txt")
pT_smash_22, v2_22, v2_err_22 = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SP_v2_photons_Brems.txt")
pT_smash_brem, v2_brem, v2_err_brem = raw.T

# Hydro
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_above_Tfr, v1_above_Tfr, v2_above_Tfr, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/tot_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_tot, v1_music_140_150_tot, v2_music_140_150_tot, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/22_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_22, v1_music_140_150_22, v2_music_140_150_22, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/brem_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_brem, v1_music_140_150_brem, v2_music_140_150_brem, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/tot_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_120_150_tot, v1_music_120_150_tot, v2_music_120_150_tot, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/22_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_120_150_22, v1_music_120_150_22, v2_music_120_150_22, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/brem_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_120_150_brem, v1_music_120_150_brem, v2_music_120_150_brem, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/tot_photons_T100-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_100_150_tot, v1_music_100_150_tot, v2_music_100_150_tot, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/22_photons_T100-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_100_150_22, v1_music_100_150_22, v2_music_100_150_22, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/brem_photons_T100-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_100_150_brem, v1_music_100_150_brem, v2_music_100_150_brem, *rest = raw.T


plot_dict={
'late_tot':{
'smash_calcs':[pT_smash,v2_tot,v2_tot_err],
'music_calcs':[pT_music, v2_music_140_150_tot, v2_music_100_150_tot],
'label':r"$\pi \pi \to \pi \pi \gamma$ & $\pi \rho \to \pi \gamma$",
'plot_text':"Photons produced\nafter particlization\n"r"$\pi \pi \to \pi \pi \gamma$ & $\pi \rho \to \pi \gamma$",
'plot_text_position':(0.55, 0.12)
},
'late_22':{
'smash_calcs':[pT_smash_22,v2_22,v2_err_22],
'music_calcs':[pT_music, v2_music_140_150_22, v2_music_100_150_22],
'label':r"$\pi \rho \to \pi \gamma$",
'plot_text':"Photons produced\nafter particlization\n"r"$\pi \rho \to \pi \gamma$",
'plot_text_position':(0.55, 0.12)
},
'late_brem':{
'smash_calcs':[pT_smash_brem,v2_brem,v2_err_brem],
'music_calcs':[pT_music, v2_music_140_150_brem, v2_music_100_150_brem],
'label':r"$\pi \pi \to \pi \pi \gamma$",
'plot_text':"Photons produced\nafter particlization\n"r"$\pi \pi \to \pi \pi \gamma$",
'plot_text_position':(0.55, 0.88)
},
}
#pT_smash_22, v2_22, v2_err_22 = raw.T
#raw=np.loadtxt("smash_calcs/SP_v2_photons_Brems.txt")
#pT_smash_brem, v2_brem, v2_err_brem = raw.T

for filelabel, tmp_dict in plot_dict.items():

    plt.figure()
    plt.xscale('linear')
    plt.yscale('linear')
    plt.xlim(0,4)
    plt.ylim(0,0.25)
    plt.xlabel(r'$p_T$ $(GeV)$')
    plt.ylabel(r'$v_2^{\gamma}\{SP\}$')

    #plt.text(0.2, 0.9, 'Points: SMASH\nLight bands:    Hydro, 100<T<150 MeV\nDarker bands: Hydro, 120<T<150 MeV', horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=14)

    #plt.hlines(psi2_h, 0, 4, color='', linestyle='', label='0

    #pT_smash, v2_tot, v2_tot_err = raw.T
    #pT_smash_22, v2_tot_22, v2_tot_err_22 = raw.T
    #pT_smash_brem, v2_tot_brem, v2_tot_err_brem = raw.T

    smash_calc=tmp_dict['smash_calcs']

    plt.errorbar(x=smash_calc[0], y=smash_calc[1], yerr=smash_calc[2], fmt='D', color='red', label="SMASH") 

    #ax3.fill_between(x, y1, y2)
    #plt.errorbar(x=pT_smash[::3], y=dN_brem[::3], yerr=dN_brem_err[::3], fmt='D', color='red') 
    #plt.errorbar(x=pT_smash[::3], y=dN_22[::3], yerr=dN_22_err[::3], fmt='D', color='blue') 
    #
    music_calc=tmp_dict['music_calcs']
    label=tmp_dict['label']
    plt.fill_between(music_calc[0], music_calc[1], music_calc[2], color='red', alpha=0.3, label=r"Hydrodynamics") #r"$\pi \pi \to \pi \pi \gamma$") 
    #plt.fill_between(pT_music, dN_music_140_150_22, dN_music_100_150_22, color='blue', alpha=0.3, label=r"$\pi \rho \to \pi \gamma$") 
    #
    #plt.fill_between(pT_music, dN_music_140_150_brem, dN_music_120_150_brem, color='red', alpha=0.4) 
    #plt.fill_between(pT_music, dN_music_140_150_22, dN_music_120_150_22, color='blue', alpha=0.4) 

    plt.text(tmp_dict['plot_text_position'][0], tmp_dict['plot_text_position'][1], tmp_dict['plot_text'], horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=13)

    plt.legend(loc='upper left', fontsize=14)
    plt.tight_layout()
    plt.savefig("v2_"+filelabel+".pdf")
    plt.show()



