import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter
import matplotlib.ticker as mtick
import os.path
import scipy.interpolate
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..')
import common_plotting
import matplotlib.gridspec as gridspec


# RHIC
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/SP_v2_photons_total.txt")
pT_smash_rhic, v2_tot_rhic, v2_tot_err_rhic = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/SP_v2_photons_2to2.txt")
pT_smash_22_rhic, v2_22_rhic, v2_err_22_rhic = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/SP_v2_photons_Brems.txt")
pT_smash_brem_rhic, v2_brem_rhic, v2_err_brem_rhic = raw.T

# LHC
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/SP_v2_photons_total.txt")
pT_smash_lhc, v2_tot_lhc, v2_tot_err_lhc = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/SP_v2_photons_2to2.txt")
pT_smash_22_lhc, v2_22_lhc, v2_err_22_lhc = raw.T
raw=np.loadtxt("../calcs/photons/smash_calcs/lhc/SMASH-2.0.1-fix/SP_v2_photons_Brems.txt")
pT_smash_brem_lhc, v2_brem_lhc, v2_err_brem_lhc = raw.T





common_plotting.load_plotting_style_paper()
plt.figure(figsize=(10*0.8, 4.5*0.8))
gs = gridspec.GridSpec(1,8)

# RHIC:
plt.subplot(gs[: , :4])
plt.xscale('linear')
plt.xlim(0,3)
plt.ylim(-2,22)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.ylabel(r'v$_2$ [%]', fontsize = 13)

# SMASH
# plt.plot(pT_smash_22_rhic[::3], 100.0*v2_22_rhic[::3], label = '2$\leftrightarrow$2 Scatterings', ls = '--', color = 'C2')
# plt.plot(pT_smash_brem_rhic[::3], 100.0*v2_brem_rhic[::3], label = 'Bremsstrahlung', ls = ':', color = 'C1')
# plt.plot(pT_smash_rhic[::3], 100.0*v2_tot_rhic[::3], ls = '-', label = 'Total', color = 'C0')
plt.plot(pT_smash_22_rhic, 100.0*v2_22_rhic, label = '2$\leftrightarrow$2 Scatterings', ls = '--', color = 'C2')
plt.plot(pT_smash_brem_rhic, 100.0*v2_brem_rhic, label = 'Bremsstrahlung', ls = ':', color = 'C1')
plt.plot(pT_smash_rhic, 100.0*v2_tot_rhic, ls = '-', label = 'Total', color = 'C0')
# plt.fill_between(pT_smash_22_rhic[::3], v2_22_rhic[::3] * 100.0 - v2_err_22_rhic[::3] * 100.0, v2_22_rhic[::3] * 100.0 + v2_err_22_rhic[::3] * 100.0, alpha = 0.5, color = 'C2', lw = 0)
# plt.fill_between(pT_smash_brem_rhic[::3], v2_brem_rhic[::3] * 100.0 - v2_err_brem_rhic[::3] * 100.0, v2_brem_rhic[::3] * 100.0 + v2_err_brem_rhic[::3] * 100.0, alpha = 0.5, color = 'C1', lw = 0)
# plt.fill_between(pT_smash_rhic[::3], v2_tot_rhic[::3] * 100.0 - v2_tot_err_rhic[::3] * 100.0, v2_tot_rhic[::3] * 100.0 + v2_tot_err_rhic[::3] * 100.0, alpha = 0.5, color = 'C0', lw = 0)
plt.fill_between(pT_smash_22_rhic, v2_22_rhic * 100.0 - v2_err_22_rhic * 100.0, v2_22_rhic * 100.0 + v2_err_22_rhic * 100.0, alpha = 0.5, color = 'C2', lw = 0)
plt.fill_between(pT_smash_brem_rhic, v2_brem_rhic * 100.0 - v2_err_brem_rhic * 100.0, v2_brem_rhic * 100.0 + v2_err_brem_rhic * 100.0, alpha = 0.5, color = 'C1', lw = 0)
plt.fill_between(pT_smash_rhic, v2_tot_rhic * 100.0 - v2_tot_err_rhic * 100.0, v2_tot_rhic * 100.0 + v2_tot_err_rhic * 100.0, alpha = 0.5, color = 'C0', lw = 0)


