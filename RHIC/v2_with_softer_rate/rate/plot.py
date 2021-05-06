import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

pT_orig, dN_orig, *rest = np.loadtxt("./vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated.dat").T
pT_mod, dN_mod, *rest = np.loadtxt("./vn_rate_hg_pion_brem_ideal_Rapp_fit_tabulated_normalized_to_smash.dat").T
pT_smash, dN_smash, dN_err_smash = np.loadtxt("./smash.dat").T

###########################################################################
########################## Plotting calculations ##########################
###########################################################################

font = {'family' : 'URW Gothic',
        'weight' : 'bold',
        'size'   : 20}

plt.rc('font', **font)

plt.figure()
#plt.subplot(gs[:7 , :])
plt.xscale('linear')
plt.yscale('log')
plt.xlim(0,3)
plt.ylim(1e-14,1e-2)
plt.xlabel(r'E (GeV)')
plt.ylabel(r"E $\frac{\mathrm{dR}}{\mathrm{d}^{3}\mathrm{p}}$ [GeV$^{-2}$ fm$^{-4}$]")

plt.errorbar(pT_smash,dN_smash,yerr=dN_err_smash, fmt='D', markersize=1, label="SMASH rate") 

plt.plot(pT_orig, dN_orig, 'r:', label='Bremsstrahlung')
plt.plot(pT_mod, dN_mod, 'black',linestyle='-', label='Softer bremsstrahlung')

plt.legend(loc='upper right',fontsize=13)
plt.tight_layout()
plt.savefig("rate_modified_to_mimic_smash.pdf")
plt.show()

