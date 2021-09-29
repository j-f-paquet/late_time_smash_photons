#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import argparse
import linecache
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting
from matplotlib import gridspec

# RHIC
ydata_rhic = np.loadtxt('../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/pT.txt', unpack = True)
exp_data_STAR_pi_rhic = np.loadtxt('../data/hadrons/rhic/spectra_pi+_AuAu_200_cent1020_STAR2006.dat', unpack = True)
exp_data_Phenix_pi_rhic = np.loadtxt('../data/hadrons/rhic/spectra_pi+_AuAu_200_PHENIX2004.dat', unpack = True)
exp_data_Phenix_k_rhic = np.loadtxt('../data/hadrons/rhic/spectra_K+_AuAu_200_PHENIX2004.dat', unpack = True)
exp_data_Phenix_p_rhic = np.loadtxt('../data/hadrons/rhic/spectra_p+_AuAu_200_PHENIX2004.dat', unpack = True)
exp_data_STAR_p_rhic = np.loadtxt('../data/hadrons/rhic/spectra_p+_AuAu_200_cent1020_STAR2006.dat', unpack = True)

v2data_rhic = np.loadtxt('../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/SP_v2.txt', unpack = True)
v2exp_data_STAR_pi_rhic= np.loadtxt('../data/hadrons/rhic/v2_pions_AuAu_200_STAR2005.dat', unpack = True)
v2exp_data_STAR_K_rhic = np.loadtxt('../data/hadrons/rhic/v2_kaons_AuAu_200_STAR2005.dat', unpack = True)
v2exp_data_STAR_p_rhic = np.loadtxt('../data/hadrons/rhic/v2_protons_AuAu_200_STAR2005.dat', unpack = True)

# LHC
ydata_lhc = np.loadtxt('../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/pT.txt', unpack = True)
exp_data_ALICE_pi_lhc = np.loadtxt('../data/hadrons/lhc/spectra_pis_PbPb_2760_1020_ALICE2013.dat', unpack = True)
exp_data_ALICE_K_lhc = np.loadtxt('../data/hadrons/lhc/spectra_Ks_PbPb_2760_1020_ALICE2013.dat', unpack = True)
exp_data_ALICE_p_lhc = np.loadtxt('../data/hadrons/lhc/spectra_ppbar_PbPb_2760_1020_ALICE2013.dat', unpack = True)

v2data_lhc = np.loadtxt('../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/SP_v2.txt', unpack = True)
v2exp_ALICE_pi_lhc = np.loadtxt('../data/hadrons/lhc/v2_LHC_PbPb_2.76TeV_1020_ALICE_pions.dat', unpack = True)
v2exp_ALICE_K_lhc = np.loadtxt('../data/hadrons/lhc/v2_LHC_PbPb_2.76TeV_1020_ALICE_kaons.dat', unpack = True)
v2exp_ALICE_p_lhc = np.loadtxt('../data/hadrons/lhc/v2_LHC_PbPb_2.76TeV_1020_ALICE_protons_plus_antiprotons.dat', unpack = True)

gs = gridspec.GridSpec(10,11)
common_plotting.load_plotting_style_paper()


################
# RHIC
################
plt.subplot(gs[:5 , 1:6])
plt.title(r'Au + Au @ $\sqrt{s}$ = 200 GeV')
plt.plot(ydata_rhic[0], ydata_rhic[1]/(2.0 * np.pi * ydata_rhic[0]), label = r' $\pi^+$')
plt.plot(ydata_rhic[0], ydata_rhic[7]/(2.0 * np.pi * ydata_rhic[0]), label = r' $K^+$', ls = '--', color = 'C1')
plt.plot(ydata_rhic[0], ydata_rhic[11]/(2.0 * np.pi * ydata_rhic[0]), label = r' p', ls = '-.', color = 'C2')

