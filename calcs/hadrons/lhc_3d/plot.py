import numpy as np
import matplotlib as mpl
#mpl.use('Agg')
import matplotlib.pyplot as plt


###########################################################################
########################## Plotting calculations ##########################
###########################################################################

font = {'family' : 'URW Gothic',
        'weight' : 'bold',
        'size'   : 16}

plt.rc('font', **font)
#
#legend_params={
#'framealpha' : 1,
#'fontsize':14, 
#'handletextpad':0.3, 
#'labelspacing':0.1, 
#'borderaxespad':0.1
#}
#
#plt.rc('legend', **legend_params)

######################################
############ Total rate ##############
######################################


raw=np.loadtxt("../../hadronic_data/lhc/spectra_pis_PbPb_2760_1020_ALICE2013.dat")
pT_alice, dNdpT_alice, *rest = raw.T

raw=np.loadtxt("outputs/Fvnpt--211_y_-0.5_0.5.dat")
pT_calc, dNdpT_calc, v1cos_calc, v1sin_calc, v2cos_calc, v2sin_calc, *rest = raw.T

plt.figure()
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
#plt.ylim(1e-9,1e2)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$P^0 d^3{N_\pi}/d3p$ $(GeV^{-2})$')

#plt.text(0.2, 0.9, 'Points: SMASH\nLight bands:    Hydro, 100<T<150 MeV\nDarker bands: Hydro, 120<T<150 MeV', horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=14)

plt.errorbar(x=pT_alice, y=dNdpT_alice, fmt='D', color='red', label="ALICE") 

plt.plot(pT_calc, dNdpT_calc,"-", color='black', label=r"Hydro") 

plt.legend(loc='lower left', fontsize=10)
plt.tight_layout()
plt.savefig("pion_dNdpT_hydro_alice.pdf")
plt.show()



raw=np.loadtxt("../../hadronic_data/lhc/v2_ch_hadrons_PbPb_5020_1020_ALICE.dat")
pT_alice, dummy, dummy, v2_alice, *rest = raw.T

raw=np.loadtxt("outputs/vnchpT_eta_-0.5_0.5.dat")
pT_calc_ch, dNdpT_calc_ch, v1cos_calc_ch, v1sin_calc_ch, v2cos_calc_ch, v2sin_calc_ch, *rest = raw.T

plt.figure()
plt.xscale('linear')
#plt.yscale('log')
plt.xlim(0,1)
#plt.ylim(1e-9,1e2)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$v_2$')

#plt.text(0.2, 0.9, 'Points: SMASH\nLight bands:    Hydro, 100<T<150 MeV\nDarker bands: Hydro, 120<T<150 MeV', horizontalalignment='left', verticalalignment='center', transform=plt.axes().transAxes, fontsize=14)

plt.errorbar(x=pT_alice, y=v2_alice, fmt='D', color='red', label="ALICE, v_2{4}, charged, sqrts=5020 GeV") 

plt.plot(pT_calc, np.sqrt(v2cos_calc**2+v2sin_calc**2) ,"-", color='black', label=r"Hydro, v_2{2}, pion, sqrts=2760 GeV") 
plt.plot(pT_calc_ch, np.sqrt(v2cos_calc_ch**2+v2sin_calc_ch**2) ,":", color='blue', label=r"Hydro, v_2{2}, ch, sqrts=2760 GeV") 

plt.legend(loc='upper left', fontsize=10)
plt.tight_layout()
plt.savefig("v2_rough_hydro_alice.pdf")
plt.show()

