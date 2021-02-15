import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as mtick
import os.path
import scipy.interpolate
import matplotlib.gridspec as gridspec
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting

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
pT_above_rhic, dN_music_above_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/combined/average_sp_smash_tot.dat")
pT_above_plus_smash_rhic, dN_music_above_plus_smash_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140_rhic, dN_music_above_plus_hydro140_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120_rhic, dN_music_above_plus_hydro120_rhic, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/AuAu200/combined/average_sp_hydro_tot_T100-150.dat")
pT_above_plus_hydro100_rhic, dN_music_above_plus_hydro100_rhic, *rest = raw.T


# Interpolation for ratio RHIC
music_above_interpolation_rhic = scipy.interpolate.interp1d(pT_above_rhic, np.log(dN_music_above_rhic), kind='linear')
music_above_rebin_smash_rhic = np.exp(music_above_interpolation_rhic(pT_above_plus_smash_rhic[1:14]))
music_above_rebin_music140_rhic = np.exp(music_above_interpolation_rhic(pT_above_plus_hydro140_rhic[:14]))
music_above_rebin_music120_rhic = np.exp(music_above_interpolation_rhic(pT_above_plus_hydro120_rhic[:14]))


# SMASH LHC
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/low_stats/pT_photons_midy.txt")
pT_smash_lhc, pre_dN_22_lhc, pre_dN_22_err_lhc, pre_dN_brem_lhc, pre_dN_brem_err_lhc = raw.T
dN_22_lhc=pre_dN_22_lhc/(2*np.pi*pT_smash_lhc)
dN_22_err_lhc=pre_dN_22_err_lhc/(2*np.pi*pT_smash_lhc)
dN_brem_lhc=pre_dN_brem_lhc/(2*np.pi*pT_smash_lhc)
dN_brem_err_lhc=pre_dN_brem_err_lhc/(2*np.pi*pT_smash_lhc)

# MUSIC LHC
raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/results/photons_above_Tfr_nx200/PbPb2760/C10-20/average_sp.dat")
pT_above_lhc, dN_music_above_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_smash_tot.dat")
pT_above_plus_smash_lhc, dN_music_above_plus_smash_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140_lhc, dN_music_above_plus_hydro140_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120_lhc, dN_music_above_plus_hydro120_lhc, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T100-150.dat")
pT_above_plus_hydro100_lhc, dN_music_above_plus_hydro100_lhc, *rest = raw.T


# Interpolation for ratio RHIC
music_above_interpolation_lhc = scipy.interpolate.interp1d(pT_above_lhc, np.log(dN_music_above_lhc), kind='linear')
music_above_rebin_smash_lhc = np.exp(music_above_interpolation_lhc(pT_above_plus_smash_lhc[1:14]))
music_above_rebin_music140_lhc = np.exp(music_above_interpolation_lhc(pT_above_plus_hydro140_lhc[:14]))
music_above_rebin_music120_lhc = np.exp(music_above_interpolation_lhc(pT_above_plus_hydro120_lhc[:14]))


####################################
# Ration plot 120 < T < 150
####################################

gs = gridspec.GridSpec(10,11)

common_plotting.load_plotting_style_paper()
plt.subplot(gs[:6 , 1:6])
# RHIC
plt.xscale('linear')
plt.yscale('log')
plt.xticks([])
plt.xlim(0,2.6)
plt.ylim(1e-3,1.5e1)
plt.ylabel(r'$\frac{1}{2 \pi \mathrm{p_T}} \frac{\mathrm{d^2N}}{\mathrm{dp_T d_y}}$|$_{\mathrm{y=0}}$ [Gev$^{-2}$]')
# plt.ylabel(r'1/(2$\pi$p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]        ', fontsize = 13.5)