plt.fill_between(ydata_rhic[0], ydata_rhic[1]/(2.0 * np.pi * ydata_rhic[0]) - ydata_rhic[2]/(2.0 * np.pi * ydata_rhic[0]), ydata_rhic[1]/(2.0 * np.pi * ydata_rhic[0]) + ydata_rhic[2]/(2.0 * np.pi * ydata_rhic[0]), alpha = 0.5, lw = 0)
plt.fill_between(ydata_rhic[0], ydata_rhic[7]/(2.0 * np.pi * ydata_rhic[0]) - ydata_rhic[8]/(2.0 * np.pi * ydata_rhic[0]), ydata_rhic[7]/(2.0 * np.pi * ydata_rhic[0]) + ydata_rhic[8]/(2.0 * np.pi * ydata_rhic[0]), alpha = 0.5, lw = 0)
plt.fill_between(ydata_rhic[0], ydata_rhic[11]/(2.0 * np.pi * ydata_rhic[0]) - ydata_rhic[12]/(2.0 * np.pi * ydata_rhic[0]), ydata_rhic[11]/(2.0 * np.pi * ydata_rhic[0]) + ydata_rhic[12]/(2.0 * np.pi * ydata_rhic[0]), alpha = 0.5, lw = 0, color = 'C2')

# Plot experimental data
plt.errorbar(exp_data_STAR_pi_rhic[2], exp_data_STAR_pi_rhic[3], yerr = [exp_data_STAR_pi_rhic[4], exp_data_STAR_pi_rhic[5]], ls = 'none', marker = 's', color = 'C0')#, label = r'$\pi^+$ STAR')
plt.errorbar(exp_data_STAR_p_rhic[2], exp_data_STAR_p_rhic[3], exp_data_STAR_p_rhic[4], ls = 'none', marker = 's', color = 'C2')#, label = r'p STAR')
plt.errorbar(exp_data_Phenix_pi_rhic[0], exp_data_Phenix_pi_rhic[7], exp_data_Phenix_pi_rhic[8], ls = 'none', marker = '^', color = 'C0')#, label = r'$\pi^+$ PHENIX')
plt.errorbar(exp_data_Phenix_k_rhic[0], exp_data_Phenix_k_rhic[7], exp_data_Phenix_k_rhic[8], ls = 'none', marker = '^', color = 'C1')#, label = r'$K^+$ PHENIX')
plt.errorbar(exp_data_Phenix_p_rhic[0], exp_data_Phenix_p_rhic[7], exp_data_Phenix_p_rhic[8], ls = 'none', marker = '^', color = 'C2')#, label = r'p PHENIX')

# dummy
plt.plot(0.5, 1e4, ls = 'none', marker = 's', color = 'grey', label = 'STAR')
plt.plot(0.5, 1e4, ls = 'none', marker = '^', color = 'grey', label = 'PHENIX')
plt.plot(0.5, 1e4, ls = 'none', marker = 'o', color = 'grey', label = 'ALICE')
plt.legend(loc = 'upper right', frameon = False, ncol = 2, columnspacing = -0.2, handletextpad = 0.5)

# plt.ylabel(r'1/(2$\pi$p$_\mathrm{T}$) d$^2$N/dp$_\mathrm{T}$dy|$_{y=0}$ [Gev$^{-2}$]', fontsize = 12)
plt.ylabel(r'  $\frac{1}{2 \pi \mathrm{p_T}} \frac{\mathrm{d^2N}}{\mathrm{dp_T d_y}}$|$_{\mathrm{y=0}}$ [Gev$^{-2}$]', fontsize = 14)
plt.yscale('log')
# plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
plt.xlim(0.1,1.1)
plt.ylim(9e-1,1e3)
plt.xticks([])



plt.subplot(gs[5: , 1:6])
plt.plot(v2data_rhic[0], 100.0*v2data_rhic[1], label = r'$\pi^+$')
plt.plot(v2data_rhic[0], 100.0*v2data_rhic[5], label = r'$K^+$', ls = '--')
plt.plot(v2data_rhic[0], 100.0*v2data_rhic[3], label = r'p', ls = '-.')

