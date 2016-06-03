
#Verlet Algorithm
def Verlet(P, P1, dx, P2):
	P_new = P + P1*dx + P2(P,V)*dx**2/2
	P1_new = P1 + (P2(P,V) + P2(P_new,V_new))/2 * dx
	return (P_new, P1_new)


from numpy import linspace, sqrt
	
# Second derivative of psi
def P2(P,V):
		psi=-2*(E-V)*P
		return psi
#Harmonic Ocillator Potential	
def Pot(x):
		return .5*x**2 #k=1
# Starting values 
P = .001

#E=0.500497 #gound state energy (uncomment for use)
E=1.501486 #1rst excited state energy (uncomment for use)
dx=.01
V = .5*(-5-dx)**2
P1=.0001

# Lists for storing
Plist=[]
P1list=[]
Vlist=[]
Plist.append(P)
P1list.append(P1)
Vlist.append(V)

#Generate independent variable
xindep=linspace(-5,5,1000)
#Integration	
for i in xindep:
	V=Pot(i)
	V_new=Pot(i+dx)
	P, P1 = Verlet(P, P1, dx, P2)
	Plist.append(P)
	P1list.append(P1)
	Vlist.append(V)
#plots
from matplotlib import pyplot as plot
del Plist[1]
del Vlist[1]
print len(Plist)
print len(Vlist)
	
plot.plot(xindep,Plist, "-")
plot.axvline(x=sqrt(2*E)) #x positions of the end of the potentail
plot.axvline(x=-sqrt(2*E))
plot.show()