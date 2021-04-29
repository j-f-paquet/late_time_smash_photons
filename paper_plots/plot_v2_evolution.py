#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import linecache
import seaborn as sns
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting

colors = sns.color_palette("rocket", 7)

def plot_v2_photons(v2_1, v2_2, v2_3, v2_5, v2_10, v2_20, v2_50, v2_end, output_path, energy, system):
    for file in v2_1:
        if '2to2' in file: v2data_2to2_1 = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_1 = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_1 = np.loadtxt(file, unpack = True)
    for file in v2_2:
        if '2to2' in file: v2data_2to2_2 = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_2 = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_2 = np.loadtxt(file, unpack = True)
    for file in v2_3:
        if '2to2' in file: v2data_2to2_3 = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_3 = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_3 = np.loadtxt(file, unpack = True)
    for file in v2_5:
        if '2to2' in file: v2data_2to2_5 = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_5 = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_5 = np.loadtxt(file, unpack = True)
    for file in v2_10:
        if '2to2' in file: v2data_2to2_10 = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_10 = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_10 = np.loadtxt(file, unpack = True)
    for file in v2_20:
        if '2to2' in file: v2data_2to2_20 = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_20 = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_20 = np.loadtxt(file, unpack = True)
    for file in v2_50:
        if '2to2' in file: v2data_2to2_50 = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_50 = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_50 = np.loadtxt(file, unpack = True)
    # for file in v2_100:
    #     if '2to2' in file: v2data_2to2_100 = np.loadtxt(file, unpack = True)
    #     elif 'Brems' in file: v2data_Brems_100 = np.loadtxt(file, unpack = True)
    #     elif 'total' in file: v2data_total_100 = np.loadtxt(file, unpack = True)
    for file in v2_end:
        if '2to2' in file: v2data_2to2_end = np.loadtxt(file, unpack = True)
        elif 'Brems' in file: v2data_Brems_end = np.loadtxt(file, unpack = True)
        elif 'total' in file: v2data_total_end = np.loadtxt(file, unpack = True)


    common_plotting.load_plotting_style_paper()
    # plt.figure(figsize=(9, 3.5))

    # 2to2 Scatterings
    plt.subplot(131)
    plt.title(r'2$\leftrightarrow$2 Scatterings')
    plt.plot(v2data_2to2_1[0], 100.0*v2data_2to2_1[1], label = r't $\leq$ 1 fm', color = colors[5], ls = '--')
    plt.plot(v2data_2to2_2[0], 100.0*v2data_2to2_2[1], label = r't $\leq$ 2 fm', color = colors[4], ls = '-')
    plt.plot(v2data_2to2_3[0], 100.0*v2data_2to2_3[1], label = r't $\leq$ 3 fm', color = colors[3], ls = ':')
    plt.plot(v2data_2to2_5[0], 100.0*v2data_2to2_5[1], label = r't $\leq$ 5 fm', color = colors[2], ls = '-.')
    plt.plot(v2data_2to2_10[0], 100.0*v2data_2to2_10[1], label = r't $\leq$ 10 fm', color = colors[1], ls = '--')
    plt.plot(v2data_2to2_end[0], 100.0*v2data_2to2_end[1], label = r't $\leq$ endtime', color = colors[0], ls = '-')

    plt.fill_between(v2data_2to2_1[0], 100.0*v2data_2to2_1[1] - (100.0*v2data_2to2_1[2]), 100.0*v2data_2to2_1[1] + (100.0*v2data_2to2_1[2]), alpha = 0.3, lw = 0, color = colors[5])
    plt.fill_between(v2data_2to2_2[0], 100.0*v2data_2to2_2[1] - (100.0*v2data_2to2_2[2]), 100.0*v2data_2to2_2[1] + (100.0*v2data_2to2_2[2]), alpha = 0.3, lw = 0, color = colors[4])
    plt.fill_between(v2data_2to2_3[0], 100.0*v2data_2to2_3[1] - (100.0*v2data_2to2_3[2]), 100.0*v2data_2to2_3[1] + (100.0*v2data_2to2_3[2]), alpha = 0.3, lw = 0, color = colors[3])
    plt.fill_between(v2data_2to2_5[0], 100.0*v2data_2to2_5[1] - (100.0*v2data_2to2_5[2]), 100.0*v2data_2to2_5[1] + (100.0*v2data_2to2_5[2]), alpha = 0.3, lw = 0, color = colors[2])
    plt.fill_between(v2data_2to2_10[0], 100.0*v2data_2to2_10[1] - (100.0*v2data_2to2_10[2]), 100.0*v2data_2to2_10[1] + (100.0*v2data_2to2_10[2]), alpha = 0.3, lw = 0, color = colors[1])
    plt.fill_between(v2data_2to2_end[0], 100.0*v2data_2to2_end[1] - (100.0*v2data_2to2_end[2]), 100.0*v2data_2to2_end[1] + (100.0*v2data_2to2_end[2]), alpha = 0.3, lw = 0, color = colors[0])
    plt.legend(frameon = False)
    plt.xlim(0.1,2.6)
    plt.ylim(-5,25)
    plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')

    # Bremsstrahlung
    plt.subplot(132)
    plt.title('Bremsstrahlung')
    plt.plot(v2data_Brems_1[0], 100.0*v2data_Brems_1[1], label = r't $\leq$ 1 fm', color = colors[5], ls = '--')
    plt.plot(v2data_Brems_2[0], 100.0*v2data_Brems_2[1], label = r't $\leq$ 2 fm', color = colors[4], ls = '-')
    plt.plot(v2data_Brems_3[0], 100.0*v2data_Brems_3[1], label = r't $\leq$ 3 fm', color = colors[3], ls = ':')
    plt.plot(v2data_Brems_5[0], 100.0*v2data_Brems_5[1], label = r't $\leq$ 5 fm', color = colors[2], ls = '-.')
    plt.plot(v2data_Brems_10[0], 100.0*v2data_Brems_10[1], label = r't $\leq$ 10 fm', color = colors[1], ls = '--')
    plt.plot(v2data_Brems_end[0], 100.0*v2data_Brems_end[1], label = r't $\leq$ endtime', color = colors[0], ls = '-')

    plt.fill_between(v2data_Brems_1[0], 100.0*v2data_Brems_1[1] - (100.0*v2data_Brems_1[2]), 100.0*v2data_Brems_1[1] + (100.0*v2data_Brems_1[2]), alpha = 0.3, lw = 0, color = colors[5])
    plt.fill_between(v2data_Brems_2[0], 100.0*v2data_Brems_2[1] - (100.0*v2data_Brems_2[2]), 100.0*v2data_Brems_2[1] + (100.0*v2data_Brems_2[2]), alpha = 0.3, lw = 0, color = colors[4])
    plt.fill_between(v2data_Brems_3[0], 100.0*v2data_Brems_3[1] - (100.0*v2data_Brems_3[2]), 100.0*v2data_Brems_3[1] + (100.0*v2data_Brems_3[2]), alpha = 0.3, lw = 0, color = colors[3])
    plt.fill_between(v2data_Brems_5[0], 100.0*v2data_Brems_5[1] - (100.0*v2data_Brems_5[2]), 100.0*v2data_Brems_5[1] + (100.0*v2data_Brems_5[2]), alpha = 0.3, lw = 0, color = colors[2])
    plt.fill_between(v2data_Brems_10[0], 100.0*v2data_Brems_10[1] - (100.0*v2data_Brems_10[2]), 100.0*v2data_Brems_10[1] + (100.0*v2data_Brems_10[2]), alpha = 0.3, lw = 0, color = colors[1])
    plt.fill_between(v2data_Brems_end[0], 100.0*v2data_Brems_end[1] - (100.0*v2data_Brems_end[2]), 100.0*v2data_Brems_end[1] + (100.0*v2data_Brems_end[2]), alpha = 0.3, lw = 0, color = colors[0])
    # plt.legend()
    plt.xlim(0.1,2.6)
    plt.ylim(-5,25)
    # plt.ylabel(r'$v_2$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
    plt.yticks([])

    # Total rate
    plt.subplot(133)
    plt.title('Total')
    plt.plot(v2data_total_1[0], 100.0*v2data_total_1[1], label = r't < 1 fm', color = colors[4], ls = '--')
    plt.plot(v2data_total_2[0], 100.0*v2data_total_2[1], label = r't < 2 fm', color = colors[4], ls = '-')
    plt.plot(v2data_total_3[0], 100.0*v2data_total_3[1], label = r't < 3 fm', color = colors[3], ls = ':')
    plt.plot(v2data_total_5[0], 100.0*v2data_total_5[1], label = r't < 5 fm', color = colors[2], ls = '-.')
    plt.plot(v2data_total_10[0], 100.0*v2data_total_10[1], label = r't < 10 fm', color = colors[1], ls = '--')
    plt.plot(v2data_total_end[0], 100.0*v2data_total_end[1], label = r't < 100 fm', color = colors[0], ls = '-')

    plt.fill_between(v2data_total_1[0], 100.0*v2data_total_1[1] - (100.0*v2data_total_1[2]), 100.0*v2data_total_1[1] + (100.0*v2data_total_1[2]), alpha = 0.3, lw = 0, color = colors[5])
    plt.fill_between(v2data_total_2[0], 100.0*v2data_total_2[1] - (100.0*v2data_total_2[2]), 100.0*v2data_total_2[1] + (100.0*v2data_total_2[2]), alpha = 0.3, lw = 0, color = colors[4])
    plt.fill_between(v2data_total_3[0], 100.0*v2data_total_3[1] - (100.0*v2data_total_3[2]), 100.0*v2data_total_3[1] + (100.0*v2data_total_3[2]), alpha = 0.3, lw = 0, color = colors[3])
    plt.fill_between(v2data_total_5[0], 100.0*v2data_total_5[1] - (100.0*v2data_total_5[2]), 100.0*v2data_total_5[1] + (100.0*v2data_total_5[2]), alpha = 0.3, lw = 0, color = colors[2])
    plt.fill_between(v2data_total_10[0], 100.0*v2data_total_10[1] - (100.0*v2data_total_10[2]), 100.0*v2data_total_10[1] + (100.0*v2data_total_10[2]), alpha = 0.3, lw = 0, color = colors[1])
    plt.fill_between(v2data_total_end[0], 100.0*v2data_total_end[1] - (100.0*v2data_total_end[2]), 100.0*v2data_total_end[1] + (100.0*v2data_total_end[2]), alpha = 0.3, lw = 0, color = colors[0])
    # plt.legend()
    plt.xlim(0.1,2.6)
    plt.ylim(-5,25)
    # plt.ylabel(r'$v_2$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')
    plt.yticks([])
    plt.figtext(0.7, 0.85, 'Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')

    plt.figtext(0.906, 0.89, "SMASH-2.0.1",color = "gray", fontsize = 6.3)
    plt.tight_layout(w_pad=0.09)
    plt.savefig('v2_time_evolution_subplots.pdf')
    plt.close()





