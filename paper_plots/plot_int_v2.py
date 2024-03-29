import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting

data = np.loadtxt('../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/integrated_v2_photons.txt', unpack = True)

common_plotting.load_plotting_style_paper()
# mpl.rcParams['figure.figsize'] = 10*0.9*0.7*0.8, 5.3*0.9*0.9*0.7      # Make it not quite as wide for as long as we don't have LHC results
mpl.rcParams['figure.figsize'] = 10*0.9*0.7*0.85, 5.3*0.9*0.9*0.85

# mpl.rcParams['figure.figsize'] = 10*0.8*0.6, 5.3*0.8*0.8      # Make it not quite as wide for as long as we don't have LHC results
plt.plot(data[0] + 0.4, 100.0 * data[1], label = r'2$\leftrightarrow$2 Scatterings', ls = '--')
plt.plot(data[0] + 0.4, 100.0 * data[3], label = 'Bremsstrahlung', ls = '-.')
plt.plot(data[0] + 0.4, 100.0 * data[5], label = 'Total', ls = '-')

plt.fill_between(data[0]+0.4, 100.0 * (data[1] - data[2]), 100.0 * (data[1] + data[2]), alpha = 0.5, lw = 0 )
plt.fill_between(data[0]+0.4, 100.0 * (data[3] - data[4]), 100.0 * (data[3] + data[4]), alpha = 0.5, lw = 0 )
plt.fill_between(data[0]+0.4, 100.0 * (data[5] - data[6]), 100.0 * (data[5] + data[6]), alpha = 0.5, lw = 0)

plt.figtext(0.745, 0.2, '         Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')

#plt.xlim(0,60)
plt.xlim(0,60)
#plt.xscale('log')
plt.ylim(-1.5,4.5)
plt.xlabel('t [fm]')
plt.ylabel(r'v$_2^{\mathsf{\ int}, \gamma}$ [%]')
plt.legend(frameon = False)

plt.figtext(0.82, 0.965, "SMASH-2.0.1-1-g397f8f0",color = "gray", fontsize = 4.2)
plt.tight_layout()
plt.savefig('int_v2_photons.pdf')
plt.close()
