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
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting

######################################
############ Total rate ##############
######################################

# SMASH
# SP_v2_photons_2to2.txt  SP_v2_photons_Brems.txt  SP_v2_photons_total.txt
raw=np.loadtxt("../../calcs/photons/smash_calcs/rhic/SP_v2_photons_Brems.txt")
pT_smash_brem, v2_brem, v2_err_brem = raw.T

# Hydro
raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_brem, v1_music_140_150_brem, v2_music_140_150_brem, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T140-150_nx200_modified_brem/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_brem_softer, v1_music_140_150_brem_softer, v2_music_140_150_brem_softer, *rest = raw.T

plot_dict={
'late_brem':{
'name' : 'Bremsstrahlung',
'smash_calcs':[pT_smash_brem,v2_brem,v2_err_brem],
'music_calcs_orig':[pT_music, v2_music_140_150_brem],
'music_calcs_softer':[pT_music, v2_music_140_150_brem_softer],
'label':r"$\pi \pi \to \pi \pi \gamma$",
#'plot_text':"Photons produced\nafter particlization\n"r"$\pi \pi \to \pi \pi \gamma$",
'plot_text_position':(0.55, 0.88),
'xloc_text' : 0.68
},
}

#############################
# Single line plot with proxy
#############################

for filelabel, tmp_dict in plot_dict.items():

    common_plotting.load_plotting_style()
    plt.figure()
    plt.xscale('linear')
    plt.yscale('linear')
    plt.xlim(0,2.5)
    plt.ylim(-1,25.0)
    plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
    plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')

    #SMASH
    smash_calc=tmp_dict['smash_calcs']
    plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '--')
    plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)

    # MUSIC
    music_calc=tmp_dict['music_calcs_orig']
    plt.plot(music_calc[0], 100.0 * music_calc[1], color = 'C0', label = 'MUSIC$_\mathsf{HRG}$' )

    music_calc=tmp_dict['music_calcs_softer']
    plt.plot(music_calc[0], 100.0 * music_calc[1], color = 'green', label = 'MUSIC$_\mathsf{HRG}$, softer rate' )

    plt.figtext(tmp_dict['xloc_text'], 0.9, tmp_dict['name'], fontweight = 'bold')
    plt.legend(frameon = False, loc = 'upper left')
    plt.tight_layout()
    plt.savefig("v2_"+filelabel+"_single-line_proxy.pdf")
    plt.close()


##############################
## with bands
##############################
#
#for filelabel, tmp_dict in plot_dict.items():
#
#    common_plotting.load_plotting_style()
#    plt.figure()
#    plt.xscale('linear')
#    plt.yscale('linear')
#    plt.xlim(0,2.5)
#    plt.ylim(-1,25.0)
#    plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
#    plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')
#
#    # SMASH
#    smash_calc=tmp_dict['smash_calcs']
#    plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
#    plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
#
#    # MUSIC long
#    music_calc=tmp_dict['music_calcs_long']
#    label=tmp_dict['label']
#    plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=0.7, color = 'C1', label = 'MUSIC$_\mathsf{HRG}$: 100 MeV < T < 150 MeV', lw = 0)
#
#    # MUSIC short
#    music_calc=tmp_dict['music_calcs_short']
#    label=tmp_dict['label']
#    plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=0.7, color = 'C0', label = 'MUSIC$_\mathsf{HRG}$: 120 MeV < T < 150 MeV', lw = 0)
#
#    plt.figtext(tmp_dict['xloc_text'], 0.9, tmp_dict['name'], fontweight = 'bold')
#    plt.legend(frameon = False, loc = 'upper left')
#    plt.tight_layout()
#    plt.savefig("v2_"+filelabel+"_range_T.pdf")
#    plt.close()
