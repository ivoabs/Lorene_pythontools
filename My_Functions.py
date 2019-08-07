############################################################
#				***My Functions***
#
#DESCRIPTION: A set fo auxiliarry routines for LORENE
#INSTRUCTIONS:
#AUTHORSHIP: ivoabs@gmail.com ; 2018-19
############################################################



#############################################################################
#Generic
#############################################################################

import numpy as np 
from scipy.interpolate import interp1d

def copy_list(list):
	'creates a copy of a list'
	l=len(list)
	copy=[]
	for i in range(l):
		copy.append(list[i])
	return copy



def change_val_file(file,new_freq,value_line):
	'changes the frequency in the parrot.d file'
	f=open(file,'r')
	all_lines=f.readlines()
	f.close

	new_lines=copy_list(all_lines)
	fline=new_lines[value_line]
	fline=fline.split(' ')
	fline[0]=str(new_freq)
	fline=" ".join(fline)
	new_lines[value_line]=fline

	f=open(file,'w')
	for i in range(len(new_lines)):
		f.write(new_lines[i])
	f.close

	return 

#############################################################################
# Extract R(density) 
#############################################################################
def get_Rrho1(density_profile,transition_data,f_label,or_label):
	'returns the radius of the rho1 transition '

 	#f_label -> field label; 
 	#or_label->orientation label(1 for theta=0 and 2 for theta=pi/2)

	f=open(transition_data,'r')
	lines1=f.readlines()
	f.close()
	
	
	for i in range(len(lines1)):
		lines1[i]=(lines1[i]).strip()
		lines1[i]=(lines1[i]).split(" ")
		
	xi=lines1[f_label][1]

	f=open(density_profile,'r')
	lines2=f.readlines()
	f.close()
	
	for i in range(1,len(lines2)):
		lines2[i]=(lines2[i]).strip()
		lines2[i]=(lines2[i]).split("  ")
		lines2[i]=map(float,lines2[i])
	X=[]
	for i in range(1,len(lines2)):
		X.append(lines2[i][0])

	Y=[]
	for i in range(1,len(lines2)):
		Y.append(lines2[i][or_label])
	print Y
	print X

	X=np.array(X)
	Y=np.array(Y)

	f_inter=interp1d(Y,X) # because we want rho(radius)

	return f_inter(xi)



 

def get_Rrho2(density_profile,transition_data,f_label,or_label):
	'returns the radius of the rho2 transition '

 	#f_label -> field label; 
 	#or_label->orientation label(1 for theta=0 and 2 for theta=pi/2)

 	f=open(transition_data,'r')
	lines1=f.readlines()
	f.close()
	
	
	for i in range(len(lines1)):
		lines1[i]=(lines1[i]).strip()
		lines1[i]=(lines1[i]).split(" ")
		
	xi=lines1[f_label][2]

	f=open(density_profile,'r')
	lines2=f.readlines()
	f.close()
	
	for i in range(1,len(lines2)):
		lines2[i]=(lines2[i]).strip()
		lines2[i]=(lines2[i]).split("  ")
		lines2[i]=map(float,lines2[i])
	X=[]
	for i in range(1,len(lines2)):
		X.append(lines2[i][0])

	Y=[]
	for i in range(1,len(lines2)):
		Y.append(lines2[i][or_label])

	X=np.array(X)
	Y=np.array(Y)

	f_inter=interp1d(Y,X) # because we want rho(radius)

	return f_inter(xi)


	 
def B_to_mu(Bmu_data,Bval,or_label):
 	#f_label -> field label; 
 	#or_label->orientation label(1 for theta=0 and 2 for theta=pi/2)

	f=open(transition_data,'r')
	lines1=f.readlines()
	f.close()
	
	
	for i in range(len(lines1)):
		lines1[i]=(lines1[i]).strip()
		lines1[i]=(lines1[i]).split(" ")
		
	xi=lines1[f_label][1]

	f=open(Bmu_data,'r')
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
		Y.append(lines2[i][or_label])

	X=np.array(X)
	Y=np.array(Y)

	f_inter=interp1d(Y,X) 

	return f_inter(Bval)

