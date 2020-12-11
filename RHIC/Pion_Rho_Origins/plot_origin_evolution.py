#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from collections import OrderedDict
import ast
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting

keys_to_names = {'Elastic_2toX' : r'Elastic (2 $\to$ X)',
                  '2to3' : r'2 $\to$ 3',
                  '2to2' : r'2 $\to$ 2',
                  '2to1' : r'2 $\to$ 1',
                  'Elastic_decays' : 'Elastic (decay)',
                  'Decays' : 'Decay',
                  'Strings' : 'String',
                  'Sampler' : 'Sampler'}

particles = {'pion' : r'$\mathbf{\pi}$',
             'rho' : r'$\mathbf{\rho}$'}

def normalize_dict(dict):
    sum_values = sum(dict.values(), 0.0)
    # normalize to 100 percent
    dict = {k: 100.0 * v / sum_values for k, v in dict.items()}

    return dict

def only_major_contriutions(dict, cut):
    for key in dict.keys():
        if dict[key] < cut:
            del dict[key]
    return dict

def remove_zero_contributions(dict):
    for key in dict.keys():
        if float(dict[key]) == 0.0:
            del dict[key]
    return dict

def plot_origins(data, particle):

    t = [5.0, 10.0, 20.0, 50.0, 100.0]
    Sampler = []
    Decays = []
    Strings = []
    TwoToTwo = []
    El_Decay = []
    El_TwoToX = []
    TwoTo1 = []
    for key in [5.0, 10.0, 20.0, 50.0, 100.0]:
        dict2 = normalize_dict(data[key])
        Sampler.append(dict2['Sampler'])
        Decays.append(dict2['Decays'])
        Strings.append(dict2['Strings'])
        TwoToTwo.append(dict2['2 to 2'])
        El_TwoToX.append(dict2['Elastic (2 to X)'])
        El_Decay.append(dict2['Elastic (decay)'])
        TwoTo1.append(dict2['2 to 1'])

    common_plotting.load_plotting_style()
    sns.set_palette('rocket')
    plt.plot(t, Decays, label = 'Decays')
    plt.plot(t, TwoTo1, label = r'2 $\rightarrow$ 1', ls = '-.')
    plt.plot(t, Sampler, label = 'Sampler', ls = '--')
    plt.plot(t, El_Decay, label = 'Elastic (decay)', ls = ':')
    plt.plot(t, Strings, label = 'Strings', ls = '--')
    # plt.plot(t, TwoToTwo, label = r'2 $\rightarrow$ 2')
    plt.plot(t, El_TwoToX, label = r'Elastic (2 $\rightarrow$ X)', ls = '-')
    plt.xlim(0,100)
    plt.ylim(-1,80) if particle == 'pion' else plt.ylim(-1,70)
    plt.legend(ncol = 2, frameon = False)
    plt.figtext(0.25, 0.85, particles[particle], fontweight = 'bold', fontsize = 15)

    plt.xlabel('t [fm]')
    plt.ylabel('Contribution [%]')

    plt.tight_layout()
    plt.savefig('Process_Origins_Evolution_' + particle + '.pdf')
    plt.close()





if __name__ == '__main__':

    file_path = (os.path.dirname(os.path.abspath(__file__)) + '/../../calcs/photons/smash_calcs/rhic/')

    pion_mix = []
    rho_mix = []
    for file in os.listdir(file_path):
        if 'Mix' not in file: continue
        else:
            if 'Pion' in file: pion_mix.append(file_path + file)
            elif 'Rho' in file: rho_mix.append(file_path + file)


    origin_evolution_pions = {}
    origin_evolution_rhos = {}
    for file in pion_mix:
        time = file.split('_')[-1].split('fm')[0]
        with open(file, 'r') as f: data = ast.literal_eval(f.readline())
        f.close()

        origin_evolution_pions[float(time)] = data

    for file in rho_mix:
        time = file.split('_')[-1].split('fm')[0]
        with open(file, 'r') as f: data = ast.literal_eval(f.readline())
        f.close()

        origin_evolution_rhos[float(time)] = data

    plot_origins(origin_evolution_pions, 'pion')
    plot_origins(origin_evolution_rhos, 'rho')
