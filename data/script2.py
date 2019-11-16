import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
import scipy as sp
import scipy.interpolate
import scipy.optimize
# matplotlib.use('PDF')
def idealDiode(V,Js,Rb,n,T=300):
    k = 1.380649*10**(-23) # Дж/К
    e = 1.6*10**(-19)
    # J = 

def UfromJ(J,Js,Rb,n,T=300):
    k = 1.380649*10**(-23) # Дж/К
    e = 1.6*10**(-19)
    phiT = k*T/e
    U = n*phiT*np.log(J/Js+1)+J*Rb
    return U

# plt.rc('text', usetex = True)
# plt.rc('font', size=20, family = 'serif')
# # plt.rc('text.latex',unicode=True)
# # plt.rc('legend', fontsize=13)
# plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
import numpy as np
# import math

# Volts
volt = np.array([0,2,6,10,20,30,40,42])
# Hz
f = np.array([503.7,1241,1247,1282,1296,1296,1307,1307])*1000

# voltsTheory = UfromJ(curr,Js=0.02801/1000,Rb=2,n=1,T=300)
plt.plot(volt,f,'o')
# plt.plot(voltsTheory,curr,'ko')
plt.grid(which = 'both')
# plt.xlim((-0.2,0.5))
plt.show()