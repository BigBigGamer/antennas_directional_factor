import matplotlib.pyplot as plt
from matplotlib import rc
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages
import scipy as sp
import scipy.interpolate
import scipy.optimize
# matplotlib.use('PDF')

plt.rc('text', usetex = True)
plt.rc('font', size=13, family = 'serif')
# plt.rc('text.latex',unicode=True)
# plt.rc('legend', fontsize=13)
plt.rc('text.latex', preamble=r'\usepackage[russian]{babel}')
import numpy as np
import math
fid1=open('data/data1.txt','r')
lines1=fid1.readlines()
sqv=[] 
l=[]
for i in range(1,len(lines1)):
    # print(float(lines[i].split(',')[0]))
    sqv.append(float(lines1[i].split(',')[0]))
    l.append(float(lines1[i].split(',')[1]))

fid2=open('data/data2.txt','r')
lines2=fid2.readlines()
sqv2=[] 
deltaX=[]
for i in range(1,len(lines2)):
    # print(float(lines[i].split(',')[0]))
    sqv2.append(float(lines2[i].split(',')[0]))
    deltaX.append(float(lines2[i].split(',')[1]))    

fid3=open('data/data3.txt','r')

lines3=fid3.readlines()
Emax3=[] 
Emin3=[] 
deltaX3=[]
for i in range(1,len(lines3)):
    # print(float(lines[i].split(',')[0]))
    Emax3.append(float(lines3[i].split(',')[1]))
    Emin3.append(float(lines3[i].split(',')[2]))
    deltaX3.append(float(lines3[i].split(',')[0]))
k = np.sqrt(np.array(Emin3)/np.array(Emax3))
Gamma = (1-k)/(1+k)
print('Max Gamma = ',np.amax(Gamma))
# plt.plot(deltaX3,Gamma)
# plt.plot(deltaX,sqv2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(l,sqv,'ko')
x_interpol = np.arange(0,70,0.05)
Interpol = sp.interpolate.CubicSpline(l,sqv,extrapolate = False)
ax.plot(x_interpol,Interpol(x_interpol),'r-')
ax.set_xticks(range(0,70,3))
ax.grid(True,which = 'major')
plt.title(r'Зависимость интенсивности $|E|^2$ от координаты x')
plt.xlabel(r'x, мм')
plt.ylabel(r'$|E|^2$, $\mu V$')
# plt.show()
fig.savefig('graphs/data1.png',dpi=500)

# pdf1 = PdfPages('data1.pdf')
# pdf1.savefig(fig)
# pdf1.close()


# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
# ax2.plot(deltaX,sqv2)
# ax2.set_xticks(range(0,70,3),minor = True)
# ax2.grid(True,which = 'minor')
# plt.show(block = False)

# fig3 = plt.figure()
# ax3 = fig3.add_subplot(111)
# ax3.plot(deltaX3,Gamma)
# ax3.set_xticks(range(0,70,3),minor = True)
# ax3.grid(True,which = 'minor')
# plt.show()