plt.fill_between(v2data_rhic[0], 100.0*v2data_rhic[1] - 100.0*v2data_rhic[2], 100.0*v2data_rhic[1] + 100.0*v2data_rhic[2], alpha = 0.5, lw = 0)
plt.fill_between(v2data_rhic[0], 100.0*v2data_rhic[5] - 100.0*v2data_rhic[6], 100.0*v2data_rhic[5] + 100.0*v2data_rhic[6], alpha = 0.5, lw = 0)
plt.fill_between(v2data_rhic[0], 100.0*v2data_rhic[3] - 100.0*v2data_rhic[4], 100.0*v2data_rhic[3] + 100.0*v2data_rhic[4], alpha = 0.5, lw = 0)

# plot experimental data
plt.errorbar(v2exp_data_STAR_pi_rhic[0], v2exp_data_STAR_pi_rhic[13], v2exp_data_STAR_pi_rhic[14], ls = 'none', marker = 's', color = 'C0', label = r'$\pi^+$ STAR')
plt.errorbar(v2exp_data_STAR_K_rhic[0], v2exp_data_STAR_K_rhic[13], v2exp_data_STAR_K_rhic[14], ls = 'none', marker = 's', color = 'C1', label = r'$K^+$ STAR')
plt.errorbar(v2exp_data_STAR_p_rhic[0], v2exp_data_STAR_p_rhic[13], v2exp_data_STAR_p_rhic[14], ls = 'none', marker = 's', color = 'C2', label = r'p  STAR')

# plt.legend(loc = 'upper left', frameon = False)
plt.ylabel(r'$v_2^{\mathsf{\ SP}}$ [%]')
plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
plt.xlim(0.1,1.1)
plt.ylim(-1.5,11)


################
# LHC
################
plt.subplot(gs[:5 , 6:])
plt.title(r'Pb + Pb @ $\sqrt{s}$ = 2.76 TeV')
plt.plot(ydata_lhc[0], ydata_lhc[1]/(2.0 * np.pi * ydata_lhc[0]), label = r'$\pi^+$')
plt.plot(ydata_lhc[0], ydata_lhc[7]/(2.0 * np.pi * ydata_lhc[0]), label = r'$K^+$', ls = '--', color = 'C1')
plt.plot(ydata_lhc[0], ydata_lhc[11]/(2.0 * np.pi * ydata_lhc[0]), label = r'p', ls = '-.', color = 'C2')

plt.fill_between(ydata_lhc[0], ydata_lhc[1]/(2.0 * np.pi * ydata_lhc[0]) - ydata_lhc[2]/(2.0 * np.pi * ydata_lhc[0]), ydata_lhc[1]/(2.0 * np.pi * ydata_lhc[0]) + ydata_lhc[2]/(2.0 * np.pi * ydata_lhc[0]), alpha = 0.5, lw = 0)
plt.fill_between(ydata_lhc[0], ydata_lhc[7]/(2.0 * np.pi * ydata_lhc[0]) - ydata_lhc[8]/(2.0 * np.pi * ydata_lhc[0]), ydata_lhc[7]/(2.0 * np.pi * ydata_lhc[0]) + ydata_lhc[8]/(2.0 * np.pi * ydata_lhc[0]), alpha = 0.5, lw = 0)
plt.fill_between(ydata_lhc[0], ydata_lhc[11]/(2.0 * np.pi * ydata_lhc[0]) - ydata_lhc[12]/(2.0 * np.pi * ydata_lhc[0]), ydata_lhc[11]/(2.0 * np.pi * ydata_lhc[0]) + ydata_lhc[12]/(2.0 * np.pi * ydata_lhc[0]), alpha = 0.5, lw = 0, color = 'C2')

