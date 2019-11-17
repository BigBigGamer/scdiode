import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit
# matplotlib.use('PDF')
def idealDiode(V,Js,n,T=300):
    k = 1.380649*10**(-23) # Дж/К
    e = 1.6*10**(-19)
    phiT = k*T/e
    J = Js*(np.exp(V/phiT) - 1)
    return J

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
# import math

# Volts
volt = np.array([0,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44,-2,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100])
volt1 = np.array([0,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44])
volt2 = np.array([-2,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100])
# volt = np.abs(volt)
# Aps
curr = np.array([0,1,8,14,28,38,54,74,100,-0.02,-0.022,-0.022,-0.024,-0.024,-0.025,-0.026,-0.026,-0.027,-0.028,-0.028]) / 1000
curr1 = np.array([0,1,8,14,28,38,54,74,100]) / 1000
curr2 = np.array([-0.02,-0.022,-0.022,-0.024,-0.024,-0.025,-0.026,-0.026,-0.027,-0.028,-0.028]) / 1000
# curr = np.abs(curr)
# curr_t = np.linspace(0,100/1000,200)
curr_t = np.logspace(-10,-1,300)


popt, pcov = curve_fit(UfromJ,curr1,volt1,p0 = [10**(-4),2,2]) 
# popt, pcov = curve_fit(UfromJ,curr1,volt1,p0 = [10**(-4),7,1],bounds = ([0.028001*10**(-3),0,0],[np.inf,np.inf,np.inf])) 
perr = np.sqrt(np.diag(pcov))
voltsTheory = UfromJ(curr_t,Js=popt[0],Rb=popt[1],n=popt[2])
print('Approximation Done:\nJs = {} Amps\nRb = {} Ohm\nn = {}'.format(popt[0],popt[1],popt[2]))
print(perr)


# popt2, pcov2 = curve_fit(UfromJ,curr2,volt2,p0 = [10**(-4),7,1],bounds = ([0.028001*10**(-3),0,0],[np.inf,np.inf,np.inf])) 
# popt2, pcov2 = curve_fit(idealDiode,volt,curr,p0 = [10**(-4),1],maxfev=2000) 
# perr2 = np.sqrt(np.diag(pcov2))
# currTheory2 = idealDiode(volt,Js=popt2[0],n=popt2[1])
# print('Approximation 2 Done:\nJs = {} Amps\nn = {}'.format(popt2[0],popt2[1]))
# print(perr2)


plt.figure(figsize = (10,7))
plt.plot(voltsTheory*100,curr_t*1000,'k-',label = 'Approximation')
plt.plot(volt1*100,curr1*1000,'ro',label = 'Experiment')
plt.plot(volt2,abs(curr2*1000),'ro')

# ticks = np.append( np.arange(-100,0,step = 20),np.arange(0,1,step = 0.2))
ticks = [-100,-80,-60,-40,-20,0,20,40]
labels = ('-100','-80','-60','-40','-20','0','0.2','0.4')
plt.xticks(ticks,labels)
plt.legend()
plt.grid(which = 'both')
plt.yscale('log')
plt.ylim((10**(-3),2*10**(2)))
plt.xlabel(r'$U, V$')
plt.ylabel(r'$|J|, mA$')
# plt.savefig('imgs/vah1log.png',dpi=500)

# plt.figure(figsize = (7,7))
# plt.plot(volt,currTheory2*1000,'k-',label = 'Approximation')
# plt.plot(volt,curr*1000,'ro',label = 'Experiment')

plt.show()

