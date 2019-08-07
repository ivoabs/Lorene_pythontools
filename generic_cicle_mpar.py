#! /usr/bin/env python


#DESCRIPTION: runs creates [given quantity] VS [stellar parameter (radius, mass, etc)] data file.
#HOW TO RUN:
	# chmod +x code_name.py
	#./code_name.py 




###########################################
#MODULES
###########################################
import subprocess 
import My_Functions

###########################################
#VALUES
###########################################

vl=3 #line of file where our value of interest is located.
#(3-> freq_si, 6->Requested magnetic moment)

parameter_file1="Bsup1.d"
parameter_file2="Bcent1.d"
parameter_file3="mass_b.d"
parameter_file4="central_density.d"
parameter_file5="radius_cpol.d"
parameter_file6="radius_ceq.d"
parameter_file7="radius_circ.d"
parameter_file8="GRV2.d"
parameter_file9="GRV3.d"
parameter_file10="CFA.d"
parameter_file11="freq_f.d"
parameter_file12="angular_momentum.d"
parameter_file13="inertia.d"


ficheiro="parrot.d"


#LOOP OVER QUANTITY
quant_init=0.
quant_final=1000.
N=40 #Actual number of points is going to be N+1
h=(quant_final-quant_init)/N
quant=quant_init


########################################### MAIN PROGRAM ###########################################
#THE CICLE
f=open("loopfreq_L88_m12.d",'w')
f.write("#Parameter Bsup Bcent mass_b central_density R_pol R_eq R_circ GRV2 GRV3 CFA \n")

for i in range (N+1): 

	My_Functions.change_val_file(ficheiro,quant,vl)
	
	subprocess.check_call(["./mageos"])

	f2=open(parameter_file1,'r')
	parlines=f2.readlines()
	f2.close()

	f3=open(parameter_file2,'r')
	parlines2=f3.readlines()
	f3.close()

	f4=open(parameter_file3,'r')
	parlines3=f4.readlines()
	f4.close()

	f5=open(parameter_file4,'r')
	parlines4=f5.readlines()
	f5.close()

	f6=open(parameter_file5,'r')
	parlines5=f6.readlines()
	f6.close()

	f7=open(parameter_file6,'r')
	parlines6=f7.readlines()
	f7.close()

	f8=open(parameter_file7,'r')
	parlines7=f8.readlines()
	f8.close()

	f9=open(parameter_file8,'r')
	parlines8=f9.readlines()
	f9.close()

	f10=open(parameter_file9,'r')
	parlines9=f10.readlines()
	f10.close()

	f11=open(parameter_file10,'r')
	parlines10=f11.readlines()
	f11.close()

	f12=open(parameter_file11,'r')
	parlines11=f12.readlines()
	f12.close()

	f13=open(parameter_file12,'r')
	parlines12=f13.readlines()
	f3.close()

	f14=open(parameter_file13,'r')
	parlines13=f14.readlines()
	f14.close()

	f.write(str(quant)+" "+parlines[0].strip("\n")+" "+parlines2[0].strip("\n")+" "+parlines3[0].strip("\n")+" "+parlines4[0].strip("\n")+" "+
			parlines5[0].strip("\n")+" "+parlines6[0].strip("\n")+" "+parlines7[0].strip("\n")+" "+parlines8[0].strip("\n")+" "+
			parlines9[0].strip("\n")+" "+parlines10[0].strip("\n")+" "+parlines11[0].strip("\n")+" "+parlines12[0].strip("\n")+" "+parlines13[0].strip("\n")+"\n")
	quant=quant+h
f.close()
########################################### END OF MAIN PROGRAM ###########################################




