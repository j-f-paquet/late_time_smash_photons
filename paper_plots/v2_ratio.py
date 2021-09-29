import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as mtick
import os.path
import scipy.interpolate
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting
from matplotlib import gridspec

######################################
############ Total rate ##############
######################################

# SMASH RHIC
# SP_v2_photons_2to2.txt  SP_v2_photons_Brems.txt  SP_v2_photons_total.txt
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/SP_v2_photons_total.txt")
pT_smash_rhic, v2_tot_rhic, v2_tot_err_rhic = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/SP_v2_photons_2to2.txt")
pT_smash_22_rhic, v2_22_rhic, v2_err_22_rhic = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/SP_v2_photons_Brems.txt")
pT_smash_brem_rhic, v2_brem_rhic, v2_err_brem_rhic = raw.T

# Hydro RHIC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_above_Tfr_rhic, v1_above_Tfr_rhic, v2_above_Tfr_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/tot_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_140_150_tot_rhic, v1_music_140_150_tot_rhic, v2_music_140_150_tot_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/22_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_140_150_22_rhic, v1_music_140_150_22_rhic, v2_music_140_150_22_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_140_150_brem_rhic, v1_music_140_150_brem_rhic, v2_music_140_150_brem_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/tot_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_120_150_tot_rhic, v1_music_120_150_tot_rhic, v2_music_120_150_tot_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/22_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_120_150_22_rhic, v1_music_120_150_22_rhic, v2_music_120_150_22_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_120_150_brem_rhic, v1_music_120_150_brem_rhic, v2_music_120_150_brem_rhic, *rest = raw.T


plot_dict_rhic={
'late_tot':{
'smash_calcs':[pT_smash_rhic,v2_tot_rhic,v2_tot_err_rhic],
'music_calcs_short':[pT_music_rhic, v2_music_140_150_tot_rhic, v2_music_120_150_tot_rhic]
},
'late_22':{
'smash_calcs':[pT_smash_22_rhic,v2_22_rhic,v2_err_22_rhic],
'music_calcs_short':[pT_music_rhic, v2_music_140_150_22_rhic, v2_music_120_150_22_rhic]
},
'late_brem':{
'smash_calcs':[pT_smash_brem_rhic,v2_brem_rhic,v2_err_brem_rhic],
'music_calcs_short':[pT_music_rhic, v2_music_140_150_brem_rhic, v2_music_120_150_brem_rhic]
},
}



# SMASH LHC
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/SP_v2_photons_total.txt")
pT_smash_lhc, v2_tot_lhc, v2_tot_err_lhc = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/SP_v2_photons_2to2.txt")
pT_smash_22_lhc, v2_22_lhc, v2_err_22_lhc = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/SP_v2_photons_Brems.txt")
pT_smash_brem_lhc, v2_brem_lhc, v2_err_brem_lhc = raw.T

# Hydro RHIC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/photons_above_Tfr_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_above_Tfr_lhc, v1_above_Tfr_lhc, v2_above_Tfr_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/tot_photons_T140-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_140_150_tot_lhc, v1_music_140_150_tot_lhc, v2_music_140_150_tot_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/22_photons_T140-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_140_150_22_lhc, v1_music_140_150_22_lhc, v2_music_140_150_22_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/brem_photons_T140-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_140_150_brem_lhc, v1_music_140_150_brem_lhc, v2_music_140_150_brem_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/tot_photons_T120-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_120_150_tot_lhc, v1_music_120_150_tot_lhc, v2_music_120_150_tot_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/22_photons_T120-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_120_150_22_lhc, v1_music_120_150_22_lhc, v2_music_120_150_22_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/brem_photons_T120-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_120_150_brem_lhc, v1_music_120_150_brem_lhc, v2_music_120_150_brem_lhc, *rest = raw.T


