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
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting

######################################
############ Total rate ##############
######################################

# SMASH
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/pT_photons_midy.txt")
pT_smash, pre_dN_22, pre_dN_22_err, pre_dN_brem, pre_dN_brem_err = raw.T
dN_22=pre_dN_22/(2*np.pi*pT_smash)
dN_22_err=pre_dN_22_err/(2*np.pi*pT_smash)
dN_brem=pre_dN_brem/(2*np.pi*pT_smash)
dN_brem_err=pre_dN_brem_err/(2*np.pi*pT_smash)

# Hydro+rate
#photons_T140-150_nx200/vn_rate_hg_ideal_Turbide_fit_noPiPi_tabulated.dat
#photons_T140-150_nx200/vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated.dat
#photons_T140-150_nx200/vn_rate_thermal_ideal.dat
#photons_above_Tfr_nx200/vn_rate_hg_ideal_Turbide_fit_noPiPi_tabulated.dat
#photons_above_Tfr_nx200/vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated.dat
#photons_above_Tfr_nx200/vn_rate_qgp_ideal_LO_AMYfit.dat
#photons_above_Tfr_nx200/vn_rate_thermal_ideal.dat

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_above_Tfr, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/22_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_22, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/brem_photons_T140-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_140_150_brem, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/22_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_120_150_22, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/brem_photons_T120-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_120_150_brem, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/22_photons_T100-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_100_150_22, *rest = raw.T

raw=np.loadtxt("../calcs/photons/averaged_hydro_calcs/results/brem_photons_T100-150_nx200/AuAu200/C10-20/average_sp.dat")
pT_music, dN_music_100_150_brem, *rest = raw.T

#####################################
# single line plot with 120-150 proxy
#####################################

common_plotting.load_plotting_style()
plt.figure()
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-6,1e1)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]')

# SMASH
plt.plot(pT_smash[::3], dN_22[::3], ls = '-', label = r'SMASH: 2$\leftrightarrow$2 Scatterings', color = 'C2')
plt.plot(pT_smash[::3], dN_brem[::3], ls = '--', label = 'SMASH: Bremsstrahlung', color = 'C2')
plt.fill_between(pT_smash[::3], dN_22[::3] - dN_22_err[::3], dN_22[::3] + dN_22_err[::3], color = 'C2', alpha = 0.5, lw = 0)
plt.fill_between(pT_smash[::3], dN_brem[::3] - dN_brem_err[::3], dN_brem[::3] + dN_brem_err[::3], color = 'C2', alpha = 0.5, lw = 0)

# Single line proxy MUSIC HRG:
plt.plot(pT_music, dN_music_120_150_22, label = 'MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings', ls = '-', color = 'C0')
plt.plot(pT_music, dN_music_120_150_brem, label = 'MUSIC$_\mathsf{HRG}$: Bremsstrahlung', ls = '--', color = 'C0')

# MUSIC QGP:
plt.plot(pT_music, dN_music_above_Tfr, label=r"MUSIC$_\mathsf{QGP}$", color='C1', ls = ':')

plt.legend(frameon=False)
plt.tight_layout()
plt.savefig("spectra_photon_comparison_single_line_proxy.pdf")
plt.close()



##############################
# with bands, short range
##############################
common_plotting.load_plotting_style()
plt.figure()
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-6,1e1)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]')

# SMASH
plt.plot(pT_smash[::3], dN_22[::3], ls = '-', label = r'SMASH: 2$\leftrightarrow$2 Scatterings', color = 'C0')
plt.plot(pT_smash[::3], dN_brem[::3], ls = '--', label = 'SMASH: Bremsstrahlung', color = 'C1')
plt.fill_between(pT_smash[::3], dN_22[::3] - dN_22_err[::3], dN_22[::3] + dN_22_err[::3], color = 'C2', alpha = 0.5, lw = 0)
plt.fill_between(pT_smash[::3], dN_brem[::3] - dN_brem_err[::3], dN_brem[::3] + dN_brem_err[::3], color = 'C2', alpha = 0.5, lw = 0)

# short range: 120 MeV < T 150 MeV
plt.fill_between(pT_music, dN_music_140_150_22, dN_music_120_150_22, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings\n' + '120 MeV < T < 150 MeV', lw = 0)
plt.fill_between(pT_music, dN_music_140_150_brem, dN_music_120_150_brem , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung \n' + '120 MeV < T < 150 MeV', lw = 0)

# MUSIC QGP
plt.plot(pT_music, dN_music_above_Tfr, label=r"MUSIC$_\mathsf{QGP}$", color='C2', ls = ':')

plt.legend(frameon=False)
plt.tight_layout()
plt.savefig("spectra_photon_comparison_120_150MeV.pdf")
plt.close()




##############################
# with bands, long range
##############################
common_plotting.load_plotting_style()
plt.figure()
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-6,1e1)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]')

# SMASH
plt.plot(pT_smash[::3], dN_22[::3], ls = '-', label = r'SMASH: 2$\leftrightarrow$2 Scatterings', color = 'C0')
plt.plot(pT_smash[::3], dN_brem[::3], ls = '--', label = 'SMASH: Bremsstrahlung', color = 'C1')
plt.fill_between(pT_smash[::3], dN_22[::3] - dN_22_err[::3], dN_22[::3] + dN_22_err[::3], color = 'C2', alpha = 0.5, lw = 0)
plt.fill_between(pT_smash[::3], dN_brem[::3] - dN_brem_err[::3], dN_brem[::3] + dN_brem_err[::3], color = 'C2', alpha = 0.5, lw = 0)

# long range: 100 MeV < T < 150 MeV
plt.fill_between(pT_music, dN_music_140_150_22, dN_music_100_150_22, color = 'C0' , alpha=0.7, label='MUSIC$_\mathsf{HRG}$: 2$\leftrightarrow$2 Scatterings\n' + '100 MeV < T < 150 MeV', lw = 0)
plt.fill_between(pT_music, dN_music_140_150_brem, dN_music_100_150_brem , color = 'C1', alpha=0.7, label='MUSIC$_\mathsf{HRG}$: Bremsstrahlung \n' + '100 MeV < T < 150 MeV', lw = 0)

# MUSIC QGP
plt.plot(pT_music, dN_music_above_Tfr, label=r"MUSIC$_\mathsf{QGP}$", color='C2', ls = ':')


plt.legend(frameon=False)
plt.tight_layout()
plt.savefig("spectra_photon_comparison_100_150MeV.pdf")
plt.close()
