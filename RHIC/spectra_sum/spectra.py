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
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting

######################################
############ Total rate ##############
######################################

# SMASH
raw=np.loadtxt("../../calcs/photons/smash_calcs/rhic/pT_photons_midy.txt")
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

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/results/photons_above_Tfr_nx200/AuAu200/C10-20/average_sp.dat")
pT_above, dN_music_above, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/combined/average_sp_smash_tot.dat")
pT_above_plus_smash, dN_music_above_plus_smash, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T140-150.dat")
pT_above_plus_hydro140, dN_music_above_plus_hydro140, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T120-150.dat")
pT_above_plus_hydro120, dN_music_above_plus_hydro120, *rest = raw.T

raw=np.loadtxt("../../calcs/photons/averaged_hydro_calcs/combined/average_sp_hydro_tot_T100-150.dat")
pT_above_plus_hydro100, dN_music_above_plus_hydro100, *rest = raw.T


# Interpolation for ratio
music_above_interpolation = scipy.interpolate.interp1d(pT_above, np.log(dN_music_above), kind='linear')
music_above_rebin_smash = np.exp(music_above_interpolation(pT_above_plus_smash[1:14]))
music_above_rebin_music100 = np.exp(music_above_interpolation(pT_above_plus_hydro100[:14]))
music_above_rebin_music140 = np.exp(music_above_interpolation(pT_above_plus_hydro140[:14]))
music_above_rebin_music120 = np.exp(music_above_interpolation(pT_above_plus_hydro120[:14]))
music_above_rebin_music120150 = np.exp(music_above_interpolation(pT_above_plus_hydro120[:15]))


####################################
# Ration plot with single line proxy
####################################

gs = gridspec.GridSpec(10,1)

common_plotting.load_plotting_style()
plt.subplot(gs[:7 , :])
plt.xscale('linear')
plt.yscale('log')
plt.xticks([])
plt.xlim(0,2.5)
plt.ylim(8e-4,1e1)
plt.ylabel(r'1/(2$\pi$p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]      ', fontsize=14)

plt.plot(pT_above, dN_music_above, label=r"MUSIC$_\mathsf{QGP}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_hydro120, dN_music_above_plus_hydro120, ls = '-', label = 'MUSIC$_\mathsf{QGP}$ + MUSIC$_\mathsf{HRG}$', color = 'C0')
plt.plot(pT_above_plus_smash, dN_music_above_plus_smash, ls = '--', label='MUSIC$_\mathsf{QGP}$ + ' + 'SMASH', color = 'C2')
plt.legend(frameon=False)

plt.subplot(gs[7:, :])
plt.xlim(0,2.5)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')

plt.plot(pT_above_plus_hydro120[:15], dN_music_above_plus_hydro120[:15] / music_above_rebin_music120150, label = '(MUSIC$_\mathsf{QGP}$+ MUSIC$_\mathsf{HRG}$) / MUSIC$_\mathsf{QGP}$', ls = '-', color = 'C0')
plt.plot(pT_above_plus_smash[1:14], dN_music_above_plus_smash[1:14] / music_above_rebin_smash, label = '(MUSIC$_\mathsf{QGP}$ + SMASH) / MUSIC$_\mathsf{QGP}$', ls = '--', color = 'C2')
plt.axhline(1.0, ls = ':', color = 'C1')

plt.legend(frameon=False)
plt.tight_layout(h_pad=-0.2)
plt.savefig("spectra_photon_sum_single_line_proxy.pdf")
plt.close()


####################################
# Ration plot 100 < T < 150
####################################

gs = gridspec.GridSpec(10,1)

common_plotting.load_plotting_style()
plt.subplot(gs[:7 , :])
plt.xscale('linear')
plt.yscale('log')
plt.xticks([])
plt.xlim(0,2.5)
plt.ylim(8e-4,1e1)
plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]       ', fontsize = 14)

