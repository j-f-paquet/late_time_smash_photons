import numpy as np

# v2cos  v2sin
#1.47248225e-03  1.43608155e-02

#v2cos=2.53581360e-02
#v2sin=2.62764088e-02

#v2cos=2.19064046e-02
#v2sin=2.35901158e-02

v2cos=2.07149910e-02
v2sin=2.28207859e-02

psi2=np.arctan2(v2sin, v2cos)/2

print("MUSIC: ",psi2)

#print("MUSIC, protons: ", np.arctan2(2.46283365e-02, 3.87504493e-03)/2)

#print("MUSIC, pions, dN/deta: ", np.arctan2(1.57152904e-02,1.52400985e-03)/2)

# From Anna
#156.932305384 + 221.739368413j


psi2_h=np.arctan2(346.985373515, 246.777357915)/2

print("SMASH: ", psi2_h)
