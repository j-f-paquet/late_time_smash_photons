#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import argparse
import linecache
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting


def plot_pT_spectra():
    ydata = np.loadtxt('../../calcs/photons/smash_calcs/rhic/pT.txt', unpack = True)

    exp_data_STAR_pi = np.loadtxt('../../data/hadrons/rhic/spectra_pi+_AuAu_200_cent1020_STAR2006.dat', unpack = True)
    exp_data_Phenix_pi = np.loadtxt('../../data/hadrons/rhic/spectra_pi+_AuAu_200_PHENIX2004.dat', unpack = True)
    exp_data_Phenix_k = np.loadtxt('../../data/hadrons/rhic/spectra_K+_AuAu_200_PHENIX2004.dat', unpack = True)
    exp_data_Phenix_p = np.loadtxt('../../data/hadrons/rhic/spectra_p+_AuAu_200_PHENIX2004.dat', unpack = True)
    exp_data_STAR_p = np.loadtxt('../../data/hadrons/rhic/spectra_p+_AuAu_200_cent1020_STAR2006.dat', unpack = True)

    plt.figure(figsize=(5, 3.8))
    common_plotting.load_plotting_style()
    plt.plot(ydata[0], ydata[1]/(2.0 * np.pi * ydata[0]), label = r'$\pi^+$')
    plt.plot(ydata[0], ydata[7]/(2.0 * np.pi * ydata[0]), label = r'$K^+$', ls = '--', color = 'C1')
    plt.plot(ydata[0], ydata[11]/(2.0 * np.pi * ydata[0]), label = r'p', ls = '-.', color = 'C2')

    plt.fill_between(ydata[0], ydata[1]/(2.0 * np.pi * ydata[0]) - ydata[2]/(2.0 * np.pi * ydata[0]), ydata[1]/(2.0 * np.pi * ydata[0]) + ydata[2]/(2.0 * np.pi * ydata[0]), alpha = 0.5, lw = 0)
    plt.fill_between(ydata[0], ydata[7]/(2.0 * np.pi * ydata[0]) - ydata[8]/(2.0 * np.pi * ydata[0]), ydata[7]/(2.0 * np.pi * ydata[0]) + ydata[8]/(2.0 * np.pi * ydata[0]), alpha = 0.5, lw = 0)
    plt.fill_between(ydata[0], ydata[11]/(2.0 * np.pi * ydata[0]) - ydata[12]/(2.0 * np.pi * ydata[0]), ydata[11]/(2.0 * np.pi * ydata[0]) + ydata[12]/(2.0 * np.pi * ydata[0]), alpha = 0.5, lw = 0, color = 'C2')

    # Plot experimental data
    plt.errorbar(exp_data_STAR_pi[2], exp_data_STAR_pi[3], yerr = [exp_data_STAR_pi[4], exp_data_STAR_pi[5]], ls = 'none', marker = 's', color = 'C0', label = r'$\pi^+$ STAR')
    plt.errorbar(exp_data_STAR_p[2], exp_data_STAR_p[3], exp_data_STAR_p[4], ls = 'none', marker = 's', color = 'C2', label = r'p STAR')
    plt.errorbar(exp_data_Phenix_pi[0], exp_data_Phenix_pi[7], exp_data_Phenix_pi[8], ls = 'none', marker = '^', color = 'C0', label = r'$\pi^+$ PHENIX')
    plt.errorbar(exp_data_Phenix_k[0], exp_data_Phenix_k[7], exp_data_Phenix_k[8], ls = 'none', marker = '^', color = 'C1', label = r'$K^+$ PHENIX')
    plt.errorbar(exp_data_Phenix_p[0], exp_data_Phenix_p[7], exp_data_Phenix_p[8], ls = 'none', marker = '^', color = 'C2', label = r'p PHENIX')

    plt.legend(loc = 'upper right', frameon = False)
    plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) d$^2$N/dp$_\mathrm{T}$dy|$_{y=0}$ [Gev$^{-2}$]')
    plt.yscale('log')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
    plt.xlim(0,2.0)
    plt.ylim(1e-1,1e3)

    plt.tight_layout()
    plt.savefig('pT.pdf')
    plt.close()

def plot_v2():
    v2data = np.loadtxt('../../calcs/photons/smash_calcs/rhic/SP_v2.txt', unpack = True)

    exp_data_STAR_pi = np.loadtxt('../../data/hadrons/rhic/v2_pions_AuAu_200_STAR2005.dat', unpack = True)
    exp_data_STAR_K = np.loadtxt('../../data/hadrons/rhic/v2_kaons_AuAu_200_STAR2005.dat', unpack = True)
    exp_data_STAR_p = np.loadtxt('../../data/hadrons/rhic/v2_protons_AuAu_200_STAR2005.dat', unpack = True)

    common_plotting.load_plotting_style()
    plt.plot(v2data[0], 100.0*v2data[1], label = r'$\pi^+$')
    plt.plot(v2data[0], 100.0*v2data[5], label = r'$K^+$', ls = '--')
    plt.plot(v2data[0], 100.0*v2data[3], label = r'p', ls = '-.')

    plt.fill_between(v2data[0], 100.0*v2data[1] - 100.0*v2data[2], 100.0*v2data[1] + 100.0*v2data[2], alpha = 0.5, lw = 0)
    plt.fill_between(v2data[0], 100.0*v2data[5] - 100.0*v2data[6], 100.0*v2data[5] + 100.0*v2data[6], alpha = 0.5, lw = 0)
    plt.fill_between(v2data[0], 100.0*v2data[3] - 100.0*v2data[4], 100.0*v2data[3] + 100.0*v2data[4], alpha = 0.5, lw = 0)

    # plot experimental data
    plt.errorbar(exp_data_STAR_pi[0], exp_data_STAR_pi[13], exp_data_STAR_pi[14], ls = 'none', marker = 's', color = 'C0', label = r'$\pi^+$ STAR')
    plt.errorbar(exp_data_STAR_K[0], exp_data_STAR_K[13], exp_data_STAR_K[14], ls = 'none', marker = 's', color = 'C1', label = r'$K^+$ STAR')
    plt.errorbar(exp_data_STAR_p[0], exp_data_STAR_p[13], exp_data_STAR_p[14], ls = 'none', marker = 's', color = 'C2', label = r'p  STAR')

    plt.legend(loc = 'upper left', frameon = False)
    plt.ylabel(r'$v_2^{\mathsf{\ SP}}$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
    plt.xlim(0,1.2)
    plt.ylim(-1.5,11)
    plt.tight_layout()
    plt.savefig('v2.pdf')
    plt.close()


plot_pT_spectra()
plot_v2()
