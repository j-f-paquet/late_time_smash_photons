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


####################
### Plot spectra ###
####################
plt.figure()
plt.title(r"$\pi + \pi \to \rho + \gamma$")
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-12,1e-3)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$P^0 d^3{\Gamma}/d3p$ $(GeV^{-2} fm^{-4})$')


#ls from_anna_T150/PhotonRate_
#PhotonRate_2to2.txt   PhotonRate_Brems.txt

raw=np.loadtxt("from_anna_T150/PhotonRate_2to2.txt")
pT = raw[:,0]
#dN= raw[:,-2]
dN= raw[:,1]+raw[:,3] #+raw[:,15]+raw[:,17]
plt.plot(pT,dN,"-", color='brown', label="SMASH") 

#[jp401@grads-20 rate_comparison]$ ls thermal_photons/
#.git/                                              photon.cpp                                         vn_rate_hg_ideal_Chun_table_CE.dat
#a.out                                              photon.h                                           vn_rate_hg_ideal_Turbide_fit_tabulated.dat
#evolution_xyeta_eos_qcd_old_format.dat             rates.cpp                                          vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated.dat
#hadronic_rates/                                    rates.h
#partonic_rates/                                    readme

raw=np.loadtxt("thermal_photons/pi_pi_to_rho_gamma.dat")
pT = raw[:,0]
dN= raw[:,1]
plt.plot(pT,dN,"D", color='purple', label="Turbide") 

#raw=np.loadtxt("thermal_photons/vn_rate_hg_ideal_Chun_table_CE.dat")
#pT = raw[:,0]
#dN= raw[:,1]
#plt.plot(pT,dN,"--", color='red', label="Turbide - recalculated by C.Shen") 


plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("thermal_photon_pi_pi_rho_gamma_rates_vs_smash.pdf")
plt.show()


####################
### Plot spectra ###
####################
plt.figure()
plt.title(r"$\pi + \rho \to \pi + \gamma$")
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-12,1e-3)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$P^0 d^3{\Gamma}/d3p$ $(GeV^{-2} fm^{-4})$')


#ls from_anna_T150/PhotonRate_
#PhotonRate_2to2.txt   PhotonRate_Brems.txt

raw=np.loadtxt("from_anna_T150/PhotonRate_2to2.txt")
pT = raw[:,0]
#dN= raw[:,-2]
dN=raw[:,-2]-(raw[:,1]+raw[:,3]) #+raw[:,15]+raw[:,17]
plt.plot(pT,dN,"-", color='brown', label="SMASH") 

#[jp401@grads-20 rate_comparison]$ ls thermal_photons/
#.git/                                              photon.cpp                                         vn_rate_hg_ideal_Chun_table_CE.dat
#a.out                                              photon.h                                           vn_rate_hg_ideal_Turbide_fit_tabulated.dat
#evolution_xyeta_eos_qcd_old_format.dat             rates.cpp                                          vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated.dat
#hadronic_rates/                                    rates.h
#partonic_rates/                                    readme

raw=np.loadtxt("thermal_photons/pi_rho_to_pi_gamma.dat")
pT = raw[:,0]
dN= raw[:,1]
plt.plot(pT,dN,"D", color='purple', label="Turbide") 

#raw=np.loadtxt("thermal_photons/vn_rate_hg_ideal_Chun_table_CE.dat")
#pT = raw[:,0]
#dN= raw[:,1]
#plt.plot(pT,dN,"--", color='red', label="Turbide - recalculated by C.Shen") 


plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("thermal_photon_pi_rho_pi_gamma_rates_vs_smash.pdf")
plt.show()


####################
### Plot spectra ###
####################

def fit_brem(p,T):

    a=-16.28+62.45*T-93.4*T*T-7.5*T*T*T
    b=-35.54+414.8*T-2054*T*T+3718.8*T*T*T
    g=0.7364-10.72*T+56.32*T*T-103.5*T*T*T
    d=-2.51+58.152*T-318.24*T*T+610.7*T*T*T

    return np.exp(a+b*p+g*p*p+d/(p+0.2))



plt.figure()
plt.title(r"$\pi + \pi \to \pi + \pi + \gamma$")
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-12,1e-3)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$P^0 d^3{\Gamma}/d3p$ $(GeV^{-2} fm^{-4})$')


#ls from_anna_T150/PhotonRate_
#PhotonRate_2to2.txt   PhotonRate_Brems.txt

raw=np.loadtxt("from_anna_T150/PhotonRate_Brems.txt")
pT = raw[:,0]
dN= raw[:,-2]
plt.plot(pT,dN,"-", color='brown', label="SMASH") 

raw=np.loadtxt("thermal_photons/pion_brem_rapp.dat")
pT = raw[:,0]
dN= raw[:,1]
plt.plot(pT,dN,"D", color='purple', label="Rapp") 

#dN_fit=fit_brem(pT, .15)
#plt.plot(pT,dN_fit,"D", color='blue', label="Rapp fit") 

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("thermal_photon_pi_pi_brem_rates_vs_smash.pdf")
plt.show()








######################################
############ Total rate ##############
######################################

raw=np.loadtxt("from_anna_T150/PhotonRate_Brems.txt")
pT_brem = raw[:,0]
dN_brem = raw[:,-2]
dN_brem[dN_brem < 1e-100] = 1e-100
pre_interp_brem = scipy.interpolate.interp1d(pT_brem, np.log(dN_brem), kind='linear')
interp_brem=lambda x: np.exp(pre_interp_brem(x))

raw=np.loadtxt("from_anna_T150/PhotonRate_2to2.txt")
pT_22 = raw[:,0]
dN_22=raw[:,-2]-(raw[:,1]+raw[:,3])
dN_22[dN_22<1e-100]=1e-100
pre_interp_22 = scipy.interpolate.interp1d(pT_22, np.log(dN_22), kind='linear')
interp_22 = lambda x: np.exp(pre_interp_22(x))

raw=np.loadtxt("thermal_photons/total_hadronic_rate_for_test.dat")
pT_jf = raw[:,0]
dN_jf = raw[:,1]
#interp_jf = scipy.interpolate.interp1d(pT_jf, np.log(dN_jf), kind='linear')

plt.figure()
plt.title("Total hadronic rate comparison")
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,4)
plt.ylim(1e-15,1e-3)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'$P^0 d^3{\Gamma}/d3p$ $(GeV^{-2} fm^{-4})$')

plt.plot(pT_jf,interp_brem(pT_jf)+interp_22(pT_jf),"-", color='brown', label="SMASH, total") 
plt.plot(pT_brem, dN_brem,"-.", color='red', label="SMASH, brem.") 
plt.plot(pT_22, dN_22,":", color='green', label=r"SMASH, $2\to 2$") 
plt.plot(pT_jf,dN_jf,"D", color='purple', label="\"Hydro\",total") 

plt.legend(loc='upper right', fontsize=14)
plt.tight_layout()
plt.savefig("thermal_photon_total_rate_used_for_comparison_hydro_vs_smash.pdf")
plt.show()



plt.figure()
plt.title("Total hadronic rate comparison")
plt.xscale('linear')
plt.yscale('linear')
plt.xlim(0,4)
plt.ylim(0.5,2.0)
plt.xlabel(r'$p_T$ $(GeV)$')
plt.ylabel(r'Ratio of rates')

plt.plot(pT_jf,dN_jf/(interp_brem(pT_jf)+interp_22(pT_jf)),"-", color='black', label="JF/SMASH") 

plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("ratio_thermal_photon_total_rate_used_for_comparison_hydro_vs_smash.pdf")
plt.show()
