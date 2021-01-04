import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import seaborn as sns
import common_plotting

data_photons = np.loadtxt('../../calcs/photons/smash_calcs/rhic/Mean_pT_photons_midy.txt', unpack = True)
data_hadrons = np.loadtxt('../../calcs/photons/smash_calcs/rhic/Mean_pT_medium_midy.txt', unpack = True)


common_plotting.load_plotting_style()
col2 = sns.color_palette("rocket", 6) # for even darker colour
plt.plot(data_photons[0], data_photons[1], label = r'2$\leftrightarrow$2 Scatterings', ls = '--')
plt.plot(data_photons[0], data_photons[3], label = 'Bremsstrahlung', ls = '-.')
plt.plot(data_photons[0], data_photons[5], label = 'Total', ls = '-')

plt.plot(data_hadrons[0], data_hadrons[1], label = 'Hadrons', ls = ':', color = col2[0])

# plt.fill_between(data_hadrons[0], data_hadrons[1] - data_hadrons[2], data_hadrons[1] + data_hadrons[2], color = col2[0], alpha = 0.5)
# plt.fill_between(data_photons[0], data_photons[1] - data_photons[2], data_photons[1] + data_photons[2], alpha = 0.5, lw = 0 )
# plt.fill_between(data_photons[0], data_photons[3] - data_photons[4], data_photons[3] + data_photons[4], alpha = 0.5, lw = 0 )
# plt.fill_between(data_photons[0], data_photons[5] - data_photons[6], data_photons[5] + data_photons[6], alpha = 0.5, lw = 0)

# plt.xlim(0,10000)
plt.xlim(5e0,1e4)
# plt.ylim(1e-2, 3e0)
plt.xlabel('t [fm]')
plt.xscale('log')
plt.ylabel(r'$\langle p_T \rangle |_{y = 0}$ [GeV]')
plt.legend(frameon = False, ncol = 2)
plt.tight_layout()
plt.savefig('Mean_pT.pdf')
plt.close()