#############################################################################
#extract R(density) (OBSOLETE!!!)
#############################################################################

def get_rho1(density_profile,transition_data,f_label,or_label):
	'returns the radius of the rho1 transition '

 	#f_label -> field label; 
 	#or_label->orientation label(1 for theta=0 and 2 for theta=pi/2)

	f=open(transition_data,'r')
	lines1=f.readlines()
	f.close()
	
	
	for i in range(len(lines1)):
		lines1[i]=(lines1[i]).strip()
		lines1[i]=(lines1[i]).split(" ")
		
	xi=lines1[f_label][1]
	return xi



def get_rho2(density_profile,transition_data,f_label,or_label):
	'returns the radius of the rho2 transition '

 	#f_label -> field label; 
 	#or_label->orientation label(1 for theta=0 and 2 for theta=pi/2)

 	f=open(transition_data,'r')
	lines1=f.readlines()
	f.close()
	
	
	for i in range(len(lines1)):
		lines1[i]=(lines1[i]).strip()
		lines1[i]=(lines1[i]).split(" ")
		
	xi=lines1[f_label][2]
	return xi
#############################################################################
#CHANGE PARROT
#############################################################################

def par_zero(par_file):
	f=open(par_file,'r')
	lines=f.readlines()
	f.close

	new_lines=copy_list(lines)

	new_lines[9]=new_lines[9].split("\t")
	new_lines[9][0]="0."
	new_lines[9]="\t".join(new_lines[9])
	
	print new_lines[11]
	new_lines[11]=new_lines[11].split("\t")
	
	print new_lines[11]
	new_lines[11][0]="0."
	new_lines[11]="\t".join(new_lines[11])
	print new_lines[11]

	f=open(par_file,'w')
	for i in range(len(new_lines)):
		f.write(new_lines[i])
	f.close

	return 

def par_fin(par_file):
	f=open(par_file,'r')
	lines=f.readlines()
	f.close

	new_lines=copy_list(lines)

	new_lines[9]=new_lines[9].split("\t")
	new_lines[9][0]="21500."
	new_lines[9]="\t".join(new_lines[9])
	
	print new_lines[11]
	new_lines[11]=new_lines[11].split("\t")
	
	print new_lines[11]
	new_lines[11][0]="5000."
	new_lines[11]="\t".join(new_lines[11])
	print new_lines[11]

	f=open(par_file,'w')
	for i in range(len(new_lines)):
		f.write(new_lines[i])
	f.close

	return 
#############################################################################
#Identification of phase onset zones:
#############################################################################

def get_Rphase(density_profile,xi,f_label,or_label):
	'returns the radius of the rho1 transition '

 	#f_label -> field label; 
 	#or_label->orientation label(1 for theta=0 and 2 for theta=pi/2)

	#f=open(transition_data,'r')
	#lines1=f.readlines()
	#f.close()
	
	
	#for i in range(len(lines1)):
	#	lines1[i]=(lines1[i]).strip()
	#	lines1[i]=(lines1[i]).split(" ")
		
	#xi=lines1[f_label][1]

	f=open(density_profile,'r')
	lines2=f.readlines()
	f.close()
	
	for i in range(1,len(lines2)):
		lines2[i]=(lines2[i]).strip()
		lines2[i]=(lines2[i]).split("  ")
		lines2[i]=map(float,lines2[i])
	X=[]
	for i in range(1,len(lines2)):
		X.append(lines2[i][0])

	Y=[]
	for i in range(1,len(lines2)):
		Y.append(lines2[i][or_label])

	X=np.array(X)
	Y=np.array(Y)

	f_inter=interp1d(Y,X) # because we want rho(radius)

	return f_inter(xi)
