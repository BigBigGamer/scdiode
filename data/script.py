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
volt = np.array([0,0.2,0.26,0.3,0.34,0.36,0.38,0.4,0.44,-2,-10,-20,-30,-40,-50,-60,-70,-80,-90,-100])
# Aps
curr = np.array([0,1,8,14,28,38,54,74,100,-0.02,-0.022,-0.022,-0.024,-0.024,-0.025,-0.026,-0.026,-0.027,-0.028,-0.028]) / 1000

voltsTheory = UfromJ(curr,Js=0.02801/1000,Rb=2,n=1,T=300)
plt.plot(volt,curr,'o')
# plt.plot(voltsTheory,curr,'ko')
plt.grid(which = 'both')
plt.xlim((-0.2,0.5))
plt.show()

# fig = plt.figure(figsize = (14,7))
# ax = fig.add_subplot(111)


# ax.plot(curr,high_2_pos,'ro-',label = 'Верхнее, I+')
# ax.plot(curr,high_2_neg,'ko-',label = 'Верхнее, I-')
# ax.plot(curr,low_2_pos,'rs--',label = 'Нижнее, I+')
# ax.plot(curr,low_2_neg,'ks--',label = 'Нижнее, I-')
# # x_interpol = np.arange(0,70,0.05)
# # Interpol = sp.interpolate.CubicSpline(lnew,sqvnew,extrapolate = False)
# # ax.plot(x_interpol,Interpol(x_interpol),'r-')
# # ax.set_xticks(range(0,70,3),minor = True)
# # ax.set_yticks(range(46,52,1),minor = True)
# ax.grid(which = 'both')
# plt.legend()
# plt.title(r'1-я обмотка')
# plt.xlabel(r'I, a.u.',fontsize = 25)
# # plt.ylabel(r'$|E|^2$, $\mu V$')

# plt.show()
# fig.savefig('imgs/graphs/phaser1.png',dpi=500)