plt.plot(pT_above, dN_music_above, label=r"MUSIC$_\mathsf{QGP}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash, dN_music_above_plus_smash, ls = '--', label='MUSIC$_\mathsf{QGP}$ + ' + 'SMASH', color = 'C2')
plt.fill_between(pT_above_plus_hydro100, dN_music_above_plus_hydro140, dN_music_above_plus_hydro100, alpha = 0.8, label = 'MUSIC$_\mathsf{QGP}$ + MUSIC$_\mathsf{HRG}$\n' + '100 MeV < T < 150 MeV', lw = 0, color='C0')
plt.legend(frameon=False)

plt.subplot(gs[7:, :])
plt.xlim(0,2.5)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')

plt.plot(pT_above_plus_smash[1:14], dN_music_above_plus_smash[1:14] / music_above_rebin_smash, label = '(MUSIC$_\mathsf{QGP}$ + SMASH) / MUSIC$_\mathsf{QGP}$', ls = '--', color = 'C2')
plt.axhline(1.0, ls = ':', color = 'C1')
plt.fill_between(pT_above_plus_hydro100[:14], dN_music_above_plus_hydro100[:14] / music_above_rebin_music100, dN_music_above_plus_hydro140[:14] / music_above_rebin_music140, label = '(MUSIC$_\mathsf{QGP}$+ MUSIC$_\mathsf{HRG}$) / MUSIC$_\mathsf{QGP}$', alpha = 0.8, color = 'C0', lw = 0)

plt.legend(frameon=False)
plt.tight_layout(h_pad=-0.2)
plt.savefig("spectra_photon_sum_long_range.pdf")
plt.close()


####################################
# Ration plot 100 < T < 150
####################################

gs = gridspec.GridSpec(10,1)

common_plotting.load_plotting_style()
plt.subplot(gs[:7 , :])
plt.xscale('linear')
plt.yscale('log')
plt.xticks([])
plt.xlim(0,2.5)
plt.ylim(8e-4,1e1)
plt.ylabel(r'1/(2$\pi$ p$_\mathrm{T}$) dN$_\gamma$/dp$_\mathrm{T} |_{y =0}$ [Gev$^{-2}$]       ', fontsize = 14)

plt.plot(pT_above, dN_music_above, label=r"MUSIC$_\mathsf{QGP}$", ls = ':', color = 'C1')
plt.plot(pT_above_plus_smash, dN_music_above_plus_smash, ls = '--', label='MUSIC$_\mathsf{QGP}$ + ' + 'SMASH', color = 'C2')
plt.fill_between(pT_above_plus_hydro120, dN_music_above_plus_hydro140, dN_music_above_plus_hydro120, alpha = 0.8, label = 'MUSIC$_\mathsf{QGP}$ + MUSIC$_\mathsf{HRG}$\n' + '120 MeV < T < 150 MeV', lw = 0, color='C0')
plt.legend(fontsize=10, frameon=False)

plt.subplot(gs[7:, :])
plt.xlim(0,2.5)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')

plt.plot(pT_above_plus_smash[1:14], dN_music_above_plus_smash[1:14] / music_above_rebin_smash, label = '(MUSIC$_\mathsf{QGP}$ + SMASH) / MUSIC$_\mathsf{QGP}$', ls = '--', color = 'C2')
plt.axhline(1.0, ls = ':', color = 'C1')
plt.fill_between(pT_above_plus_hydro120[:14], dN_music_above_plus_hydro120[:14] / music_above_rebin_music120, dN_music_above_plus_hydro140[:14] / music_above_rebin_music140, label = '(MUSIC$_\mathsf{QGP}$+ MUSIC$_\mathsf{HRG}$) / MUSIC$_\mathsf{QGP}$', alpha = 0.8, color = 'C0', lw = 0)

plt.legend(frameon=False)
plt.tight_layout(h_pad=-0.2)
plt.savefig("spectra_photon_sum_short_range.pdf")
plt.close()