# Plot experimental data
plt.errorbar(exp_data_ALICE_pi_lhc[0], exp_data_ALICE_pi_lhc[1], yerr = [exp_data_ALICE_pi_lhc[2], exp_data_ALICE_pi_lhc[3]], ls = 'none', marker = 'o', color = 'C0')
plt.errorbar(exp_data_ALICE_K_lhc[0], exp_data_ALICE_K_lhc[1], yerr = [exp_data_ALICE_K_lhc[2], exp_data_ALICE_K_lhc[3]], ls = 'none', marker = 'o', color = 'C1')
plt.errorbar(exp_data_ALICE_p_lhc[0], exp_data_ALICE_p_lhc[1], yerr = [exp_data_ALICE_p_lhc[2], exp_data_ALICE_p_lhc[3]], ls = 'none', marker = 'o', color = 'C2')

plt.yscale('log')
plt.xlim(0.1,1.1)
plt.ylim(9e-1,1e3)
plt.xticks([])
plt.yticks([])
plt.minorticks_off()

# dummy
plt.plot(0.5, 1e4, ls = 'none', marker = 's', color = 'grey', label = 'STAR')
plt.plot(0.5, 1e4, ls = 'none', marker = '^', color = 'grey', label = 'PHENIX')
plt.plot(0.5, 1e4, ls = 'none', marker = 'o', color = 'grey', label = 'ALICE')
# plt.legend(loc = 'upper right', frameon = False, ncol = 2)



plt.subplot(gs[5: , 6:])
plt.plot(v2data_lhc[0], 100.0*v2data_lhc[1], label = r'$\pi^+$')
plt.plot(v2data_lhc[0], 100.0*v2data_lhc[5], label = r'$K^+$', ls = '--')
plt.plot(v2data_lhc[0], 100.0*v2data_lhc[3], label = r'p', ls = '-.')

plt.fill_between(v2data_lhc[0], 100.0*v2data_lhc[1] - 100.0*v2data_lhc[2], 100.0*v2data_lhc[1] + 100.0*v2data_lhc[2], alpha = 0.5, lw = 0)
plt.fill_between(v2data_lhc[0], 100.0*v2data_lhc[5] - 100.0*v2data_lhc[6], 100.0*v2data_lhc[5] + 100.0*v2data_lhc[6], alpha = 0.5, lw = 0)
plt.fill_between(v2data_lhc[0], 100.0*v2data_lhc[3] - 100.0*v2data_lhc[4], 100.0*v2data_lhc[3] + 100.0*v2data_lhc[4], alpha = 0.5, lw = 0)

# plot experimental data
plt.errorbar(v2exp_ALICE_pi_lhc[0], 100.0 * v2exp_ALICE_pi_lhc[3], yerr=[100.0 * v2exp_ALICE_pi_lhc[4], 100.0 * v2exp_ALICE_pi_lhc[5]], ls = 'none', marker = 'o', color = 'C0', label = r'ALICE $\pi$')
plt.errorbar(v2exp_ALICE_K_lhc[0], 100.0 * v2exp_ALICE_K_lhc[3], yerr=[100.0 * v2exp_ALICE_K_lhc[4], 100.0 * v2exp_ALICE_K_lhc[5]], ls = 'none', marker = 'o', color = 'C1', label = r'ALICE K')
plt.errorbar(v2exp_ALICE_p_lhc[0], 100.0 * v2exp_ALICE_p_lhc[3], yerr=[100.0 * v2exp_ALICE_p_lhc[4], 100.0 * v2exp_ALICE_p_lhc[5]], ls = 'none', marker = 'o', color = 'C2', label = r'ALICE p + $\bar{\mathsf{p}}$')

plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
plt.yticks([])
plt.xlim(0.1,1.1)
plt.ylim(-1.5,11)



plt.figtext(0.865, 0.894, "SMASH-2.0.1-1-g397f8f0",color = "gray", fontsize = 5.3)
plt.tight_layout(h_pad=-0.2, w_pad=-5.3)
plt.savefig('hadron_spectra.pdf')
plt.close()
