import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../..')
import common_plotting
import matplotlib.ticker

data_pT_0_1 = np.loadtxt('../../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/Photon_dNdt_pT_0_1_midy.txt', unpack = True)
data_pT_1_2 = np.loadtxt('../../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/Photon_dNdt_pT_1_2_midy.txt', unpack = True)
data_pT_2_3 = np.loadtxt('../../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/Photon_dNdt_pT_2_3_midy.txt', unpack = True)
data_pT_3_4 = np.loadtxt('../../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/Photon_dNdt_pT_3_4_midy.txt', unpack = True)
data_pT_4_inf = np.loadtxt('../../calcs/photons/smash_calcs/rhic/SMASH-2.0.1-fix/Photon_dNdt_pT_4_inf_midy.txt', unpack = True)

common_plotting.load_plotting_style()
cols = sns.color_palette("rocket", 5)

# lines
plt.plot(data_pT_0_1[0], data_pT_0_1[1], color = cols[0], label = r'p$_\mathrm{T}$ < 1 GeV')
plt.plot(data_pT_0_1[0], data_pT_0_1[3], color = cols[0], ls = '--')
plt.plot(data_pT_1_2[0], data_pT_1_2[1], color = cols[1], label = r'1 GeV $\leq$ p$_\mathrm{T}$ < 2 GeV')
plt.plot(data_pT_1_2[0], data_pT_1_2[3], color = cols[1], ls = '--')
plt.plot(data_pT_2_3[0], data_pT_2_3[1], color = cols[2], label = r'2 GeV $\leq$ p$_\mathrm{T}$ < 3 GeV')
plt.plot(data_pT_2_3[0], data_pT_2_3[3], color = cols[2], ls = '--')
plt.plot(data_pT_3_4[0], data_pT_3_4[1], color = cols[3], label = r'3 GeV $\leq$ p$_\mathrm{T}$ < 4 GeV')
plt.plot(data_pT_3_4[0], data_pT_3_4[3], color = cols[3], ls = '--')
plt.plot(data_pT_4_inf[0], data_pT_4_inf[1], color = cols[4], label = r'p$_\mathrm{T}$ $\geq$ 4 GeV')
plt.plot(data_pT_4_inf[0], data_pT_4_inf[3], color = cols[4], ls = '--')

# error bands
plt.fill_between(data_pT_0_1[0], data_pT_0_1[1] - data_pT_0_1[2], data_pT_0_1[1] + data_pT_0_1[2], alpha = 0.5, color = cols[0], lw = 0)
plt.fill_between(data_pT_0_1[0], data_pT_0_1[3] - data_pT_0_1[4], data_pT_0_1[3] + data_pT_0_1[4], alpha = 0.5, color = cols[0], lw = 0)
plt.fill_between(data_pT_1_2[0], data_pT_1_2[1] - data_pT_1_2[2], data_pT_1_2[1] + data_pT_1_2[2], alpha = 0.5, color = cols[1], lw = 0)
plt.fill_between(data_pT_1_2[0], data_pT_1_2[3] - data_pT_1_2[4], data_pT_1_2[3] + data_pT_1_2[4], alpha = 0.5, color = cols[1], lw = 0)
plt.fill_between(data_pT_2_3[0], data_pT_2_3[1] - data_pT_2_3[2], data_pT_2_3[1] + data_pT_2_3[2], alpha = 0.5, color = cols[2], lw = 0)
plt.fill_between(data_pT_2_3[0], data_pT_2_3[3] - data_pT_2_3[4], data_pT_2_3[3] + data_pT_2_3[4], alpha = 0.5, color = cols[2], lw = 0)
plt.fill_between(data_pT_3_4[0], data_pT_3_4[1] - data_pT_3_4[2], data_pT_3_4[1] + data_pT_3_4[2], alpha = 0.5, color = cols[3], lw = 0)
plt.fill_between(data_pT_3_4[0], data_pT_3_4[3] - data_pT_3_4[4], data_pT_3_4[3] + data_pT_3_4[4], alpha = 0.5, color = cols[3], lw = 0)
plt.fill_between(data_pT_4_inf[0], data_pT_4_inf[1] - data_pT_4_inf[2], data_pT_4_inf[1] + data_pT_4_inf[2], alpha = 0.5, color = cols[4], lw = 0)
plt.fill_between(data_pT_4_inf[0], data_pT_4_inf[3] - data_pT_4_inf[4], data_pT_4_inf[3] + data_pT_4_inf[4], alpha = 0.5, color = cols[4], lw = 0)

