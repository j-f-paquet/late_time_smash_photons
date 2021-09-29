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
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/pT_photons_midy.txt")
pT_smash_rhic, pre_dN_22_rhic, pre_dN_22_err_rhic, pre_dN_brem_rhic, pre_dN_brem_err_rhic = raw.T
dN_22_rhic=pre_dN_22_rhic/(2*np.pi*pT_smash_rhic)
dN_22_err_rhic=pre_dN_22_err_rhic/(2*np.pi*pT_smash_rhic)
dN_brem_rhic=pre_dN_brem_rhic/(2*np.pi*pT_smash_rhic)
dN_brem_err_rhic=pre_dN_brem_err_rhic/(2*np.pi*pT_smash_rhic)

# MUSIC RHIC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_above_Tfr_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/22_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_140_150_22_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_140_150_brem_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/22_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_120_150_22_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/results/brem_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music_rhic, dN_music_120_150_brem_rhic, *rest = raw.T


# SMASH LHC
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/pT_photons_midy.txt")
pT_smash_lhc, pre_dN_22_lhc, pre_dN_22_err_lhc, pre_dN_brem_lhc, pre_dN_brem_err_lhc = raw.T
dN_22_lhc=pre_dN_22_lhc/(2*np.pi*pT_smash_lhc)
dN_22_err_lhc=pre_dN_22_err_lhc/(2*np.pi*pT_smash_lhc)
dN_brem_lhc=pre_dN_brem_lhc/(2*np.pi*pT_smash_lhc)
dN_brem_err_lhc=pre_dN_brem_err_lhc/(2*np.pi*pT_smash_lhc)

# MUSIC LHC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/photons_above_Tfr_nx200/PbPb2760/C10-20/average_sp.dat")
pT_music_lhc, dN_music_above_Tfr_lhc, *rest = raw.T

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
plt.figure()
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 10*0.8, 5.3*0.8
gs = gridspec.GridSpec(1,9)

# RHIC:
plt.subplot(gs[: , 1:5])
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-7,1e1)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'$\frac{1}{2 \pi \mathrm{p_T}} \frac{\mathrm{d^2N}}{\mathrm{dp_T d_y}}$|$_{\mathrm{y=0}}$ [Gev$^{-2}$]')
# plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]')

# SMASH
# plt.plot(pT_smash_rhic[::3], dN_22_rhic[::3], ls = '-', label = r'SMASH: 2$\leftrightarrow$2 Scatterings', color = 'C0')
# plt.plot(pT_smash_rhic[::3], dN_brem_rhic[::3], ls = '--', label = 'SMASH: Bremsstrahlung', color = 'C1')
plt.plot(pT_smash_rhic[::3], dN_22_rhic[::3] + dN_brem_rhic[::3], ls = '-', label = 'SMASH', color = 'C2')
# plt.fill_between(pT_smash_rhic[::3], dN_22_rhic[::3] - dN_22_err_rhic[::3], dN_22_rhic[::3] + dN_22_err_rhic[::3], color = 'C1', alpha = 0.5, lw = 0)
# plt.fill_between(pT_smash_rhic[::3], dN_brem_rhic[::3] - dN_brem_err_rhic[::3], dN_brem_rhic[::3] + dN_brem_err_rhic[::3], color = 'C1', alpha = 0.5, lw = 0)
plt.fill_between(pT_smash_rhic[::3], dN_22_rhic[::3] + dN_brem_rhic[::3] - np.sqrt(dN_22_err_rhic[::3]**2 + dN_brem_err_rhic[::3]**2), dN_22_rhic[::3] + dN_brem_rhic[::3] + np.sqrt(dN_22_err_rhic[::3]**2 + dN_brem_err_rhic[::3]**2), alpha = 0.5 , color = 'C2')

