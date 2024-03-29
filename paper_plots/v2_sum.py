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

# LHC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/photons_above_Tfr_nx200/PbPb2760/C10-20/average_sp.dat")
pT_above_lhc, dN_music_above_lhc, v1_above_lhc, v2_above_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_smash_tot.dat")
pT_above_plus_smash_lhc, dN_music_above_plus_smash_lhc, v1_music_above_plus_smash_lhc, v2_music_above_plus_smash_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140_lhc, dN_music_above_plus_hydro140_lhc, v1_music_above_plus_hydro140_lhc, v2_music_above_plus_hydro140_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120_lhc, dN_music_above_plus_hydro120_lhc, v1_music_above_plus_hydro120_lhc, v2_music_above_plus_hydro120_lhc, *rest = raw.T





gs = gridspec.GridSpec(10,12)

common_plotting.load_plotting_style_paper()

plt.figure()
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 10*0.8, 5.3*0.8
# RHIC
plt.subplot(gs[: , 1:6])
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,2.6)
plt.ylim(0.0,2.5)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')
plt.yticks([0.0, 0.5, 1, 1.5, 2, 2.5])

# SMASH
plt.plot(pT_above_rhic, 100.0 * v2_above_rhic, label=r"MUSIC$_\mathsf{T > 150 \ MeV}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash_rhic, 100.0 * v2_music_above_plus_smash_rhic, ls = '--', label='MUSIC$_\mathsf{T > 150 \ MeV}$ + ' + 'SMASH', color = 'C2')
# MUSIC
plt.fill_between(pT_above_plus_hydro140_rhic,  100.0 * v2_music_above_plus_hydro140_rhic,  100.0 * v2_music_above_plus_hydro120_rhic, color='C0', label = 'MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$', lw = 0)
plt.legend(frameon = False, loc = 'upper left')
plt.figtext(0.365, 0.17, '         Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')

# LHC
plt.subplot(gs[: , 7:])
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,2.6)
plt.ylim(0.0,5.0)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
# plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')
plt.yticks([0.0,1.0, 2.0, 3.0, 4.0, 5.0])
# plt.yticks([0.0,1.5,2.5,3.5,4.5])

# SMASH
plt.plot(pT_above_lhc, 100.0 * v2_above_lhc, label=r"MUSIC$_\mathsf{T > 150 \ MeV}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash_lhc, 100.0 * v2_music_above_plus_smash_lhc, ls = '--', label='MUSIC$_\mathsf{T > 150 \ MeV}$ + ' + 'SMASH', color = 'C2')
# MUSIC
plt.fill_between(pT_above_plus_hydro140_lhc,  100.0 * v2_music_above_plus_hydro140_lhc,  100.0 * v2_music_above_plus_hydro120_lhc, color='C0', label = 'MUSIC$_\mathsf{T > 150 \ MeV}$ + MUSIC$_\mathsf{T \leq 150 \ MeV}$', lw = 0)
plt.legend(frameon = False, loc = 'upper left')
plt.figtext(0.82, 0.17, '           Pb + Pb\n' + r' $\mathbf{\sqrt{s}}$ = 2.76 TeV', fontweight = 'bold')

plt.figtext(0.857, 0.962, "SMASH-2.0.1-1-g397f8f0",color = "gray", fontsize = 5.3)
plt.tight_layout(w_pad=-6.4, h_pad=-0.5)
plt.savefig("v2_sum.pdf")
plt.close()
