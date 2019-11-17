import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit

def getC(fr):
    L = 364e-6 #Гн
    C2 = 37.9e-12
    Cd = 1/(4*np.pi**2 * L * fr**2) - C2
    return Cd

plt.rc('text', usetex = True)
plt.rc('font', size=20, family = 'serif')
plt.rc('text.latex',unicode=True)
# plt.rc('legend', fontsize=13)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
import numpy as np

# Volts BACK
# volt = np.array([0,2,6,10,20,30,40,42])
volt = np.array([2,6,10,20,30,40,42])

# f, Hz
# f = np.array([503.7,1241,1274,1282,1296,1296,1307,1307],dtype=np.int64)*1000
f = np.array([1241,1274,1282,1296,1299,1307,1307],dtype=np.int64)*1000
C = getC(f)*1e12 
fc = 1/C**2

z = np.polyfit(volt,fc,1)
print(z)
p = np.poly1d(z)
vt = np.linspace(-9,42,50)
plt.figure(figsize = (10,7))
plt.plot(vt,p(vt),'k-',label = 'Approximation')
plt.plot(volt,fc,'ro',label = 'Experiment')
# plt.legend()
plt.grid(which = 'both')
plt.xlabel(r'$U_{rev}, V$')
plt.ylabel(r'$1/C^2, 1/pF^2$')
plt.vlines(x=0,ymin=-1,ymax=1,color = 'k',lw=1)
plt.hlines(y=0,xmin=-10,xmax=42,color = 'k',lw=1)
plt.ylim(-0.025,0.15)
plt.xlim(-10,43)
# plt.savefig('imgs/vfh.png',dpi=500)

plt.show()