# short range: 120 MeV < T 150 MeV
# plt.fill_between(pT_music_rhic, dN_music_140_150_22_rhic, dN_music_120_150_22_rhic, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$: 2$\leftrightarrow$2 Scatterings', lw = 0)
# plt.fill_between(pT_music_rhic, dN_music_140_150_brem_rhic, dN_music_120_150_brem_rhic , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$: Bremsstrahlung', lw = 0)
plt.fill_between(pT_music_rhic, dN_music_140_150_22_rhic + dN_music_140_150_brem_rhic, dN_music_120_150_22_rhic + dN_music_120_150_brem_rhic , color = 'C0', alpha=1.0, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$: Total', lw = 0)
# plt.fill_between(pT_music_rhic, dN_music_140_150_22_rhic, dN_music_120_150_22_rhic, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings\n' + '120 MeV < T < 150 MeV', lw = 0)
# plt.fill_between(pT_music_rhic, dN_music_140_150_brem_rhic, dN_music_120_150_brem_rhic , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung \n' + '120 MeV < T < 150 MeV', lw = 0)

# MUSIC QGP
plt.plot(pT_music_rhic, dN_music_above_Tfr_rhic, label=r"MUSIC$_\mathsf{T > 150 \ MeV}$", color='C1', ls = ':')
plt.xticks([0,1,2,3,4])

plt.legend(frameon=False)
plt.figtext(0.135, 0.16, 'Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')
# plt.figtext(0.12, 0.19, '      Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200.0 GeV', fontweight = 'bold')

# LHC
plt.subplot(gs[: , 5:])
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-7,1e1)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.yticks([])
plt.minorticks_off()
# plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]')

# SMASH
# plt.plot(pT_smash_lhc[::3], dN_22_lhc[::3], ls = '-', label = r'SMASH: 2$\leftrightarrow$2 Scatterings', color = 'C0')
# plt.plot(pT_smash_lhc[::3], dN_brem_lhc[::3], ls = '--', label = 'SMASH: Bremsstrahlung', color = 'C1')
plt.plot(pT_smash_lhc[::3], dN_22_lhc[::3] + dN_brem_lhc[::3], ls = '-', label = 'SMASH', color = 'C2')
# plt.fill_between(pT_smash_lhc[::3], dN_22_lhc[::3] - dN_22_err_lhc[::3], dN_22_lhc[::3] + dN_22_err_lhc[::3], color = 'C1', alpha = 0.5, lw = 0)
# plt.fill_between(pT_smash_lhc[::3], dN_brem_lhc[::3] - dN_brem_err_lhc[::3], dN_brem_lhc[::3] + dN_brem_err_lhc[::3], color = 'C1', alpha = 0.5, lw = 0)
plt.fill_between(pT_smash_lhc[::3], dN_22_lhc[::3] + dN_brem_lhc[::3] - np.sqrt(dN_22_err_lhc[::3]**2 + dN_brem_err_lhc[::3]**2), dN_22_lhc[::3] + dN_brem_lhc[::3] + np.sqrt(dN_22_err_lhc[::3]**2 + dN_brem_err_lhc[::3]**2), alpha = 0.5 , color = 'C2')


# short range: 120 MeV < T 150 MeV
# plt.fill_between(pT_music_lhc, dN_music_140_150_22_lhc, dN_music_120_150_22_lhc, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$: 2$\leftrightarrow$2 Scatterings', lw = 0)
# plt.fill_between(pT_music_lhc, dN_music_140_150_brem_lhc, dN_music_120_150_brem_lhc , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$: Bremsstrahlung', lw = 0)
plt.fill_between(pT_music_lhc, dN_music_140_150_22_lhc + dN_music_140_150_brem_lhc, dN_music_120_150_22_lhc + dN_music_120_150_brem_lhc , color = 'C0', alpha=1.0, label='MUSIC$_\mathsf{T \leq 150 \ MeV}$', lw = 0)
# plt.fill_between(pT_music_lhc, dN_music_140_150_22_lhc, dN_music_120_150_22_lhc, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings\n' + '120 MeV < T < 150 MeV', lw = 0)
# plt.fill_between(pT_music_lhc, dN_music_140_150_brem_lhc, dN_music_120_150_brem_lhc , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung \n' + '120 MeV < T < 150 MeV', lw = 0)

# MUSIC QGP
plt.plot(pT_music_lhc, dN_music_above_Tfr_lhc, label=r"MUSIC$_\mathsf{T > 150 \ MeV}$", color='C1', ls = ':')


plt.legend(frameon=False)
plt.figtext(0.57, 0.16, 'Pb + Pb\n' + r'$\mathbf{\sqrt{s}}$ = 2.76 TeV', fontweight = 'bold')
plt.xticks([0,1,2,3,4])
# plt.figtext(0.57, 0.19, '       Pb + Pb\n' + r'$\mathbf{\sqrt{s}}$ = 2760.0 GeV', fontweight = 'bold')

plt.figtext(0.862, 0.96, "SMASH-2.0.1-1-g397f8f0",color = "gray", fontsize = 5.3)
plt.tight_layout(w_pad=-5.5)
plt.savefig("spectra.pdf")
plt.close()
