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

######################################
############ Total rate ##############
######################################

# SMASH RHIC
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1/pT_photons_midy.txt")
pT_smash_rhic, pre_dN_22_rhic, pre_dN_22_err_rhic, pre_dN_brem_rhic, pre_dN_brem_err_rhic = raw.T
dN_22_rhic=pre_dN_22_rhic/(2*np.pi*pT_smash_rhic)
dN_22_err_rhic=pre_dN_22_err_rhic/(2*np.pi*pT_smash_rhic)
dN_brem_rhic=pre_dN_brem_rhic/(2*np.pi*pT_smash_rhic)
dN_brem_err_rhic=pre_dN_brem_err_rhic/(2*np.pi*pT_smash_rhic)

# MUSIC RHIC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/22_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_140_150_22_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_140_150_brem_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/22_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_120_150_22_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_120_150_brem_rhic, *rest = raw.T


# SMASH LHC
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1/pT_photons_midy.txt")
pT_smash_lhc, pre_dN_22_lhc, pre_dN_22_err_lhc, pre_dN_brem_lhc, pre_dN_brem_err_lhc = raw.T
dN_22_lhc=pre_dN_22_lhc/(2*np.pi*pT_smash_lhc)
dN_22_err_lhc=pre_dN_22_err_lhc/(2*np.pi*pT_smash_lhc)
dN_brem_lhc=pre_dN_brem_lhc/(2*np.pi*pT_smash_lhc)
dN_brem_err_lhc=pre_dN_brem_err_lhc/(2*np.pi*pT_smash_lhc)

# MUSIC LHC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/22_photons_T140-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_140_150_22_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/brem_photons_T140-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_140_150_brem_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/22_photons_T120-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_120_150_22_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/brem_photons_T120-150_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_120_150_brem_lhc, *rest = raw.T



##############################
# with bands, short range
##############################

common_plotting.load_plotting_style_paper()
plt.figure(figsize=(10*0.8, 4.5*0.8))
gs = gridspec.GridSpec(1,9)

# RHIC:
plt.subplot(gs[: , 1:5])
plt.xscale('linear')
plt.xlim(0,4)
plt.ylim(0,1.08)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'Fraction of late-stage photons' + '\n' + 'from 2$\leftrightarrow$2 scatterings', fontsize = 13)
# plt.ylabel(r'Fraction of photons from 2$\leftrightarrow$2 scatterings')
# plt.ylabel(r'$\frac{\mathsf{dN}_\gamma^{2\leftrightarrow2}/\mathsf{d}p_\mathrm{T} |_{\mathsf{y} =0}}{\mathsf{dN}_\gamma^{2\leftrightarrow2}/\mathsf{d}p_\mathrm{T} |_{\mathsf{y} =0} \ + \ \mathsf{dN}_\gamma^{\mathsf{Brems}}/\mathsf{d}p_\mathrm{T} |_{\mathsf{y} =0}}$')
# SMASH
plt.plot(pT_smash_rhic[::3], dN_22_rhic[::3] / (dN_22_rhic[::3] + dN_brem_rhic[::3]), ls = '-', label = 'SMASH', color = 'C2')
plt.fill_between(pT_smash_rhic[::3], dN_22_rhic[::3] / (dN_22_rhic[::3] + dN_brem_rhic[::3]) - np.sqrt(dN_brem_rhic[::3]**2 * dN_22_err_rhic[::3]**2 + dN_22_rhic[::3]**2 * dN_brem_err_rhic[::3]**2) / (dN_22_rhic[::3] + dN_brem_rhic[::3])**2, dN_22_rhic[::3] / (dN_22_rhic[::3] + dN_brem_rhic[::3]) + np.sqrt(dN_brem_rhic[::3]**2 * dN_22_err_rhic[::3]**2 + dN_22_rhic[::3]**2 * dN_brem_err_rhic[::3]**2) / (dN_22_rhic[::3] + dN_brem_rhic[::3])**2, alpha = 0.5 , color = 'C2', lw = 0)
# MUSIC: 120 MeV < T 150 MeV
plt.fill_between(pT_music_rhic, dN_music_140_150_22_rhic / (dN_music_140_150_22_rhic + dN_music_140_150_brem_rhic), dN_music_120_150_22_rhic / (dN_music_120_150_22_rhic + dN_music_120_150_brem_rhic) , color = 'C0', alpha=1.0, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$', lw = 0)

plt.legend(frameon=False, loc = 'upper left')
plt.figtext(0.405, 0.205, '         Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')
plt.xticks([0,1,2,3,4])

# LHC
plt.subplot(gs[: , 5:])
plt.xscale('linear')
plt.xlim(0,4)
plt.ylim(0,1.08)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.yticks([])
plt.minorticks_off()

# SMASH
plt.plot(pT_smash_lhc[::3], dN_22_lhc[::3] / (dN_22_lhc[::3] + dN_brem_lhc[::3]), ls = '-', label = 'SMASH', color = 'C2')
plt.fill_between(pT_smash_lhc[::3], dN_22_lhc[::3] / (dN_22_lhc[::3] + dN_brem_lhc[::3]) - np.sqrt(dN_brem_lhc[::3]**2 * dN_22_err_lhc[::3]**2 + dN_22_lhc[::3]**2 * dN_brem_err_lhc[::3]**2) / (dN_22_lhc[::3] + dN_brem_lhc[::3])**2, dN_22_lhc[::3] / (dN_22_lhc[::3] + dN_brem_lhc[::3]) + np.sqrt(dN_brem_lhc[::3]**2 * dN_22_err_lhc[::3]**2 + dN_22_lhc[::3]**2 * dN_brem_err_lhc[::3]**2) / (dN_22_lhc[::3] + dN_brem_lhc[::3])**2, alpha = 0.5 , color = 'C2', lw = 0)
# MUSIC
plt.fill_between(pT_music_lhc, dN_music_140_150_22_lhc / (dN_music_140_150_22_lhc + dN_music_140_150_brem_lhc), dN_music_120_150_22_lhc / (dN_music_120_150_22_lhc + dN_music_120_150_brem_lhc) , color = 'C0', alpha=1.0, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$', lw = 0)

plt.legend(frameon=False, loc = 'upper left')
plt.figtext(0.827, 0.205, '           Pb + Pb\n' + r' $\mathbf{\sqrt{s}}$ = 2.76 TeV', fontweight = 'bold')
plt.xticks([0,1,2,3,4])

plt.figtext(0.917, 0.965, "SMASH-2.0.1", color = "gray", fontsize = 5.3)
plt.tight_layout(w_pad=-5.3)
plt.savefig("ratio_spectra.pdf")
plt.close()