plot_dict_lhc={
'late_tot':{
'smash_calcs':[pT_smash_lhc,v2_tot_lhc,v2_tot_err_lhc],
'music_calcs_short':[pT_music_lhc, v2_music_140_150_tot_lhc, v2_music_120_150_tot_lhc]
},
'late_22':{
'smash_calcs':[pT_smash_22_lhc,v2_22_lhc,v2_err_22_lhc],
'music_calcs_short':[pT_music_lhc, v2_music_140_150_22_lhc, v2_music_120_150_22_lhc]
},
'late_brem':{
'smash_calcs':[pT_smash_brem_lhc,v2_brem_lhc,v2_err_brem_lhc],
'music_calcs_short':[pT_music_lhc, v2_music_140_150_brem_lhc, v2_music_120_150_brem_lhc]
},
}

box = dict(facecolor='white', edgecolor='black', linewidth=0.8)

y_lower_lim = 0.5
y_upper_lim = 2.5

gs = gridspec.GridSpec(9,11)
common_plotting.load_plotting_style_paper()
#Make this figure higher than the others and adjust fonts, for readability
mpl.rcParams['figure.figsize'] = 10*0.6, 5.3*0.8*1.6
# mpl.rcParams['axes.labelsize'] = 15
# mpl.rcParams['legend.fontsize'] = 11
plt.figure()

# RHIC
ax1 = plt.subplot(gs[:3 , 1:6])
plt.title(r'Au + Au @ $\sqrt{s}$ = 200 GeV')
smash_calc=plot_dict_rhic['late_22']['smash_calcs']
# plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
# plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
music_calc=plot_dict_rhic['late_22']['music_calcs_short']
plt.plot(music_calc[0], smash_calc[1]/((music_calc[1]+music_calc[2])*0.5), alpha=1.0, color = 'C2', label = 'MUSIC mean', lw = 2.0, ls = '--')
plt.fill_between(music_calc[0], smash_calc[1]/music_calc[1], smash_calc[1]/music_calc[2], alpha=0.5, color = 'C2', label = 'MUSIC range', lw = 0)


plt.legend(frameon = False, loc = 'lower right')
plt.xlim(0,2.6)
plt.ylim(y_lower_lim, y_upper_lim)
plt.xticks([])
# plt.yticks([0,5,10,15,20,25])
# ax1.minorticks_on()
plt.figtext(0.435, 0.91725, '2$\leftrightarrow$2 Scatterings', fontweight = 'bold', bbox=box)

ax2 = plt.subplot(gs[3:6 , 1:6])
smash_calc=plot_dict_rhic['late_brem']['smash_calcs']
music_calc=plot_dict_rhic['late_brem']['music_calcs_short']
plt.plot(music_calc[0], smash_calc[1]/((music_calc[1]+music_calc[2])*0.5), alpha=1.0, color = 'C1', label = 'MUSIC mean', lw = 2.0, ls = ':')
plt.fill_between(music_calc[0], smash_calc[1]/music_calc[1], smash_calc[1]/music_calc[2], alpha=0.5, color = 'C1', label = 'MUSIC range', lw = 0)

plt.legend(frameon = False, loc = 'lower right')
plt.xlim(0,2.6)
plt.ylim(y_lower_lim, y_upper_lim)
plt.xticks([])
# plt.yticks([0,5,10,15,20,25])
# ax2.minorticks_on()
plt.ylabel(r'v$_{2 \quad \mathsf{SMASH}}^{\gamma, \mathsf{SP}}$ / v$_{2 \quad \mathsf{MUSIC}}^{\gamma, \mathsf{SP}}$ ')
plt.figtext(0.445, 0.6316, 'Bremsstrahlung', fontweight = 'bold', bbox=box)

