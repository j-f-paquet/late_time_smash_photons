import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as mtick
import os.path
import scipy.interpolate
import seaborn as sns
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting
import matplotlib.gridspec as gridspec


######################################
############ Total rate ##############
######################################
# RHIC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_above_rhic, dN_music_above_rhic, v1_above_rhic, v2_above_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/combined/average_sp_smash_tot.dat")
pT_above_plus_smash_rhic, dN_music_above_plus_smash_rhic, v1_music_above_plus_smash_rhic, v2_music_above_plus_smash_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140_rhic, dN_music_above_plus_hydro140_rhic, v1_music_above_plus_hydro140_rhic, v2_music_above_plus_hydro140_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120_rhic, dN_music_above_plus_hydro120_rhic, v1_music_above_plus_hydro120_rhic, v2_music_above_plus_hydro120_rhic, *rest = raw.T

# Interpolation for ratio RHIC
music_above_interpolation_rhic = scipy.interpolate.interp1d(pT_above_rhic, v2_above_rhic, kind='linear')
music_above_rebin_smash_rhic = music_above_interpolation_rhic(pT_above_plus_smash_rhic[1:14])
music_above_rebin_music140_rhic = music_above_interpolation_rhic(pT_above_plus_hydro140_rhic[:14])
music_above_rebin_music120_rhic = music_above_interpolation_rhic(pT_above_plus_hydro120_rhic[:14])



# LHC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/photons_above_Tfr_nx200/PbPb2760/C10-20/average_sp.dat")
pT_above_lhc, dN_music_above_lhc, v1_above_lhc, v2_above_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_smash_tot.dat")
pT_above_plus_smash_lhc, dN_music_above_plus_smash_lhc, v1_music_above_plus_smash_lhc, v2_music_above_plus_smash_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140_lhc, dN_music_above_plus_hydro140_lhc, v1_music_above_plus_hydro140_lhc, v2_music_above_plus_hydro140_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120_lhc, dN_music_above_plus_hydro120_lhc, v1_music_above_plus_hydro120_lhc, v2_music_above_plus_hydro120_lhc, *rest = raw.T


# Interpolation for ratio RHIC
music_above_interpolation_lhc = scipy.interpolate.interp1d(pT_above_lhc, v2_above_lhc, kind='linear')
music_above_rebin_smash_lhc = music_above_interpolation_lhc(pT_above_plus_smash_lhc[1:14])
music_above_rebin_music140_lhc = music_above_interpolation_lhc(pT_above_plus_hydro140_lhc[:14])
music_above_rebin_music120_lhc = music_above_interpolation_lhc(pT_above_plus_hydro120_lhc[:14])


####################################
# Ration plot 120 < T < 150
####################################

gs = gridspec.GridSpec(10,10)

common_plotting.load_plotting_style_paper()
plt.subplot(gs[:6 , :5])

# RHIC
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,2.6)
plt.ylim(0.0,2.5)
#plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')
plt.yticks([0.0, 0.5, 1, 1.5, 2, 2.5])
plt.xticks([])

