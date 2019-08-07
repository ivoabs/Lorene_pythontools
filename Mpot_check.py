#! /usr/bin/env python

#DESCRIPTION:
#HOW TO RUN:
	# chmod +x code_name.py
	#./code_name.py 


###########################################
#MODULES
###########################################
import math
import subprocess 
import My_Functions
import numpy as np
import matplotlib.pyplot as plt #library used for the plot
import matplotlib.collections as collections

###########################################
#VALUES & FILES
###########################################
transition_data="Data_transition_L55.txt"
radius_file="radius_angles.d"
field_label=2 #This corresponds to the line in the transition_data file
orientation_label=2 #1 for density at theta=Pi/2 and 2 for density at theta=0
output_file="Mpot_check_result.txt"
#density_profile="prof_density.d"
vl=3 #line of the quantity of interest in the parrot.d 

Nangles=1000

########################################### MAIN CODE ###########################################

###########################################
#CALLING LORENE
###########################################
subprocess.check_call(["./mageos"])

###########################################
#RESULTS
###########################################

	#density profile
f=open("prof_density_angles.d",'r')
lines_angles=f.readlines()
f.close()

lines_angles=lines_angles[1:]
lines_angles=map(lambda x: x.strip(),lines_angles)
lines_angles=map(lambda x: x.split(" "),lines_angles)
	
	#enthalpy profile
f=open("prof_ent_angles.d",'r')
lines_ent=f.readlines()
f.close()
lines_ent=lines_ent[1:]
lines_ent=map(lambda x: x.strip(),lines_ent)
lines_ent=map(lambda x: x.split(" "),lines_ent)

f=open("Magpot_angles.d","r")
lines_mag=f.readlines()
f.close()
lines_mag=lines_mag[1:]
lines_mag=map(lambda x: x.strip(), lines_mag)
lines_mag=map(lambda x: x.split(" "),lines_mag)



for k in range (0,Nangles):
	#create prof_density
	f2=open("prof_density.d",'w')
	f2.write("# R[km] density_bar(theta) \n")
	for i in range (len(lines_angles)):
		f2.write(lines_angles[i][0]+"  "+lines_angles[i][k+1]+"\n")
	f2.close()

	#Obtaining full radius
	R_full=0
	for i in range (1,len(lines_ent)):
		x=lines_ent[i][k+1]
		x=float(x)
		if x<=0:
			R_full=float(lines_ent[i-1][0])
			break
	print k," ",x," ",R_full

			#Transition raidus
	Rrho1=My_Functions.get_Rrho1("prof_density.d",transition_data,field_label,1)
	Rrho2=My_Functions.get_Rrho2("prof_density.d",transition_data,field_label,1)
		
		#Differences
	Dtrans=Rrho1-Rrho2
	Delta1=R_full-Rrho1
	Delta2=R_full-Rrho2
                
	#Getting the maximum of M
	Mm=0
	Mmx=0
	M_list=[]
	for i in range(len(lines_mag)):
		M_list.append(lines_mag[i][k+1])
	Mm=max(M_list)
	Mmx=M_list.index(max(M_list))
	RMmx=lines_mag[Mmx][k+1]

	#Check if RMmx fall in the transition zone:
	fall=False

	if RMmx >Rrho1:
		if RMmx < Rrho2:
			fall=True

	if fall==True:
		break

f3=open(output_file,'w')
f3.write("angle 	 Maximum M 		r(Maximum M)  	R1 		R2 	\n")
f3.write(str(k)+" "+str(Mmx)+" "+str(RMmx)+" "+str(Rrho1)+" "+str(Rrho2)+"\n")
f3.close()