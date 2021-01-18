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
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/pT_photons_midy.txt")
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
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/low_stats/pT_photons_midy.txt")
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
gs = gridspec.GridSpec(1,11)

# RHIC:
plt.subplot(gs[: , 1:6])
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-5,1e1)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]')

# SMASH
plt.plot(pT_smash_rhic[::3], dN_22_rhic[::3], ls = '-', label = r'SMASH: 2$\leftrightarrow$2 Scatterings', color = 'C0')
plt.plot(pT_smash_rhic[::3], dN_brem_rhic[::3], ls = '--', label = 'SMASH: Bremsstrahlung', color = 'C1')
plt.fill_between(pT_smash_rhic[::3], dN_22_rhic[::3] - dN_22_err_rhic[::3], dN_22_rhic[::3] + dN_22_err_rhic[::3], color = 'C1', alpha = 0.5, lw = 0)
plt.fill_between(pT_smash_rhic[::3], dN_brem_rhic[::3] - dN_brem_err_rhic[::3], dN_brem_rhic[::3] + dN_brem_err_rhic[::3], color = 'C1', alpha = 0.5, lw = 0)

# short range: 120 MeV < T 150 MeV
plt.fill_between(pT_music_rhic, dN_music_140_150_22_rhic, dN_music_120_150_22_rhic, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings', lw = 0)
plt.fill_between(pT_music_rhic, dN_music_140_150_brem_rhic, dN_music_120_150_brem_rhic , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung', lw = 0)
# plt.fill_between(pT_music_rhic, dN_music_140_150_22_rhic, dN_music_120_150_22_rhic, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings\n' + '120 MeV < T < 150 MeV', lw = 0)
# plt.fill_between(pT_music_rhic, dN_music_140_150_brem_rhic, dN_music_120_150_brem_rhic , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung \n' + '120 MeV < T < 150 MeV', lw = 0)

# MUSIC QGP
plt.plot(pT_music_rhic, dN_music_above_Tfr_rhic, label=r"MUSIC$_\mathsf{QGP}$", color='C2', ls = ':')

plt.legend(frameon=False)
plt.figtext(0.115, 0.19, 'Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')
# plt.figtext(0.12, 0.19, '      Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200.0 GeV', fontweight = 'bold')

# LHC
plt.subplot(gs[: , 6:])
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-5,1e1)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.yticks([])
plt.minorticks_off()
# plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]')

# SMASH
plt.plot(pT_smash_lhc[::3], dN_22_lhc[::3], ls = '-', label = r'SMASH: 2$\leftrightarrow$2 Scatterings', color = 'C0')
plt.plot(pT_smash_lhc[::3], dN_brem_lhc[::3], ls = '--', label = 'SMASH: Bremsstrahlung', color = 'C1')
plt.fill_between(pT_smash_lhc[::3], dN_22_lhc[::3] - dN_22_err_lhc[::3], dN_22_lhc[::3] + dN_22_err_lhc[::3], color = 'C1', alpha = 0.5, lw = 0)
plt.fill_between(pT_smash_lhc[::3], dN_brem_lhc[::3] - dN_brem_err_lhc[::3], dN_brem_lhc[::3] + dN_brem_err_lhc[::3], color = 'C1', alpha = 0.5, lw = 0)

# short range: 120 MeV < T 150 MeV
plt.fill_between(pT_music_lhc, dN_music_140_150_22_lhc, dN_music_120_150_22_lhc, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings', lw = 0)
plt.fill_between(pT_music_lhc, dN_music_140_150_brem_lhc, dN_music_120_150_brem_lhc , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung', lw = 0)
# plt.fill_between(pT_music_lhc, dN_music_140_150_22_lhc, dN_music_120_150_22_lhc, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings\n' + '120 MeV < T < 150 MeV', lw = 0)
# plt.fill_between(pT_music_lhc, dN_music_140_150_brem_lhc, dN_music_120_150_brem_lhc , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung \n' + '120 MeV < T < 150 MeV', lw = 0)

# MUSIC QGP
plt.plot(pT_music_lhc, dN_music_above_Tfr_lhc, label=r"MUSIC$_\mathsf{QGP}$", color='C2', ls = ':')


plt.legend(frameon=False)
plt.figtext(0.56, 0.19, 'Pb + Pb\n' + r'$\mathbf{\sqrt{s}}$ = 2760 GeV', fontweight = 'bold')
# plt.figtext(0.57, 0.19, '       Pb + Pb\n' + r'$\mathbf{\sqrt{s}}$ = 2760.0 GeV', fontweight = 'bold')


plt.tight_layout(w_pad=-5.0)
plt.savefig("spectra.pdf")
plt.close()
