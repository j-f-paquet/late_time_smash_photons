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
import matplotlib.gridspec as gridspec
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting

######################################
############ Total rate ##############
######################################

raw=np.loadtxt("../rate_comparison/from_anna_T150/PhotonRate_Brems.txt")
pT_brem = raw[:,0]
dN_brem = raw[:,-2]
dN_brem_err = raw[:,-1]
dN_brem[dN_brem < 1e-100] = 1e-100
pre_interp_brem = scipy.interpolate.interp1d(pT_brem, np.log(dN_brem), kind='linear')
pre_interp_brem_err = scipy.interpolate.interp1d(pT_brem, np.log(dN_brem_err), kind='linear')
interp_brem=lambda x: np.exp(pre_interp_brem(x))
interp_brem_err=lambda x: np.exp(pre_interp_brem_err(x))

raw=np.loadtxt("../rate_comparison/from_anna_T150/PhotonRate_2to2.txt")
pT_22 = raw[:,0]
dN_22=raw[:,-2]-(raw[:,1]+raw[:,3])
dN_22_err=raw[:,-1]+(raw[:,2]+raw[:,4])
dN_22[dN_22<1e-100]=1e-100
pre_interp_22 = scipy.interpolate.interp1d(pT_22, np.log(dN_22), kind='linear')
pre_interp_22_err = scipy.interpolate.interp1d(pT_22, np.log(dN_22_err), kind='linear')
interp_22 = lambda x: np.exp(pre_interp_22(x))
interp_22_err = lambda x: np.exp(pre_interp_22_err(x))

raw=np.loadtxt("../rate_comparison/thermal_photons/pi_rho_to_pi_gamma.dat")
pT_jf_22 = raw[:,0]
dN_jf_22 = raw[:,1]

raw=np.loadtxt("../rate_comparison/thermal_photons/pion_brem_rapp.dat")
pT_jf_brem = raw[:,0]
dN_jf_brem= raw[:,1]

raw=np.loadtxt("../rate_comparison/thermal_photons/total_hadronic_rate_for_test.dat")
pT_jf_total = raw[:,0]
dN_jf_total = raw[:,1]
#interp_jf = scipy.interpolate.interp1d(pT_jf, np.log(dN_jf), kind='linear')

gs = gridspec.GridSpec(10,1)
common_plotting.load_plotting_style_paper()
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 10*0.9*0.7*0.85, 5.3*0.9*0.9*0.85
# mpl.rcParams['figure.figsize'] = 10*0.8*0.7, 5.3*0.8
plt.figure()
plt.subplot(gs[:7 , :])
plt.xscale('linear')
plt.yscale('log')
plt.xticks([])
plt.ylabel(r"E $\frac{\mathrm{dR}}{\mathrm{d}^{3}\mathrm{p}}$ [GeV$^{-2}$ fm$^{-4}$]")

# SMASH
resampled_smash_pT=np.linspace(np.max([pT_brem[0],0.2]),np.max(pT_brem),30)
plt.plot(resampled_smash_pT, interp_22(resampled_smash_pT)  , label='2$\leftrightarrow$2 Scatterings',)
plt.plot(resampled_smash_pT, interp_brem(resampled_smash_pT), label='Bremsstrahlung')
plt.plot(resampled_smash_pT, interp_brem(resampled_smash_pT)+interp_22(resampled_smash_pT), label='Total')

plt.fill_between(resampled_smash_pT, interp_22(resampled_smash_pT) - interp_22_err(resampled_smash_pT), interp_22(resampled_smash_pT) + interp_22_err(resampled_smash_pT), lw = 0, alpha = 0.5)
plt.fill_between(resampled_smash_pT, interp_brem(resampled_smash_pT) - interp_brem_err(resampled_smash_pT), interp_brem(resampled_smash_pT) + interp_brem_err(resampled_smash_pT), lw = 0, alpha = 0.5)
plt.fill_between(resampled_smash_pT, interp_22(resampled_smash_pT) + interp_brem(resampled_smash_pT) - np.sqrt(interp_22_err(resampled_smash_pT)**2 + interp_brem_err(resampled_smash_pT)**2), interp_22(resampled_smash_pT) + interp_brem(resampled_smash_pT) + np.sqrt(interp_22_err(resampled_smash_pT)**2 + interp_brem_err(resampled_smash_pT)**2), lw = 0, alpha = 0.5)

# MUSIC
plt.plot(pT_jf_22,dN_jf_22, '--')
plt.plot(pT_jf_brem,dN_jf_brem,"--")
plt.plot(pT_jf_total,dN_jf_total,"--")

# dummies for legend entry
plt.plot(1,50, color ='grey', label = 'SMASH')
plt.plot(1,70, color ='grey', label = 'MUSIC', ls = '--')

plt.xlim(0.2,3.0)
plt.ylim(1e-14, 1e-2)
plt.legend(loc='upper right', frameon=False, ncol=2)
plt.figtext(0.23, 0.88, 'T = 150 MeV', fontweight = 'bold')

plt.subplot(gs[7:, :])
plt.plot(pT_jf_total, (interp_brem(pT_jf_total)+interp_22(pT_jf_total)) / dN_jf_total, label = r'Total$_\mathsf{SMASH}$ / Total$_\mathsf{MUSIC}$', color = 'C2')
plt.fill_between(pT_jf_total, (interp_brem(pT_jf_total)+interp_22(pT_jf_total) - interp_brem_err(pT_jf_total)-interp_22_err(pT_jf_total)) / dN_jf_total, (interp_brem(pT_jf_total)+interp_22(pT_jf_total) + interp_brem_err(pT_jf_total)+interp_22_err(pT_jf_total)) / dN_jf_total, color = 'C2', alpha = 0.5, lw = 0)
plt.axhline(1.0, color = 'grey', lw = 1)
plt.xlim(0.2,3.0)
plt.ylim(0.0,2.0)
plt.xlabel(r'E [GeV]')
plt.legend(loc='upper left', frameon=False)

plt.figtext(0.882, 0.944, "SMASH-2.0.1",color = "gray", fontsize = 4.2)
plt.tight_layout(h_pad = -0.5)
plt.savefig("thermal_photon_comparison.pdf")
plt.close()
