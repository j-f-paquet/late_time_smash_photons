import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt
#from matplotlib import colors, ticker, cm
#import scipy.interpolate
#from matplotlib.mlab import bivariate_normal
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as mtick
#from scipy.stats import linregress
import os.path
#from scipy.interpolate import InterpolatedUnivariateSpline
import scipy.interpolate
import seaborn as sns
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting


######################################
############ Total rate ##############
######################################

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/PbPb2760/results/photons_above_Tfr_nx200/PbPb2760/C10-20/average_sp.dat")
pT_above, dN_music_above, v1_above, v2_above, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_smash_tot.dat")
pT_above_plus_smash, dN_music_above_plus_smash, v1_music_above_plus_smash, v2_music_above_plus_smash, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140, dN_music_above_plus_hydro140, v1_music_above_plus_hydro140, v2_music_above_plus_hydro140, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120, dN_music_above_plus_hydro120, v1_music_above_plus_hydro120, v2_music_above_plus_hydro120, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/PbPb2760/combined/average_sp_hydro_tot_T100-150.dat")
pT_above_plus_hydro100, dN_music_above_plus_hydro100, v1_music_above_plus_hydro100, v2_music_above_plus_hydro100, *rest = raw.T

common_plotting.load_plotting_style()
plt.figure()
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,2.5)
plt.ylim(0,6.5)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'v$_2^{\gamma, \mathsf{SP}}$ [%]')

# SMASH
plt.plot(pT_above, 100.0 * v2_above, label=r"MUSIC$_\mathsf{QGP}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash, 100.0 * v2_music_above_plus_smash, ls = '--', label='MUSIC$_\mathsf{QGP}$ + ' + 'SMASH', color = 'C2')

# MUSIC
plt.fill_between(pT_above_plus_hydro100,  100.0 * v2_music_above_plus_hydro140,  100.0 * v2_music_above_plus_hydro100, color='C0', alpha=0.6, label = 'MUSIC$_\mathsf{QGP}$ + MUSIC$_\mathsf{HRG}$' + '100 MeV < T < 150 MeV', lw = 0)
plt.fill_between(pT_above_plus_hydro100,  100.0 * v2_music_above_plus_hydro140,  100.0 * v2_music_above_plus_hydro120, color='C0', label = 'MUSIC$_\mathsf{QGP}$ + MUSIC$_\mathsf{HRG}$' + '120 MeV < T < 150 MeV', lw = 0)

plt.legend(frameon = False, loc = 'upper left')
plt.tight_layout()
plt.savefig("v2_sum_LHC.pdf")
plt.close()
