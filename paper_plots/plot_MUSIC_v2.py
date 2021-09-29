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
import matplotlib.gridspec as gridspec


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
'music_calcs_short':[pT_music_rhic, v2_music_140_150_tot_rhic, v2_music_120_150_tot_rhic]
},
'late_22':{
'music_calcs_short':[pT_music_rhic, v2_music_140_150_22_rhic, v2_music_120_150_22_rhic]
},
'late_brem':{
'music_calcs_short':[pT_music_rhic, v2_music_140_150_brem_rhic, v2_music_120_150_brem_rhic]
},
}


# Hydro LHC
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
'music_calcs_short':[pT_music_lhc, v2_music_140_150_tot_lhc, v2_music_120_150_tot_lhc]
},
'late_22':{
'music_calcs_short':[pT_music_lhc, v2_music_140_150_22_lhc, v2_music_120_150_22_lhc]
},
'late_brem':{
'music_calcs_short':[pT_music_lhc, v2_music_140_150_brem_lhc, v2_music_120_150_brem_lhc]
},
}



common_plotting.load_plotting_style_paper()
plt.figure(figsize=(10*0.8, 4.5*0.8))
gs = gridspec.GridSpec(1,8)

# RHIC:
plt.subplot(gs[: , :4])
plt.xscale('linear')
plt.xlim(0,3)
plt.ylim(-2,22)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'v$_2$ [%]', fontsize = 13)

# MUSIC
plt.plot(plot_dict_rhic['late_22']['music_calcs_short'][0], 100.0 * 0.5 * (plot_dict_rhic['late_22']['music_calcs_short'][1] + plot_dict_rhic['late_22']['music_calcs_short'][2]), color = 'C2' )
plt.plot(plot_dict_rhic['late_brem']['music_calcs_short'][0], 100.0 * 0.5 * (plot_dict_rhic['late_brem']['music_calcs_short'][1] + plot_dict_rhic['late_brem']['music_calcs_short'][2]), color = 'C1' )
plt.plot(plot_dict_rhic['late_tot']['music_calcs_short'][0], 100.0 * 0.5 * (plot_dict_rhic['late_tot']['music_calcs_short'][1] + plot_dict_rhic['late_tot']['music_calcs_short'][2]), color = 'C0' )
plt.fill_between(plot_dict_rhic['late_22']['music_calcs_short'][0], 100.0 * plot_dict_rhic['late_22']['music_calcs_short'][1], 100.0 * plot_dict_rhic['late_22']['music_calcs_short'][2], alpha=0.5, color = 'C2', label = '2$\leftrightarrow$2 Scatterings', lw = 0)
plt.fill_between(plot_dict_rhic['late_brem']['music_calcs_short'][0], 100.0 * plot_dict_rhic['late_brem']['music_calcs_short'][1], 100.0 * plot_dict_rhic['late_brem']['music_calcs_short'][2], alpha=0.5, color = 'C1', label = 'Bremsstrahlung', lw = 0)
plt.fill_between(plot_dict_rhic['late_tot']['music_calcs_short'][0], 100.0 * plot_dict_rhic['late_tot']['music_calcs_short'][1], 100.0 * plot_dict_rhic['late_tot']['music_calcs_short'][2], alpha=0.5, color = 'C0', label = 'Total', lw = 0)


# plt.plot(pT_smash_22_rhic[::3], 100.0*v2_22_rhic[::3], label = '2$\leftrightarrow$2 Scatterings', ls = '--', color = 'C2')
# plt.plot(pT_smash_brem_rhic[::3], 100.0*v2_brem_rhic[::3], label = 'Bremsstrahlung', ls = ':', color = 'C1')
# plt.plot(pT_smash_rhic[::3], 100.0*v2_tot_rhic[::3], ls = '-', label = 'Total', color = 'C0')
# plt.plot(pT_smash_22_rhic[::3], 100.0*v2_22_rhic[::3], label = 'SMASH: 2$\leftrightarrow$2 Scatterings', ls = '--', color = 'C2')
# plt.plot(pT_smash_brem_rhic[::3], 100.0*v2_brem_rhic[::3], label = 'SMASH: Bremsstrahlung', ls = ':', color = 'C0')
# plt.plot(pT_smash_rhic[::3], 100.0*v2_tot_rhic[::3], ls = '-', label = 'SMASH: Total', color = 'C1')
# plt.fill_between(pT_smash_22_rhic[::3], v2_22_rhic[::3] * 100.0 - v2_err_22_rhic[::3] * 100.0, v2_22_rhic[::3] * 100.0 + v2_err_22_rhic[::3] * 100.0, alpha = 0.5, color = 'C2', lw = 0)
# plt.fill_between(pT_smash_brem_rhic[::3], v2_brem_rhic[::3] * 100.0 - v2_err_brem_rhic[::3] * 100.0, v2_brem_rhic[::3] * 100.0 + v2_err_brem_rhic[::3] * 100.0, alpha = 0.5, color = 'C1', lw = 0)
# plt.fill_between(pT_smash_rhic[::3], v2_tot_rhic[::3] * 100.0 - v2_tot_err_rhic[::3] * 100.0, v2_tot_rhic[::3] * 100.0 + v2_tot_err_rhic[::3] * 100.0, alpha = 0.5, color = 'C0', lw = 0)