leg1 = plt.legend(loc = 'upper right', frameon=False)
# dummy entries
dum1, = plt.plot(1,50, color ='grey', label = r'2$\leftrightarrow$2 Scatterings')
dum2, = plt.plot(1,70, color ='grey', label = 'Bremsstrahlung', ls = '--')
plt.legend(handles=[dum1, dum2], loc='upper left', frameon=False)
ax = plt.gca().add_artist(leg1) # Add first legend again

plt.xlim(0,150)
plt.ylim(1e-10, 1e2)
plt.yscale('log')
plt.xlabel('t [fm]')
plt.ylabel('dN/dt [1/fm]')
plt.tight_layout()
plt.savefig('dN_dt_with_pT_cuts.pdf')
plt.close()

##################################

tot_2to2 = data_pT_0_1[1] + data_pT_1_2[1] + data_pT_2_3[1] + data_pT_3_4[1] + data_pT_4_inf[1]
tot_brems = data_pT_0_1[3] + data_pT_1_2[3] + data_pT_2_3[3] + data_pT_3_4[3] + data_pT_4_inf[3]
tot_total = tot_2to2 + tot_brems

plt.figure(figsize=(6,3))
plt.subplot(121)
plt.plot(data_pT_0_1[0], tot_2to2, label = r'2$\leftrightarrow$2 Scatterings', ls = '--')
plt.plot(data_pT_0_1[0], tot_brems, label = r'Bremsstrahlung', ls = '-.')
plt.yscale('log')
plt.legend()
plt.xlabel('t [fm]')
plt.ylabel(r'dN$_\gamma$|$_{\mathrm{y=0}}$/dt')

plt.subplot(122)
plt.plot(data_pT_0_1[0], tot_2to2/tot_total, label = r'2$\leftrightarrow$2 Scatterings', ls = '--')
plt.plot(data_pT_0_1[0], tot_brems/tot_total, label = r'Bremsstrahlung', ls = '-.')
plt.legend()
plt.xlabel('t [fm]')
plt.ylabel(r'Contribution')

plt.tight_layout()
plt.savefig('dN_dt_tot.pdf')
plt.close()

print (tot_2to2/tot_total)
print (tot_brems/tot_total)


##################################
# integrated version
bin_width = data_pT_0_1[0][1]-data_pT_0_1[0][0]
print (bin_width)

plt.figure(figsize=(6,3))
plt.subplot(121)
plt.plot(data_pT_0_1[0], bin_width * np.cumsum(tot_2to2), ls = '--', label = r'2$\leftrightarrow$2 Scatterings')
plt.plot(data_pT_0_1[0], bin_width * np.cumsum(tot_brems), ls = '-.', label = r'Bremsstrahlung')
plt.plot(data_pT_0_1[0], bin_width * (np.cumsum(tot_2to2) + np.cumsum(tot_brems)), ls = '-', label = r'Total')
# plt.yscale('log')
plt.legend()
plt.xlabel('t [fm]')
plt.ylabel(r'N$_\gamma$|$_{\mathrm{y=0}}$')
plt.xlim(0, 200)

plt.subplot(122)
plt.plot(data_pT_0_1[0], np.cumsum(tot_2to2)/np.cumsum(tot_total), ls = '--', label = r'2$\leftrightarrow$2 Scatterings')
plt.plot(data_pT_0_1[0], np.cumsum(tot_brems)/np.cumsum(tot_total), ls = '-.',  label = r'Bremsstrahlung')
#plt.plot(data_pT_0_1[0], np.cumsum(tot_total)/np.cumsum(tot_total))
plt.legend()
plt.xlabel('t [fm]')
plt.ylabel(r'Contribution')
plt.xlim(0, 200)
plt.ylim(0,1.02)

plt.tight_layout()
plt.savefig('dN_dt_tot_integrated.pdf')
plt.close()

print (np.mean(np.cumsum(tot_2to2)/np.cumsum(tot_total)))
print (np.mean(np.cumsum(tot_brems)/np.cumsum(tot_total)))
