#! /usr/bin/env python

#DESCRIPTION: Calculates the thickness of the transition region
#TO RUN:
# chmod +x Cicle.py
#./Cicle.py

###########################################
#MODULES
###########################################
import subprocess 
import My_Functions
import numpy as np
import matplotlib.pyplot as plt #library used for the plot
import matplotlib.collections as collections


###########################################
#VALUES & FILES
###########################################

transition_data="Data_transition_L88.txt"
density_profile="prof_density.d"
radius_file="radius.d"
field_label=2 #This corresponds to the line in the transition_data file
orientation_label=2 #1 for density at theta=Pi/2 and 2 for density at theta=0
output_file="crust_max_L88_m18.txt"
vl=3 #line of the quantity of interest in the parrot.d 

########################################### MAIN PROGRAM ###########################################

#CALLING LORENE
subprocess.check_call(["./mageos"])



#RESULTS
	#Full radius
f=open(radius_file,'r')
radius_lines=f.readlines()
f.close()
R_full=radius_lines[0].split(" ")
R_full=map(float,R_full)

	#Transition raidus
Rrho1=My_Functions.get_Rrho1(density_profile,transition_data,field_label,orientation_label)
Rrho2=My_Functions.get_Rrho2(density_profile,transition_data,field_label,orientation_label)
	
	#Differences
Dtrans=Rrho1-Rrho2
Delta1=R_full[orientation_label-1]-Rrho1
Delta2=R_full[orientation_label-1]-Rrho2

	#Other quantities
f=open("mass.d","r")
m_lines=f.readlines()
masses=m_lines[0].split(" ")
M_bar, M_g=float(masses[0]), float(masses[1])
f.close()

f=open("Bsup1.d","r")
B_lines=f.readlines()
B_sup=float(B_lines[0])
f.close()
	
	#Output
f=open(output_file,'w')
f.write("mu 	R(rho1)   R(rho2)  Delta(trans) Delta1  Delta2		R_full		M_bar	M_g		B_sup	 \n")
f.write(str(0)+" "+str(Rrho1)+" "+str(Rrho2)+" "+str(Dtrans)+" "+str(Delta1)+" "+str(Delta2)+" "+str(R_full[orientation_label-1])+" "+str(M_bar)+" "+str(M_g)+" "+str(B_sup)+"\n")
f.close

#PLOTS
   #density
f=open(density_profile,'r')
lines2=f.readlines()
f.close()

for i in range(1,len(lines2)):
	lines2[i]=(lines2[i]).strip()
	lines2[i]=(lines2[i]).split("  ")
	lines2[i]=map(float,lines2[i])
	#print lines2[i]
X=[]
for i in range(1,len(lines2)):
	X.append(lines2[i][0])

Y=[]
for i in range(1,len(lines2)):
	Y.append(lines2[i][orientation_label])

#plot
rho1=My_Functions.get_Rrho1(density_profile,transition_data,field_label,orientation_label)
rho2=My_Functions.get_Rrho2(density_profile,transition_data,field_label,orientation_label)
	
fig = plt.figure()
ax = fig.add_subplot(111)
y=np.linspace(0,max(Y),10)
Rrho1=np.linspace(Rrho1,Rrho1,10)
Rrho2=np.linspace(Rrho2,Rrho2,10)

plt.plot(X,Y,marker='o',ms=3,linestyle='-',color='r')
plt.ylabel(r'$\rho(r)$')
plt.xlabel(r'$R_{eq}$ [km]')
plt.plot(Rrho1,y,lw=1.5,linestyle='--',color='b')
plt.plot(Rrho2,y,lw=1.5,linestyle='--',color='g')
#plt.text(15, 0.20, r'$Yellow=R_{\rho_1}$')
#plt.text(15, 0.25, r'$Green=R_{\rho_2}$')

plt.grid(True)

#plt.show()
#ax.show()
########################################### END OF MAIN PROGRAM ###########################################