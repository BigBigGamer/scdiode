import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit

def UfromJ(J,Js,Rb,n,T=300):
    k = 1.380649*10**(-23) # Дж/К
    e = 1.6*10**(-19)
    phiT = k*T/e
    # print(J,Js)
    U = n*phiT*np.log(J/Js+1)+J*Rb
    return U

plt.rc('text', usetex = True)
plt.rc('font', size=20, family = 'serif')
plt.rc('text.latex',unicode=True)
# plt.rc('legend', fontsize=13)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
import numpy as np

volt01 = np.array([0,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44])
# Aps
curr01 = np.array([0,1,8,14,28,38,54,74,100]) / 1000


# Volts
volt1 = np.array([0,0.1,0.2,0.3,0.36,0.38,0.4,0.42])

# Aps
curr1 = np.array([0,0,4,20,38,64,76,100]) / 1000

curr_t = np.linspace(0,100/1000,200)

popt, pcov = curve_fit(UfromJ,curr1,volt1,p0 = [10**(-4),2,2]) 
# popt, pcov = curve_fit(UfromJ,curr1,volt1,p0 = [10**(-4),7,1],bounds = ([0.028001*10**(-3),0,0],[np.inf,np.inf,np.inf])) 
perr = np.sqrt(np.diag(pcov))
voltsTheory = UfromJ(curr_t,Js=popt[0],Rb=popt[1],n=popt[2])
print('Approximation Done:\nJs = {} Amps\nRb = {} Ohm\nn = {}'.format(popt[0],popt[1],popt[2]))
print(perr)

plt.figure(figsize = (10,7))
plt.plot(voltsTheory,curr_t*1000,'k-',label = 'Approximation, T = 340K')
plt.plot(volt1,curr1*1000,'ro',label = 'Experiment, T = 340K')
plt.plot(volt01,curr01*1000,'bs',label = 'Experiment, T = 298K')
plt.legend()
plt.grid(which = 'both')
plt.xlabel(r'$U, V$')
plt.ylabel(r'$J, mA$')
# plt.savefig('imgs/vah12str.png',dpi=500)

plt.show()

