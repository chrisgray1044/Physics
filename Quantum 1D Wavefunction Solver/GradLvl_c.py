
#See part a for Comments
def Verlet(P, P1, dx, P2):
	P_new = P + P1*dx + P2(P,V)*dx**2/2
	P1_new = P1 + (P2(P,V) + P2(P_new,V_new))/2 * dx
	return (P_new, P1_new)


from numpy import linspace, sqrt
from matplotlib import pyplot as plot	

def P2(P,V):
		psi=-2*(E-V)*P
		return psi
#Mexican Hat Potentail
def Pot(x):
		return x**4-8*x**2 #a=2
#Approximated energies
#Eo=0.542029
#E1=20.83062

Elist=linspace(.54201,.54205,30)
#Elist=linspace(20.83059,20.83064,30) #E range for examination
dx=.01
		
for j in Elist: #preform the verlet algorithm for every E value
	print j #E Vaule for this integration
	# starting Values
	P = .000001
	E=j
	V =(-6-dx)**4-8*(-6-dx)**2
	P1=1
	#Storing Lists
	Plist=[]
	P1list=[]
	Vlist=[]
	#Store Starting values
	Plist.append(P)
	P1list.append(P1)
	Vlist.append(V)
	#Domain
	xindep=linspace(-6,6,120)
	for i in xindep:
		
		V=Pot(i)
		V_new=Pot(i+dx)
		P, P1 = Verlet(P, P1, dx, P2)
		Plist.append(P)
		P1list.append(P1)
		Vlist.append(V)

	del Plist[1]
	del Vlist[1]
	print len(Plist)
	print len(Vlist)
	
	plot.plot(xindep,Plist, "-")
	plot.axvline(x=-sqrt(4+sqrt(E+16))) #x positions of the end of the potential
	plot.axvline(x=sqrt(4+sqrt(E+16)))

	plot.show()