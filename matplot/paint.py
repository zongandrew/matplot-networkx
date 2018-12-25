import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def calplt(R, r, d):
    x = np.linspace(0, R*r*np.pi, 50000)

    G = (R-r)*np.sin(x)
    H = (R-r)*np.cos(x)

    I = d*np.sin(-R/r*x)
    J = d*np.cos(-R/r*x)

    plt.plot(G+I, H+J, linewidth=0.5, color='red')



R = 13.0
r = 8.0 
D = 5.0
s = 0.5
for n in range(1, int(D/s)):
    plt.xlim((-R, R))
    plt.ylim((-R, R))
    plt.figure()
    calplt(R, r, s*n)
    plt.savefig("%d.png" % n)