plt.plot(pT_above_rhic, dN_music_above_rhic, label=r"MUSIC$_\mathsf{QGP}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash_rhic, dN_music_above_plus_smash_rhic, ls = '--', label='MUSIC$_\mathsf{QGP}$ + ' + 'SMASH', color = 'C2')
plt.fill_between(pT_above_plus_hydro120_rhic, dN_music_above_plus_hydro140_rhic, dN_music_above_plus_hydro120_rhic, alpha = 1.0, label = 'MUSIC$_\mathsf{QGP}$ + MUSIC$_\mathsf{HRG}$', lw = 0, color='C0')
plt.legend(fontsize=10, frameon=False)

plt.subplot(gs[6:, 1:6])
plt.xlim(0,2.6)
plt.ylim(0.98, 1.5)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')

plt.plot(pT_above_plus_smash_rhic[1:14], dN_music_above_plus_smash_rhic[1:14] / music_above_rebin_smash_rhic, label = '(MUSIC$_\mathsf{QGP}$ + SMASH) / MUSIC$_\mathsf{QGP}$', ls = '--', color = 'C2')
plt.axhline(1.0, ls = ':', color = 'C1')
plt.fill_between(pT_above_plus_hydro120_rhic[:14], dN_music_above_plus_hydro120_rhic[:14] / music_above_rebin_music120_rhic, dN_music_above_plus_hydro140_rhic[:14] / music_above_rebin_music140_rhic, label = '(MUSIC$_\mathsf{QGP}$+ MUSIC$_\mathsf{HRG}$) / MUSIC$_\mathsf{QGP}$', alpha = 1.0, color = 'C0', lw = 0)

plt.legend(frameon=False)
plt.figtext(0.115, 0.51, 'Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')

# LHC
plt.subplot(gs[:6 , 6:])
plt.xscale('linear')
plt.yscale('log')
plt.xticks([])
plt.yticks([])
plt.minorticks_off()
plt.xlim(0,2.6)
plt.ylim(1e-3,1.5e1)
# plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]       ', fontsize = 14)

plt.plot(pT_above_lhc, dN_music_above_lhc, label=r"MUSIC$_\mathsf{QGP}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash_lhc, dN_music_above_plus_smash_lhc, ls = '--', label='MUSIC$_\mathsf{QGP}$ + ' + 'SMASH', color = 'C2')
plt.fill_between(pT_above_plus_hydro120_lhc, dN_music_above_plus_hydro140_lhc, dN_music_above_plus_hydro120_lhc, alpha = 1.0, label = 'MUSIC$_\mathsf{QGP}$ + MUSIC$_\mathsf{HRG}$', lw = 0, color='C0')
plt.legend(fontsize=10, frameon=False, loc = 'upper right')

plt.subplot(gs[6:, 6:])
plt.xlim(0,2.6)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.yticks([])
plt.minorticks_off()
plt.ylim(0.98, 1.5)

plt.plot(pT_above_plus_smash_lhc[1:14], dN_music_above_plus_smash_lhc[1:14] / music_above_rebin_smash_lhc, label = '(MUSIC$_\mathsf{QGP}$ + SMASH) / MUSIC$_\mathsf{QGP}$', ls = '--', color = 'C2')
plt.axhline(1.0, ls = ':', color = 'C1')
plt.fill_between(pT_above_plus_hydro120_lhc[:14], dN_music_above_plus_hydro120_lhc[:14] / music_above_rebin_music120_lhc, dN_music_above_plus_hydro140_lhc[:14] / music_above_rebin_music140_lhc, label = '(MUSIC$_\mathsf{QGP}$+ MUSIC$_\mathsf{HRG}$) / MUSIC$_\mathsf{QGP}$', alpha = 1.0, color = 'C0', lw = 0)

plt.legend(frameon=False, loc = 'upper right')
plt.figtext(0.56, 0.51, 'Pb + Pb\n' + r'$\mathbf{\sqrt{s}}$ = 2.76 TeV', fontweight = 'bold')

plt.tight_layout(w_pad=-5.7, h_pad=-0.5)
plt.savefig("spectra_sum.pdf")
plt.close()