if __name__ == '__main__':

    file_path = (os.path.dirname(os.path.abspath(__file__)) + '/../calcs/photons/smash_calcs/rhic/SMASH-2.0.1/')

    v2_1fm_photons_list = []
    v2_2fm_photons_list = []
    v2_3fm_photons_list = []
    v2_5fm_photons_list = []
    v2_10fm_photons_list = []
    v2_20fm_photons_list = []
    v2_50fm_photons_list = []
    # v2_100fm_photons_list = []
    v2_end_photons_list = []

    for file in os.listdir(file_path):
        observable = file.split('/')[-1].split('.')[0]
        plot_path_and_name = observable + '.pdf'

        if 'SP_v2_photons' in observable:
            if 'no_pT_cut' in observable: continue
            if 'tmax1.' in file:
                v2_1fm_photons_list.append(file_path + file)
            elif 'tmax2.' in file:
                v2_2fm_photons_list.append(file_path + file)
            elif 'tmax3.' in file:
                v2_3fm_photons_list.append(file_path + file)
            elif 'tmax5.' in file:
                v2_5fm_photons_list.append(file_path + file)
            elif 'tmax10.' in file:
                v2_10fm_photons_list.append(file_path + file)
            elif 'tmax20.' in file:
                v2_20fm_photons_list.append(file_path + file)
            elif 'tmax50.' in file:
                v2_50fm_photons_list.append(file_path + file)
            # elif 'tmax100.' in file:
            #     v2_100fm_photons_list.append(file_path + file)
            else:
                v2_end_photons_list.append(file_path + file)

plot_v2_photons(v2_1fm_photons_list, v2_2fm_photons_list, v2_3fm_photons_list, v2_5fm_photons_list, v2_10fm_photons_list, v2_20fm_photons_list, v2_50fm_photons_list, v2_end_photons_list, 'v2_photons_time_evolution.pdf', '200', 'AuAu')
