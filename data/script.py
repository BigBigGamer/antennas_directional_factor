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

fid11=open('data/data4.txt','r')
lines11=fid11.readlines()
sqvnew=[] 
lnew=[]
for i in range(1,len(lines11)):
    # print(float(lines[i].split(',')[0]))
    sqvnew.append(float(lines11[i].split(',')[0]))
    lnew.append(float(lines11[i].split(',')[1]))


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
Interpol = sp.interpolate.CubicSpline(lnew,sqvnew,extrapolate = False)
ax.plot(x_interpol,Interpol(x_interpol),'r-')
ax.set_xticks(range(0,70,3),minor = True)
ax.set_yticks(range(46,52,1),minor = True)
ax.grid(True,which = 'minor')
# plt.title(r'Зависимость интенсивности $|E|^2$ от координаты x')
plt.xlabel(r'x, мм')
plt.ylabel(r'$|E|^2$, $\mu V$')

# a = [1,3,4,5]
plt.show()
fig.savefig('graphs/data111.png',dpi=500)



# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)

# x_interpol = np.arange(0,50,0.05)
# Interpol = sp.interpolate.CubicSpline(deltaX,sqv2,extrapolate = False)
# ax2.plot(x_interpol,Interpol(x_interpol),'r-')

# ax2.plot(deltaX,sqv2,'ko')
# ax2.set_xticks(range(0,50,1),minor = True)
# ax2.set_yticks(range(42,55,1),minor = True)
# ax2.grid(True,which = 'minor')
# plt.ylabel(r'$|E|^2$, $\mu V$')
# plt.xlabel(r'$\Delta X$, мм')
# plt.show()
# fig2.savefig('graphs/data222.png',dpi=500)




# fig3 = plt.figure()
# ax3 = fig3.add_subplot(111)
# x_interpol = np.arange(30,60,0.05)
# Interpol = sp.interpolate.CubicSpline(deltaX3,Gamma,extrapolate = False)
# ax3.plot(x_interpol,Interpol(x_interpol),'r-')
# ax3.plot(deltaX3,Gamma,'ko')
# ax3.set_xticks(range(30,60,1),minor = True)
# ax3.set_yticks(np.arange(0.02,0.07,0.005),minor = True)
# ax3.grid(True,which = 'minor')
# plt.ylabel(r'$\tilde{\Gamma}$')
# plt.xlabel(r'$\Delta X$, мм')
# plt.show()
# fig3.savefig('graphs/data33.png',dpi=500)