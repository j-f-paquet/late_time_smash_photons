import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting

data = np.loadtxt('../../calcs/photons/smash_calcs/rhic/integrated_v2_photons.txt', unpack = True)

common_plotting.load_plotting_style()
plt.plot(data[0], 100.0 * data[1], label = r'2$\leftrightarrow$2 Scatterings', ls = '--')
plt.plot(data[0], 100.0 * data[3], label = 'Bremsstrahlung', ls = '-.')
plt.plot(data[0], 100.0 * data[5], label = 'Total', ls = '-')

plt.fill_between(data[0], 100.0 * (data[1] - data[2]), 100.0 * (data[1] + data[2]), alpha = 0.5, lw = 0 )
plt.fill_between(data[0], 100.0 * (data[3] - data[4]), 100.0 * (data[3] + data[4]), alpha = 0.5, lw = 0 )
plt.fill_between(data[0], 100.0 * (data[5] - data[6]), 100.0 * (data[5] + data[6]), alpha = 0.5, lw = 0)

plt.xlim(0,200)
# plt.xscale('log')
plt.ylim(-1,5)
plt.xlabel('t [fm]')
plt.ylabel(r'v$_2^{\mathsf{\ int}, \gamma}$ [%]')
plt.legend(frameon = False)
plt.tight_layout()
plt.savefig('int_v2_photons.pdf')
plt.close()