ax3 = plt.subplot(gs[6:9 , 1:6])
smash_calc=plot_dict_rhic['late_tot']['smash_calcs']
music_calc=plot_dict_rhic['late_tot']['music_calcs_short']
plt.plot(music_calc[0], smash_calc[1]/((music_calc[1]+music_calc[2])*0.5), alpha=1.0, color = 'C0', label = 'MUSIC mean', lw = 2.0)
plt.fill_between(music_calc[0], smash_calc[1]/music_calc[1], smash_calc[1]/music_calc[2], alpha=0.5, color = 'C0', label = 'MUSIC range', lw = 0)
plt.xlim(0,2.6)
plt.ylim(y_lower_lim, y_upper_lim)
# plt.yticks([0,5,10,15,20,25])
# ax3.minorticks_on()
plt.legend(frameon = False, loc = 'lower right')
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.figtext(0.51, 0.3452, 'Total', fontweight = 'bold', bbox=box)

# LHC

ax4 = plt.subplot(gs[:3 , 6:])
plt.title(r'Pb + Pb @ $\sqrt{s}$ = 2.76 TeV')
smash_calc=plot_dict_lhc['late_22']['smash_calcs']
music_calc=plot_dict_lhc['late_22']['music_calcs_short']
plt.plot(music_calc[0], smash_calc[1]/((music_calc[1]+music_calc[2])*0.5), alpha=1.0, color = 'C2', label = 'MUSIC mean', lw = 2.0, ls = '--')
plt.fill_between(music_calc[0], smash_calc[1]/music_calc[1], smash_calc[1]/music_calc[2], alpha=0.5, color = 'C2', label = 'MUSIC range', lw = 0)
plt.xlim(0,2.6)
plt.ylim(y_lower_lim, y_upper_lim)
plt.xticks([])
# plt.yticks([0,5,10,15,20,25])
ax4.set_yticklabels([])
# plt.figtext(0.83, 0.89, '2$\leftrightarrow$2 Scatterings', fontweight = 'bold')

ax5 = plt.subplot(gs[3:6 , 6:])
smash_calc=plot_dict_lhc['late_brem']['smash_calcs']
music_calc=plot_dict_lhc['late_brem']['music_calcs_short']
plt.plot(music_calc[0], smash_calc[1]/((music_calc[1]+music_calc[2])*0.5), alpha=1.0, color = 'C1', label = 'MUSIC mean', lw = 2.0, ls = ':')
plt.fill_between(music_calc[0], smash_calc[1]/music_calc[1], smash_calc[1]/music_calc[2], alpha=0.5, color = 'C1', label = 'MUSIC range', lw = 0)
plt.xlim(0,2.6)
plt.ylim(y_lower_lim, y_upper_lim)
plt.xticks([])
# plt.yticks([0,5,10,15,20,25])
ax5.set_yticklabels([])
# plt.figtext(0.835, 0.63, 'Bremsstrahlung', fontweight = 'bold')

ax6 = plt.subplot(gs[6:9 , 6:])
smash_calc=plot_dict_lhc['late_tot']['smash_calcs']
music_calc=plot_dict_lhc['late_tot']['music_calcs_short']
plt.plot(music_calc[0], smash_calc[1]/((music_calc[1]+music_calc[2])*0.5), alpha=1.0, color = 'C0', label = 'MUSIC mean', lw = 2.0)
plt.fill_between(music_calc[0], smash_calc[1]/music_calc[1], smash_calc[1]/music_calc[2], alpha=0.5, color = 'C0', label = 'MUSIC range', lw = 0)
plt.xlim(0,2.6)
plt.ylim(y_lower_lim, y_upper_lim)
# plt.yticks([])
# plt.yticks([0,5,10,15,20,25])
ax6.set_yticklabels([])
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
# plt.figtext(0.93, 0.36, 'Total', fontweight = 'bold')

plt.figtext(0.79, 0.927, "SMASH-2.0.1-1-g397f8f0",color = "gray", fontsize = 6.3)
plt.tight_layout(h_pad=-0.2, w_pad=-4.6)
plt.savefig("v2_ratio.pdf")
plt.close()
