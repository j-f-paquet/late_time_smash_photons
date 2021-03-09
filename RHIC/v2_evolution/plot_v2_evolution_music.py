#!/usr/bin/python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import linecache
import seaborn as sns
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting

colors = sns.color_palette("rocket", 5)

def plot_v2_photons(v2_1, v2_5, v2_10, v2_end, output_path, energy, system):
    for file in v2_1:
        if '22_photons_' in file: v2data_2to2_1 = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'brem_photons_' in file: v2data_Brems_1 = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'tot_photons_' in file: v2data_total_1 = np.loadtxt(file, unpack = True)[[0,3]]
    for file in v2_5:
        if '22_photons_' in file: v2data_2to2_5 = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'brem_photons_' in file: v2data_Brems_5 = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'tot_photons_' in file: v2data_total_5 = np.loadtxt(file, unpack = True)[[0,3]]
    for file in v2_10:
        if '22_photons_' in file: v2data_2to2_10 = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'brem_photons_' in file: v2data_Brems_10 = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'tot_photons_' in file: v2data_total_10 = np.loadtxt(file, unpack = True)[[0,3]]
    for file in v2_end:
        if '22_photons_' in file: v2data_2to2_end = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'brem_photons_' in file: v2data_Brems_end = np.loadtxt(file, unpack = True)[[0,3]]
        elif 'tot_photons_' in file: v2data_total_end = np.loadtxt(file, unpack = True)[[0,3]]

    common_plotting.load_plotting_style()
    plt.figure(figsize=(9, 3.5))

    # 2to2 Scatterings
    plt.subplot(131)
    plt.title(r'2$\leftrightarrow$2 Scatterings')
    plt.plot(v2data_2to2_1[0], 100.0*v2data_2to2_1[1], label = r't $\leq$ 1 fm', color = colors[3], ls = ':')
    plt.plot(v2data_2to2_5[0], 100.0*v2data_2to2_5[1], label = r't $\leq$ 5 fm', color = colors[2], ls = '-.')
    plt.plot(v2data_2to2_10[0], 100.0*v2data_2to2_10[1], label = r't $\leq$ 10 fm', color = colors[1], ls = '--')
    plt.plot(v2data_2to2_end[0], 100.0*v2data_2to2_end[1], label = r't $\leq$ endtime', color = colors[0], ls = '-')

    #plt.plot(v2data_2to2_1[0], 100.0*v2data_2to2_1[1], color = colors[3])
    #plt.plot(v2data_2to2_5[0], 100.0*v2data_2to2_5[1], color = colors[2])
    #plt.plot(v2data_2to2_10[0], 100.0*v2data_2to2_10[1], color = colors[1])
    #plt.plot(v2data_2to2_end[0], 100.0*v2data_2to2_end[1], color = colors[0])
    plt.legend(frameon = False)
    plt.xlim(0,3)
    plt.ylim(-5,25)
    plt.ylabel(r'$v_2$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')

    # Bremsstrahlung
    plt.subplot(132)
    plt.title('Bremsstrahlung')
    plt.plot(v2data_Brems_1[0], 100.0*v2data_Brems_1[1], label = r't $\leq$ 1 fm', color = colors[3], ls = ':')
    plt.plot(v2data_Brems_5[0], 100.0*v2data_Brems_5[1], label = r't $\leq$ 5 fm', color = colors[2], ls = '-.')
    plt.plot(v2data_Brems_10[0], 100.0*v2data_Brems_10[1], label = r't $\leq$ 10 fm', color = colors[1], ls = '--')
    plt.plot(v2data_Brems_end[0], 100.0*v2data_Brems_end[1], label = r't $\leq$ endtime', color = colors[0], ls = '-')

    #plt.plot(v2data_Brems_1[0], 100.0*v2data_Brems_1[1], color = colors[3])
    #plt.plot(v2data_Brems_5[0], 100.0*v2data_Brems_5[1], color = colors[2])
    #plt.plot(v2data_Brems_10[0], 100.0*v2data_Brems_10[1], color = colors[1])
    #plt.plot(v2data_Brems_end[0], 100.0*v2data_Brems_end[1], color = colors[0])
    # plt.legend()
    plt.xlim(0,3)
    plt.ylim(-5,25)
    plt.ylabel(r'$v_2$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')

    # Total rate
    plt.subplot(133)
    plt.title('Total')
    plt.plot(v2data_total_1[0], 100.0*v2data_total_1[1], label = r't < 5 fm', color = colors[3], ls = ':')
    plt.plot(v2data_total_5[0], 100.0*v2data_total_5[1], label = r't < 5 fm', color = colors[2], ls = '-.')
    plt.plot(v2data_total_10[0], 100.0*v2data_total_10[1], label = r't < 10 fm', color = colors[1], ls = '--')
    plt.plot(v2data_total_end[0], 100.0*v2data_total_end[1], label = r't < 100 fm', color = colors[0], ls = '-')

    #plt.fill_between(v2data_total_1[0], 100.0*v2data_total_1[1], color = colors[3])
    #plt.fill_between(v2data_total_5[0], 100.0*v2data_total_5[1], color = colors[2])
    #plt.fill_between(v2data_total_10[0], 100.0*v2data_total_10[1], color = colors[1])
    #plt.fill_between(v2data_total_end[0], 100.0*v2data_total_end[1], color = colors[0])
    # plt.legend()
    plt.xlim(0,3)
    plt.ylim(-5,25)
    plt.ylabel(r'$v_2$ [%]')
    plt.xlabel(r'p$_\mathrm{T}$ [GeV]')

    plt.tight_layout()
    plt.savefig('v2_time_evolution_music_subplots.pdf')
    plt.close()





if __name__ == '__main__':

    file_path = (os.path.dirname(os.path.abspath(__file__)) + '/../../calcs/photons/averaged_hydro_calcs/AuAu200/results/')

    v2_1fm_photons_list = []
    v2_5fm_photons_list = []
    v2_10fm_photons_list = []
    v2_end_photons_list = []

    for file in os.listdir(file_path):
        observable = file #.split('/')[-1].split('.')[0]
        plot_path_and_name = observable + '.pdf'

        if '_T140-150_nx200' in observable:

            if '_above_Tfr_photons' in file:
                continue

            if '_before1fm' in file:
                v2_1fm_photons_list.append(file_path + file+'/AuAu200/C10-20/average_sp.dat')
            elif '_before5fm' in file:
                v2_5fm_photons_list.append(file_path + file+'/AuAu200/C10-20/average_sp.dat')
            elif '_before10fm' in file:
                v2_10fm_photons_list.append(file_path + file+'/AuAu200/C10-20/average_sp.dat') 
            else:
                v2_end_photons_list.append(file_path + file+'/AuAu200/C10-20/average_sp.dat')

plot_v2_photons(v2_1fm_photons_list, v2_5fm_photons_list, v2_10fm_photons_list, v2_end_photons_list, 'v2_photons_time_evolution_music.pdf', '200', 'AuAu')
