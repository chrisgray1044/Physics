
def Verlet(P, P1, dx, P2):
	P_new = P + P1*dx + P2(P,V)*dx**2/2
	P1_new = P1 + (P2(P,V) + P2(P_new,V_new))/2 * dx
	return (P_new, P1_new)


from numpy import linspace, sqrt, pi, cos
from matplotlib import pyplot as plot	

def P2(P,V):
		psi=-2*(E-V)*P
		return psi
#Cosine Well
def Pot(x):
		return -10*(1+cos((pi*x)/2)) #Vo=20  L=2

#interval
dx=.01
#Approximated energies
#Eo=-17.5898732
#E1=-12.7932354
Elist=linspace(-12.7932377655,-12.7932321101,30) #Energy range for examination

for j in Elist: #preform the verlet algorithm for every E value
	print j #E Vaule for this integration
	P = .000001
	E=j
	V =0
	P1=1
	Plist=[] #lists for storeing
	P1list=[]
	Vlist=[]
	Plist.append(P)
	P1list.append(P1)    #starting values
	Vlist.append(V)
	xindep1=linspace(-3,-1,200)	#V=0 domain
	xindep2=linspace(-0.99,0.99,200) #cosine domain
	xindep3=linspace(1,3,200)	#V=0 domain
	xindep=linspace(-3,3,600)
	#Integration
	for i in xindep1:
		
		V=0
		V_new=0
		P, P1 = Verlet(P, P1, dx, P2)
		Plist.append(P)
		P1list.append(P1)
		Vlist.append(V)
		
	for i in xindep2:	
		
		V=Pot(i)
		V_new=Pot(i+dx)
		P, P1 = Verlet(P, P1, dx, P2)
		Plist.append(P)
		P1list.append(P1)
		Vlist.append(V)
		
	for i in xindep3:
		V=0
		V_new=0
		P, P1 = Verlet(P, P1, dx, P2)
		Plist.append(P)
		P1list.append(P1)
		Vlist.append(V)
			
	del Plist[1]
	del Vlist[1]
	print len(Plist)
	print len(Vlist)
	
	plot.plot(xindep,Plist, "-")
	plot.axvline(x=1) #x positions of the end of the potentail
	plot.axvline(x=-1)
	plot.show()
	
	