plt.legend(frameon=False, loc = 'upper left')
plt.figtext(0.235, 0.205, '     Au + Au\n' + r'$\mathbf{\sqrt{s}}$ = 200 GeV', fontweight = 'bold')
plt.xticks([0,1,2,3])



# LHC
plt.subplot(gs[: , 4:])
plt.xscale('linear')
plt.xlim(0,3)
plt.ylim(-2,22)
plt.xlabel(r'p$_\mathsf{T}$ [GeV]')
plt.yticks([])
plt.minorticks_off()

# SMASH
plt.plot(pT_smash_22_lhc, 100.0*v2_22_lhc, label = 'SMASH: 2to2', ls = '--', color = 'C2')
plt.plot(pT_smash_brem_lhc, 100.0*v2_brem_lhc, label = 'SMASH: Brems', ls = ':', color = 'C1')
plt.plot(pT_smash_lhc, 100.0*v2_tot_lhc, ls = '-', label = 'SMASH: Tot', color = 'C0')
plt.fill_between(pT_smash_22_lhc, v2_22_lhc * 100.0 - v2_err_22_lhc * 100.0, v2_22_lhc * 100.0 + v2_err_22_lhc * 100.0, alpha = 0.5, color = 'C2', lw = 0)
plt.fill_between(pT_smash_brem_lhc, v2_brem_lhc * 100.0 - v2_err_brem_lhc * 100.0, v2_brem_lhc * 100.0 + v2_err_brem_lhc * 100.0, alpha = 0.5, color = 'C1', lw = 0)
plt.fill_between(pT_smash_lhc, v2_tot_lhc * 100.0 - v2_tot_err_lhc * 100.0, v2_tot_lhc * 100.0 + v2_tot_err_lhc * 100.0, alpha = 0.5, color = 'C0', lw = 0)
# plt.plot(pT_smash_22_lhc[::3], 100.0*v2_22_lhc[::3], label = 'SMASH: 2to2', ls = '--', color = 'C2')
# plt.plot(pT_smash_brem_lhc[::3], 100.0*v2_brem_lhc[::3], label = 'SMASH: Brems', ls = ':', color = 'C1')
# plt.plot(pT_smash_lhc[::3], 100.0*v2_tot_lhc[::3], ls = '-', label = 'SMASH: Tot', color = 'C0')
# plt.fill_between(pT_smash_22_lhc[::3], v2_22_lhc[::3] * 100.0 - v2_err_22_lhc[::3] * 100.0, v2_22_lhc[::3] * 100.0 + v2_err_22_lhc[::3] * 100.0, alpha = 0.5, color = 'C2', lw = 0)
# plt.fill_between(pT_smash_brem_lhc[::3], v2_brem_lhc[::3] * 100.0 - v2_err_brem_lhc[::3] * 100.0, v2_brem_lhc[::3] * 100.0 + v2_err_brem_lhc[::3] * 100.0, alpha = 0.5, color = 'C1', lw = 0)
# plt.fill_between(pT_smash_lhc[::3], v2_tot_lhc[::3] * 100.0 - v2_tot_err_lhc[::3] * 100.0, v2_tot_lhc[::3] * 100.0 + v2_tot_err_lhc[::3] * 100.0, alpha = 0.5, color = 'C0', lw = 0)


# plt.legend(frameon=False, loc = 'upper left')
plt.figtext(0.68, 0.205, '      Pb + Pb\n' + r' $\mathbf{\sqrt{s}}$ = 2.76 TeV', fontweight = 'bold')
plt.xticks([0,1,2,3])

plt.figtext(0.862, 0.965, "SMASH-2.0.1-1-g397f8f0", color = "gray", fontsize = 5.3)
plt.tight_layout(w_pad=-0.05)
plt.savefig("v2_SMASH.pdf")
plt.close()
