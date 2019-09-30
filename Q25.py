from smith_chart import plot_smith
from pylab import *

plot_smith()


ZL = 1.5 - 0.7j

G = (ZL-1)/(ZL+1)
plot(real(G),imag(G),'bo')

# marker of load impedance
text(real(G),imag(G),ZL)


text(0.9,0.9,r'$|\Gamma|=%0.2f$'%abs(G))
# G - circle
theta = linspace(0,2*pi,128)
plot(abs(G) * cos(theta),abs(G)*sin(theta),alpha=0.4)

#line from the load point
amp = linspace(0,1.3,128)
plot(amp*cos(angle(G)),amp*sin(angle(G)))

L = 0.196 # lambda
# travel towards generator
phi = linspace(0,L,64)*4*pi
for p in phi:
    plot(abs(G) * cos(-p+angle(G)),abs(G)*sin(-p+angle(G)),marker='o',c='m',markersize=6,alpha=0.2)


L = -0.0541667 # lambda
# travel towards generator
phi = linspace(0,L,64)*4*pi
for p in phi:
    plot(abs(G) * cos(-p+angle(G)),abs(G)*sin(-p+angle(G)),marker='o',c='c',markersize=6,alpha=0.2)





savefig('Q25.png',dpi=150,bbox_inches='tight')
show()
