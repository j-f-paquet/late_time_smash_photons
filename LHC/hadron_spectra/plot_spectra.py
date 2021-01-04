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
    ydata = np.loadtxt('../../calcs/hadrons/smash_calcs/lhc/low_stats/pT.txt', unpack = True)

    exp_data_ALICE_pi = np.loadtxt('../../data/hadrons/lhc/spectra_pis_PbPb_2760_1020_ALICE2013.dat', unpack = True)
    exp_data_ALICE_K = np.loadtxt('../../data/hadrons/lhc/spectra_Ks_PbPb_2760_1020_ALICE2013.dat', unpack = True)
    exp_data_ALICE_p = np.loadtxt('../../data/hadrons/lhc/spectra_ppbar_PbPb_2760_1020_ALICE2013.dat', unpack = True)

    plt.figure(figsize=(5, 3.8))
    common_plotting.load_plotting_style()
    plt.plot(ydata[0], ydata[1]/(2.0 * np.pi * ydata[0]), label = r'$\pi^+$')
    plt.plot(ydata[0], ydata[7]/(2.0 * np.pi * ydata[0]), label = r'$K^+$', ls = '--', color = 'C1')
    plt.plot(ydata[0], ydata[11]/(2.0 * np.pi * ydata[0]), label = r'p', ls = '-.', color = 'C2')

    plt.fill_between(ydata[0], ydata[1]/(2.0 * np.pi * ydata[0]) - ydata[2]/(2.0 * np.pi * ydata[0]), ydata[1]/(2.0 * np.pi * ydata[0]) + ydata[2]/(2.0 * np.pi * ydata[0]), alpha = 0.5, lw = 0)
    plt.fill_between(ydata[0], ydata[7]/(2.0 * np.pi * ydata[0]) - ydata[8]/(2.0 * np.pi * ydata[0]), ydata[7]/(2.0 * np.pi * ydata[0]) + ydata[8]/(2.0 * np.pi * ydata[0]), alpha = 0.5, lw = 0)
    plt.fill_between(ydata[0], ydata[11]/(2.0 * np.pi * ydata[0]) - ydata[12]/(2.0 * np.pi * ydata[0]), ydata[11]/(2.0 * np.pi * ydata[0]) + ydata[12]/(2.0 * np.pi * ydata[0]), alpha = 0.5, lw = 0, color = 'C2')

    # Plot experimental data
    plt.errorbar(exp_data_ALICE_pi[0], exp_data_ALICE_pi[1], yerr = [exp_data_ALICE_pi[2], exp_data_ALICE_pi[3]], ls = 'none', marker = '^', color = 'C0', label = r'$\pi^+$ ALICE')
    plt.errorbar(exp_data_ALICE_K[0], exp_data_ALICE_K[1], yerr = [exp_data_ALICE_K[2], exp_data_ALICE_K[3]], ls = 'none', marker = '^', color = 'C1', label = r'$\pi^+$ ALICE')
    plt.errorbar(exp_data_ALICE_p[0], exp_data_ALICE_p[1], yerr = [exp_data_ALICE_p[2], exp_data_ALICE_p[3]], ls = 'none', marker = '^', color = 'C2', label = r'$\pi^+$ ALICE')


    plt.legend(loc = 'upper right', frameon = False)
    plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) d$^2$N/dp$_\mathrm{T}$dy|$_{y=0}$ [Gev$^{-2}$]')
    plt.yscale('log')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
    plt.xlim(0,2.0)
    plt.ylim(1e-1,1e3)

    plt.tight_layout()
    plt.savefig('pT_LHC.pdf')
    plt.close()

def plot_v2():
    v2data = np.loadtxt('../../calcs/hadrons/smash_calcs/lhc/low_stats/SP_v2.txt', unpack = True)

    # exp_data_ALICE_charged_had = np.loadtxt('v2_ch_hadrons_PbPb_5020_1020_ALICE.dat', unpack = True)
    exp_ALICE_pi = np.loadtxt('../../data/hadrons/lhc/v2_LHC_PbPb_2.76TeV_1020_ALICE_pions.dat', unpack = True)
    exp_ALICE_K = np.loadtxt('../../data/hadrons/lhc/v2_LHC_PbPb_2.76TeV_1020_ALICE_kaons.dat', unpack = True)
    exp_ALICE_p = np.loadtxt('../../data/hadrons/lhc/v2_LHC_PbPb_2.76TeV_1020_ALICE_protons_plus_antiprotons.dat', unpack = True)

    common_plotting.load_plotting_style()
    plt.plot(v2data[0], 100.0*v2data[1], label = r'$\pi^+$')
    plt.plot(v2data[0], 100.0*v2data[5], label = r'$K^+$', ls = '--')
    plt.plot(v2data[0], 100.0*v2data[3], label = r'p', ls = '-.')

    plt.fill_between(v2data[0], 100.0*v2data[1] - 100.0*v2data[2], 100.0*v2data[1] + 100.0*v2data[2], alpha = 0.5, lw = 0)
    plt.fill_between(v2data[0], 100.0*v2data[5] - 100.0*v2data[6], 100.0*v2data[5] + 100.0*v2data[6], alpha = 0.5, lw = 0)
    plt.fill_between(v2data[0], 100.0*v2data[3] - 100.0*v2data[4], 100.0*v2data[3] + 100.0*v2data[4], alpha = 0.5, lw = 0)

    # plot experimental data
    plt.errorbar(exp_ALICE_pi[0], 100.0 * exp_ALICE_pi[3], yerr=[100.0 * exp_ALICE_pi[4], 100.0 * exp_ALICE_pi[5]], ls = 'none', marker = 's', color = 'C0', label = r'ALICE $\pi$')
    plt.errorbar(exp_ALICE_K[0], 100.0 * exp_ALICE_K[3], yerr=[100.0 * exp_ALICE_K[4], 100.0 * exp_ALICE_K[5]], ls = 'none', marker = 's', color = 'C1', label = r'ALICE K')
    plt.errorbar(exp_ALICE_p[0], 100.0 * exp_ALICE_p[3], yerr=[100.0 * exp_ALICE_p[4], 100.0 * exp_ALICE_p[5]], ls = 'none', marker = 's', color = 'C2', label = r'ALICE p + $\bar{\mathsf{p}}$')

    plt.legend(loc = 'upper left', frameon = False)
    plt.ylabel(r'$v_2^{\mathsf{\ SP}}$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
    plt.xlim(0,1.2)
    plt.ylim(-1.5,11)
    plt.tight_layout()
    plt.savefig('v2_LHC.pdf')
    plt.close()


plot_pT_spectra()
plot_v2()
