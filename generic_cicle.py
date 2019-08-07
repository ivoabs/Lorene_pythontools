#! /usr/bin/env python


#DESCRIPTION: runs creates [given quantity] VS [stellar parameter (radius, mass, etc)] data file.

#to run:
# chmod +x Cicle.py
#./Cicle.py 


import subprocess 
import My_Functions

#VALUES
vl=3 #line of file where our value of interest is located.
#(3-> freq_si, 6->Requested magnetic moment)

parameter_file="central_cendity.d" # You may need to change mag_eos_star.C file in order to produce the desired output.
#parameter_file2="Bcent2.d"

#_________XXXXXXX
#GETTING INITIAL VALUE
ficheiro="parrot.d"
#f=open(ficheiro,'r')
#lines=f.readlines()
#quant_line=lines[vl]
#quant_line=quant_line.split(' ')
#quant_init=float(quant_line[0])
#f.close()
quant_init=60.



#LOOP OVER QUANTITY
quant_final=10000.
N=4 #Actual number of points is going to be N+1
h=(quant_final-quant_init)/N
quant=quant_init

#THE CICLE
f=open("Quantity_Vs_Parameter.d",'w')
f.write("Parameter [units]   Quantity(theta=0)      Quantity(theta=pi/2) \n")

for i in range (N+1): 

	My_Functions.change_val_file(ficheiro,quant,vl)
	
	subprocess.check_call(["./mageos"])

	f2=open(parameter_file,'r')
	parlines=f2.readlines()
	f2.close()

	#f3=open(parameter_file2,'r')
	#parlines2=f3.readlines()
	#f3.close()

	#rlines=rlines.split(" ")
	#f.write(str(quant)+" " +parlines[0]+" "+parlines2[0]+"\n") ---> for two parameters
	f.write(str(quant)+" " +parlines[0]+"\n")
	quant=quant+h
f.close()



###############

#subprocess.check_call(["./mageos"])



