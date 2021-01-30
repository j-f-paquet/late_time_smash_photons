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
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SP_v2_photons_total.txt")
pT_smash_rhic, v2_tot_rhic, v2_tot_err_rhic = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SP_v2_photons_2to2.txt")
pT_smash_22_rhic, v2_22_rhic, v2_err_22_rhic = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SP_v2_photons_Brems.txt")
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
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/low_stats/SP_v2_photons_total.txt")
pT_smash_lhc, v2_tot_lhc, v2_tot_err_lhc = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/low_stats/SP_v2_photons_2to2.txt")
pT_smash_22_lhc, v2_22_lhc, v2_err_22_lhc = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/low_stats/SP_v2_photons_Brems.txt")
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

gs = gridspec.GridSpec(9,11)
common_plotting.load_plotting_style_paper()
plt.figure()

# RHIC

ax1 = plt.subplot(gs[:3 , 1:6])
plt.title(r'Au + Au @ $\sqrt{s}$ = 200 GeV')
smash_calc=plot_dict_rhic['late_22']['smash_calcs']
plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
music_calc=plot_dict_rhic['late_22']['music_calcs_short']
plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=1.0, color = 'C0', label = 'MUSIC$_\mathsf{HRG}$', lw = 2.0)
plt.legend(frameon = False, loc = 'upper left')
plt.xlim(0,2.6)
plt.ylim(-2,25.0)
plt.xticks([])
plt.yticks([0,5,10,15,20,25])
# ax1.minorticks_on()
plt.figtext(0.462, 0.868, '2$\leftrightarrow$2 Scatterings', fontweight = 'bold', bbox=box)

ax2 = plt.subplot(gs[3:6 , 1:6])
smash_calc=plot_dict_rhic['late_brem']['smash_calcs']
plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
music_calc=plot_dict_rhic['late_brem']['music_calcs_short']
plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=1.0, color = 'C0', label = 'MUSIC$_\mathsf{HRG}$', lw = 2.0)
# plt.legend(frameon = False, loc = 'upper left')
plt.xlim(0,2.6)
plt.ylim(-2,25.0)
plt.xticks([])
plt.yticks([0,5,10,15,20,25])
# ax2.minorticks_on()
plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')
plt.figtext(0.467, 0.613, 'Bremsstrahlung', fontweight = 'bold', bbox=box)

ax3 = plt.subplot(gs[6:9 , 1:6])
smash_calc=plot_dict_rhic['late_tot']['smash_calcs']
plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
music_calc=plot_dict_rhic['late_tot']['music_calcs_short']
plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=1.0, color = 'C0', label = 'MUSIC$_\mathsf{HRG}$', lw = 2.0)
# plt.legend(frameon = False, loc = 'upper left')
plt.xlim(0,2.6)
plt.yticks([0,5,10,15,20,25])
# ax3.minorticks_on()
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.figtext(0.519, 0.356, 'Total', fontweight = 'bold', bbox=box)

# LHC

ax4 = plt.subplot(gs[:3 , 6:])
plt.title(r'Pb + Pb @ $\sqrt{s}$ = 2760 GeV')
smash_calc=plot_dict_lhc['late_22']['smash_calcs']
plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
music_calc=plot_dict_lhc['late_22']['music_calcs_short']
plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=1.0, color = 'C0', label = 'MUSIC$_\mathsf{HRG}$', lw = 2.0)
# plt.legend(frameon = False, loc = 'upper left')
plt.xlim(0,2.6)
plt.ylim(-2,25.0)
plt.xticks([])
plt.yticks([0,5,10,15,20,25])
ax4.set_yticklabels([])
# plt.figtext(0.83, 0.89, '2$\leftrightarrow$2 Scatterings', fontweight = 'bold')

ax5 = plt.subplot(gs[3:6 , 6:])
smash_calc=plot_dict_lhc['late_brem']['smash_calcs']
plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
music_calc=plot_dict_lhc['late_brem']['music_calcs_short']
plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=1.0, color = 'C0', label = 'MUSIC$_\mathsf{HRG}$', lw = 2.0)
# plt.legend(frameon = False, loc = 'upper left')
plt.xlim(0,2.6)
plt.ylim(-2,25.0)
plt.xticks([])
plt.yticks([0,5,10,15,20,25])
ax5.set_yticklabels([])
# plt.figtext(0.835, 0.63, 'Bremsstrahlung', fontweight = 'bold')

ax6 = plt.subplot(gs[6:9 , 6:])
smash_calc=plot_dict_lhc['late_tot']['smash_calcs']
plt.plot(smash_calc[0], 100.0 * smash_calc[1], color = 'C2', label = 'SMASH', ls = '-')
plt.fill_between(smash_calc[0], 100.0 * (smash_calc[1] - smash_calc[2]), 100.0 * (smash_calc[1] + smash_calc[2]), alpha = 0.5, color = 'C2', lw = 0)
music_calc=plot_dict_lhc['late_tot']['music_calcs_short']
plt.fill_between(music_calc[0], 100.0 * music_calc[1], 100.0 * music_calc[2], alpha=1.0, color = 'C0', label = 'MUSIC$_\mathsf{HRG}$', lw = 2.0)
# plt.legend(frameon = False, loc = 'upper left')
plt.xlim(0,2.6)
plt.ylim(-2,25.0)
plt.yticks([])
plt.yticks([0,5,10,15,20,25])
ax6.set_yticklabels([])
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
# plt.figtext(0.93, 0.36, 'Total', fontweight = 'bold')

plt.tight_layout(h_pad=-0.1, w_pad=-3.4)
plt.savefig("v2.pdf")
plt.close()