# SMASH
plt.plot(pT_above_rhic, 100.0 * v2_above_rhic, label=r"MUSIC$_\mathsf{T > 150 \ MeV}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash_rhic, 100.0 * v2_music_above_plus_smash_rhic, ls = '--', label='MUSIC$_\mathsf{T > 150 \ MeV}$ + ' + 'SMASH', color = 'C2')
# MUSIC
plt.fill_between(pT_above_plus_hydro140_rhic,  100.0 * v2_music_above_plus_hydro140_rhic,  100.0 * v2_music_above_plus_hydro120_rhic, color='C0', label = 'MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$', lw = 0)
plt.legend(frameon = False, loc = 'upper left')
#plt.figtext(0.365, 0.17, '         Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')

plt.subplot(gs[6:, :5])
plt.xlim(0,2.6)
plt.ylim(0.5, 2.0)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')

#plt.plot(pT_above_plus_smash_rhic[1:14], v2_music_above_plus_smash_rhic[1:14] / music_above_rebin_smash_rhic, label = '(MUSIC$_\mathsf{T > 150 \ MeV}$ + SMASH) / MUSIC$_\mathsf{T > 150 \ MeV}$', ls = '--', color = 'C2')
plt.plot(pT_above_plus_smash_rhic[1:14], v2_music_above_plus_smash_rhic[1:14] / (0.5*(v2_music_above_plus_hydro140_rhic[1:14] + v2_music_above_plus_hydro120_rhic[1:14])), label = 'Mean: (MUSIC$_\mathsf{T > 150 \ MeV}$ + SMASH) / (MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$)', ls = '--', color = 'C2')
# plt.axhline(1.0, ls = ':', color = 'C1')
plt.axhline(1.0, ls = '-', color = 'grey', zorder = 0)
#plt.fill_between(pT_above_plus_hydro120_rhic[:14], v2_music_above_plus_hydro140_rhic[:14] / music_above_rebin_music140_rhic, v2_music_above_plus_hydro120_rhic[:14] / music_above_rebin_music120_rhic, label = '(MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$) / MUSIC$_\mathsf{T > 150 \ MeV}$', alpha = 1.0, color = 'C0', lw = 0)
plt.fill_between(pT_above_plus_smash_rhic[1:14], v2_music_above_plus_smash_rhic[1:14]/ v2_music_above_plus_hydro140_rhic[1:14], v2_music_above_plus_smash_rhic[1:14]/ v2_music_above_plus_hydro120_rhic[1:14], label = 'Range: (MUSIC$_\mathsf{T > 150 \ MeV}$ + SMASH) / (MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$)', alpha = 0.5, color = 'C2', lw = 0)

plt.legend(frameon=False, fontsize = 5.5)
#plt.figtext(0.135, 0.5, 'Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')
plt.yticks([0.5, 1.0, 1.5, 2.0])


# LHC
plt.subplot(gs[:6 , 5:])
# plt.xscale('linear')
# plt.yscale('linear')
plt.xlim(0,2.6)
plt.ylim(0,5)
# plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
# # plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')
plt.yticks([1.5, 2.5, 3.5, 4.5, 5.5])
# plt.yticks([0.0,1.5,2.5,3.5,4.5])
plt.yticks([0,1,2,3,4,5])
plt.xticks([])

# SMASH
plt.plot(pT_above_lhc, 100.0 * v2_above_lhc, label=r"MUSIC$_\mathsf{T > 150 \ MeV}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash_lhc, 100.0 * v2_music_above_plus_smash_lhc, ls = '--', label='MUSIC$_\mathsf{T > 150 \ MeV}$ + ' + 'SMASH', color = 'C2')
# MUSIC
plt.fill_between(pT_above_plus_hydro140_lhc,  100.0 * v2_music_above_plus_hydro140_lhc,  100.0 * v2_music_above_plus_hydro120_lhc, color='C0', label = 'MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$', lw = 0)
plt.legend(frameon = False, loc = 'upper left')
#plt.figtext(0.82, 0.17, '           Pb + Pb\n' + r' $\mathbf{\sqrt{s}}$ = 2.76 TeV', fontweight = 'bold')


plt.subplot(gs[6:, 5:])
plt.xlim(0,2.6)
plt.ylim(0.5, 2.0)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')


#plt.plot(pT_above_plus_smash_lhc[1:14], v2_music_above_plus_smash_lhc[1:14] / music_above_rebin_smash_lhc, label = '(MUSIC$_\mathsf{T > 150 \ MeV}$ + SMASH) / MUSIC$_\mathsf{T > 150 \ MeV}$', ls = '--', color = 'C2')
plt.plot(pT_above_plus_smash_lhc[1:14], v2_music_above_plus_smash_lhc[1:14] / (0.5*(v2_music_above_plus_hydro140_lhc[1:14] + v2_music_above_plus_hydro120_lhc[1:14])), label = 'Mean: (MUSIC$_\mathsf{T > 150 \ MeV}$ + SMASH) / (MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$)', ls = '--', color = 'C2')
# plt.axhline(1.0, ls = ':', color = 'C1')
plt.axhline(1.0, ls = '-', color = 'grey', zorder = 0)
#plt.fill_between(pT_above_plus_hydro120_lhc[:14], v2_music_above_plus_hydro140_lhc[:14] / music_above_rebin_music140_lhc, v2_music_above_plus_hydro120_lhc[:14] / music_above_rebin_music120_lhc, label = '(MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$) / MUSIC$_\mathsf{T > 150 \ MeV}$', alpha = 1.0, color = 'C0', lw = 0)
plt.fill_between(pT_above_plus_smash_lhc[1:14], v2_music_above_plus_smash_lhc[1:14] / v2_music_above_plus_hydro140_lhc[1:14], v2_music_above_plus_smash_lhc[1:14] / v2_music_above_plus_hydro120_lhc[1:14], label = 'Range: (MUSIC$_\mathsf{T > 150 \ MeV}$ + SMASH) / (MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$)', alpha = 0.5, color = 'C2', lw = 0)

plt.legend(frameon=False, fontsize = 5.5)
#plt.figtext(0.135, 0.5, 'Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')
plt.yticks([])

#plt.figtext(0.9, 0.962, "SMASH-2.0.1-1-g397f8f0",color = "gray", fontsize = 5.3)
#plt.tight_layout()
plt.tight_layout(w_pad=+0.2, h_pad=-0.1)
# plt.tight_layout(w_pad=-6.4, h_pad=-0.5)
plt.savefig("v2_sum_ratio.pdf")
plt.close()

print (max(v2_music_above_plus_smash_rhic[1:14] / v2_music_above_plus_hydro140_rhic[1:14]))
print (max(v2_music_above_plus_smash_lhc[1:14] / v2_music_above_plus_hydro140_lhc[1:14]))
