import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
import scipy as sp
import scipy.interpolate
import scipy.optimize
# matplotlib.use('PDF')

plt.rc('text', usetex = True)
plt.rc('font', size=20, family = 'serif')
# plt.rc('text.latex',unicode=True)
# plt.rc('legend', fontsize=13)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
import numpy as np
import math

curr = [0,1,2,3,4,5,6,7,8,9,10]
high_1_pos = [460,450,420,370,285,150,20,45,240,420,float('nan')]
high_1_neg = [460,460,445,390,310,190,40,35,230,410,float('nan')]

high_2_pos = [260,270,290,310,340,380,420,440,410,370,330]
high_2_neg = [260,280,290,310,345,380,430,445,410,370,330]
high_12_pos = [330,330,320,300,280,230,210,150,float('nan'),float('nan'),float('nan')]
high_12_neg = [330,320,320,310,300,260,240,160,float('nan'),float('nan'),float('nan')]

low_1_pos = [110,110,130,170,240,320,410,440,390,300,190]
low_1_neg = [110,120,150,200,260,340,410,440,390,300,190]
low_2_pos = [240,230,210,180,130,50,10,30,190,360,450]
low_2_neg = [240,230,210,170,130,50,10,40,200,370,460]
low_12_pos = [250,260,300,360,415,460,445,460,float('nan'),float('nan'),float('nan')]
low_12_neg = [250,240,270,320,370,420,415,440,float('nan'),float('nan'),float('nan')]

a1h = 4 
a1l = 6 
a2h = 6 
a2l = 3.5
a12h = 6
a12l = 3.5 
high_1_pos = 10**(a1h/10)*np.array(high_1_pos)
high_1_neg = 10**(a1h/10)*np.array(high_1_neg)

high_2_pos = 10**(a2h/10)*np.array(high_2_pos)
high_2_neg = 10**(a2h/10)*np.array(high_2_neg)

low_1_pos = 10**(a1l/10)*np.array(low_1_pos)
low_1_neg = 10**(a1l/10)*np.array(low_1_neg)

low_2_pos = 10**(a2l/10)*np.array(low_2_pos)
low_2_neg = 10**(a2l/10)*np.array(low_2_neg)

high_12_pos = 10**(a12h/10)*np.array(high_12_pos)
high_12_neg = 10**(a12h/10)*np.array(high_12_neg)

low_12_pos = 10**(a12l/10)*np.array(low_12_pos)
low_12_neg = 10**(a12l/10)*np.array(low_12_neg)

# pairs_pos = [[high_1_pos,low_1_pos],[high_2_pos,low_2_pos],[high_12_pos,low_12_pos]]
# pairs_neg = [[high_1_pos,low_1_pos],[high_2_pos,low_2_pos],[high_12_pos,low_12_pos]]
# pos_1_sum = (np.array(high_1_pos)+np.array(low_1_pos))/100
# high_1_pos = high_1_pos/pos_1_sum
# low_1_pos = low_1_pos/pos_1_sum

# neg_1_sum = (np.array(high_1_neg)+np.array(low_1_neg))/100
# high_1_neg = high_1_neg/neg_1_sum
# low_1_neg = low_1_neg/neg_1_sum

# pos_2_sum = (np.array(high_2_pos)+np.array(low_2_pos))/100
# high_2_pos = high_2_pos/pos_2_sum
# low_2_pos = low_2_pos/pos_2_sum

# neg_2_sum = (np.array(high_2_neg)+np.array(low_2_neg))/100
# high_2_neg = high_2_neg/neg_2_sum
# low_2_neg = low_2_neg/neg_2_sum

# pos_12_sum = (np.array(high_12_pos)+np.array(low_12_pos))/100
# high_12_pos = high_12_pos/pos_12_sum
# low_12_pos = low_12_pos/pos_12_sum

# neg_12_sum = (np.array(high_12_neg)+np.array(low_12_neg))/100
# high_12_neg = high_12_neg/neg_12_sum
# low_12_neg = low_12_neg/neg_12_sum

fig = plt.figure(figsize = (14,7))
ax = fig.add_subplot(111)

alpha = 6 #db
# testing
# P0_pos = ((np.array(high_1_pos)+np.array(low_1_pos)+np.array([alpha] * 11))/10)
# testing
# ax.plot(curr,P0_pos,'ro-',label = 'Верхнее, I+')

ax.plot(curr,high_2_pos,'ro-',label = 'Верхнее, I+')
ax.plot(curr,high_2_neg,'ko-',label = 'Верхнее, I-')
ax.plot(curr,low_2_pos,'rs--',label = 'Нижнее, I+')
ax.plot(curr,low_2_neg,'ks--',label = 'Нижнее, I-')
# x_interpol = np.arange(0,70,0.05)
# Interpol = sp.interpolate.CubicSpline(lnew,sqvnew,extrapolate = False)
# ax.plot(x_interpol,Interpol(x_interpol),'r-')
# ax.set_xticks(range(0,70,3),minor = True)
# ax.set_yticks(range(46,52,1),minor = True)
ax.grid(which = 'both')
plt.legend()
plt.title(r'1-я обмотка')
plt.xlabel(r'I, a.u.',fontsize = 25)
# plt.ylabel(r'$|E|^2$, $\mu V$')

plt.show()
# fig.savefig('imgs/graphs/phaser1.png',dpi=500)