plt.legend(frameon=False, loc = 'upper left')
plt.figtext(0.235, 0.205, '     Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')
plt.xticks([0,1,2,3])



# LHC
plt.subplot(gs[: , 4:])
plt.xscale('linear')
plt.xlim(0,3)
plt.ylim(-2,22)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.yticks([])
plt.minorticks_off()

# SMASH
# plt.plot(pT_smash_22_lhc[::3], 100.0*v2_22_lhc[::3], label = 'SMASH: 2to2', ls = '--', color = 'C2')
# plt.plot(pT_smash_brem_lhc[::3], 100.0*v2_brem_lhc[::3], label = 'SMASH: Brems', ls = ':', color = 'C1')
# plt.plot(pT_smash_lhc[::3], 100.0*v2_tot_lhc[::3], ls = '-', label = 'SMASH: Tot', color = 'C0')
# plt.fill_between(pT_smash_22_lhc[::3], v2_22_lhc[::3] * 100.0 - v2_err_22_lhc[::3] * 100.0, v2_22_lhc[::3] * 100.0 + v2_err_22_lhc[::3] * 100.0, alpha = 0.5, color = 'C2', lw = 0)
# plt.fill_between(pT_smash_brem_lhc[::3], v2_brem_lhc[::3] * 100.0 - v2_err_brem_lhc[::3] * 100.0, v2_brem_lhc[::3] * 100.0 + v2_err_brem_lhc[::3] * 100.0, alpha = 0.5, color = 'C1', lw = 0)
# plt.fill_between(pT_smash_lhc[::3], v2_tot_lhc[::3] * 100.0 - v2_tot_err_lhc[::3] * 100.0, v2_tot_lhc[::3] * 100.0 + v2_tot_err_lhc[::3] * 100.0, alpha = 0.5, color = 'C0', lw = 0)
plt.plot(plot_dict_lhc['late_22']['music_calcs_short'][0], 100.0 * 0.5 * (plot_dict_lhc['late_22']['music_calcs_short'][1] + plot_dict_lhc['late_22']['music_calcs_short'][2]), color = 'C2' )
plt.plot(plot_dict_lhc['late_brem']['music_calcs_short'][0], 100.0 * 0.5 * (plot_dict_lhc['late_brem']['music_calcs_short'][1] + plot_dict_lhc['late_brem']['music_calcs_short'][2]), color = 'C1' )
plt.plot(plot_dict_lhc['late_tot']['music_calcs_short'][0], 100.0 * 0.5 * (plot_dict_lhc['late_tot']['music_calcs_short'][1] + plot_dict_lhc['late_tot']['music_calcs_short'][2]), color = 'C0' )
plt.fill_between(plot_dict_lhc['late_22']['music_calcs_short'][0], 100.0 * plot_dict_lhc['late_22']['music_calcs_short'][1], 100.0 * plot_dict_lhc['late_22']['music_calcs_short'][2], alpha=0.5, color = 'C2', label = '2$\leftrightarrow$2 Scatterings', lw = 0)
plt.fill_between(plot_dict_lhc['late_brem']['music_calcs_short'][0], 100.0 * plot_dict_lhc['late_brem']['music_calcs_short'][1], 100.0 * plot_dict_lhc['late_brem']['music_calcs_short'][2], alpha=0.5, color = 'C1', label = 'Bremsstrahlung', lw = 0)
plt.fill_between(plot_dict_lhc['late_tot']['music_calcs_short'][0], 100.0 * plot_dict_lhc['late_tot']['music_calcs_short'][1], 100.0 * plot_dict_lhc['late_tot']['music_calcs_short'][2], alpha=0.5, color = 'C0', label = 'Total', lw = 0)



# plt.legend(frameon=False, loc = 'upper left')
plt.figtext(0.68, 0.205, '      Pb + Pb\n' + r' $\mathbf{\sqrt{s}}$ = 2.76 TeV', fontweight = 'bold')
plt.xticks([0,1,2,3])

plt.legend(frameon=False, loc = 'upper left')
plt.figtext(0.862, 0.965, "SMASH-2.0.1-1-g397f8f0", color = "gray", fontsize = 5.3)
plt.tight_layout(w_pad=-0.05)
plt.savefig("v2_MUSIC.pdf")
plt.close()
