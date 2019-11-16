import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit

def getC(fr):
    L = 364e-6 #Гн
    C2 = 37.9e-9
    Cd = 1/(4*np.pi**2 * L * fr**2) - C2
    return Cd

plt.rc('text', usetex = True)
plt.rc('font', size=20, family = 'serif')
plt.rc('text.latex',unicode=True)
# plt.rc('legend', fontsize=13)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
import numpy as np

# Volts BACK
volt = -np.array([0,2,6,10,20,30,40,42])

# f, Hz
f = np.array([503.7,1241,1274,1282,1296,1296,1307,1307])*1000

# curr_t = np.linspace(0,100/1000,200)

print(getC(1))
# popt, pcov = curve_fit(UfromJ,curr1,volt1,p0 = [10**(-4),2,2]) 
# popt, pcov = curve_fit(UfromJ,curr1,volt1,p0 = [10**(-4),7,1],bounds = ([0.028001*10**(-3),0,0],[np.inf,np.inf,np.inf])) 
# perr = np.sqrt(np.diag(pcov))
# voltsTheory = UfromJ(curr_t,Js=popt[0],Rb=popt[1],n=popt[2])
# print('Approximation Done:\nJs = {} Amps\nRb = {} Ohm\nn = {}'.format(popt[0],popt[1],popt[2]))
# print(perr)
#
# plt.figure(figsize = (10,7))
# plt.plot(voltsTheory,curr_t*1000,'k-',label = 'Approximation')
# plt.plot(volt1,curr1*1000,'ro',label = 'Experiment')
# plt.legend()
# plt.grid(which = 'both')
# plt.xlabel(r'$U, V$')
# plt.ylabel(r'$J, mA$')
# plt.savefig('imgs/vah1str.png',dpi=500)

plt.show()

