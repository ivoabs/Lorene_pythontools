#! /usr/bin/env python

#DESCRIPTION:Calculates crust thieckness as function of theta 
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
field_label=4 #This corresponds to the line in the transition_data file
orientation_label=2 #1 for density at theta=Pi/2 and 2 for density at theta=0
output_file="crust_angles_L55_magrot15_mp.txt" 
#density_profile="prof_density.d"
vl=3 #line of the quantity of interest in the parrot.d 

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


f_out=open(output_file,'w')
f_out.write("angle 	R(rho1)   R(rho2)  Delta(trans) Delta1  Delta2		R_full		M_bar	M_g		B_sup	 \n")

#CICLE OVER THETA
for k in range (0, 5):
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


	#!!!!!!!!!!!!check if the following is consistent with mag_eos_star.C file!!!!!!!!!!!!
	npd2=5
	theta_max=math.pi/2.
	h2=theta_max/(npd2-1)

	angle=k*h2

	#R_full=R

		#Transition raidus
	Rrho1=My_Functions.get_Rrho1("prof_density.d",transition_data,field_label,1)
	Rrho2=My_Functions.get_Rrho2("prof_density.d",transition_data,field_label,1)
		
		#Differences
	Dtrans=Rrho1-Rrho2
	Delta1=R_full-Rrho1
	Delta2=R_full-Rrho2

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
	#f_out.write("angle   R(rho2)  Delta(trans) Delta1  Delta2		R_full		M_bar	M_g		B_sup	 \n")
	f_out.write(str(angle)+" "+str(Rrho1)+" "+str(Rrho2)+" "+str(Dtrans)+" "+str(Delta1)+" "+str(Delta2)+" "+str(R_full)+" "+str(M_bar)+" "+str(M_g)+" "+str(B_sup)+"\n")
f_out.close()
########################################### END OF MAIN CODE ###########################################