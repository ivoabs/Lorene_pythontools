#! /usr/bin/env python

#DESCRIPTION:Numerical derivative (magnetic potential) 
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
from scipy import interpolate
from scipy.integrate import dblquad, quad, nquad
import time
#import matplotlib.pyplot as plt


#import matplotlib.pyplot as plt #library used for the plot
#import matplotlib.collections as collections


###########################################
#VALUES & FILES
###########################################
file="density_table_en.d"
output="Inertia_calc.d"
########################################### MAIN CODE ###########################################
f=open(file,"r")
lines=f.readlines()
f.close()

lines=lines[1:]
lines=map(lambda x: x.strip("\n"),lines)
lines=map(lambda x: x.split(),lines)

def getcolumn(list,column):
	"returns the desired column of the list of lists"
	L=[]
	for x in list:
		L.append(x[column])
	return L


R, Theta, F=getcolumn(lines,0), getcolumn(lines,1), getcolumn(lines,2)



R, Theta, F =np.array(R,dtype=np.float),np.array(Theta,dtype=np.float), np.array(F,dtype=np.float),

#convertion:
#conv_rho=1.66E+17
#F=map(lambda x:x/(conv_rho),F)
#R=map(lambda x:x*1000,R)


#---> For Spline:


rr, tt = np.meshgrid(R, Theta)
ff=np.array(F)

print rr[0][2]
#print rr

tck = interpolate.bisplrep(R,Theta,F,s=0)
#fnew= interpolate.bisplev(rr,tt,tck)




f=interpolate.interp2d(R,Theta,F)

print f(0,0)
#print fnew(0,0)



#file=open("test_iner.d","w")
#for x in R:
#	file.write(str(x)+"	"+str(f(x,0)[0])+"\n")
#file.close()

############################ part 2 ############################

#CONVERTIONS:
#rho_unit to rho_si:



def f_rho(r, theta):
	result=interpolate.interp2d(R,Theta,F,kind='cubic')
	return result(r,theta)[0]

#def f_rho_integrand(r,theta):
#	return 2*math.pi*f_rho(r,theta)*(r**2)*math.sin(theta)

def f_rho_integrand(r,theta):
	return 2*math.pi*(r**2)*math.sin(theta)*f_rho(r,theta)

def f_aux(r,theta):
	return (r*math.cos(theta)**2)-(1/3.)*(r**2)

def f_integrand (r, theta):
	return 2*math.pi*f_rho(r,theta)*f_aux(r,theta)*(r**2)*math.sin(theta)

Rmin=0
#Rmax=((11.28472618+11.86890538)/2.)*1000
Rmax=10000

theta_min=0
theta_max=math.pi

r_lim=11000
def r_range(r):
	return (0,11000)

def t_range():
	return (0,math.pi)






#I=dblquad(f_integrand,Rmin,Rmax, lambda theta: theta_min, lambda theta:theta_max,epsabs=1.49e-03, epsrel=1.49e-03)
#,args=(Rmin,Rmax,theta_min,theta_max,)

options={'limit':10000000}
tic= time.time()
print  nquad(f_rho_integrand,[r_range,t_range],opts=[options,options])
toc=time.time()
print toc-tic


#for i in range(10,N+1):
#	r_lim=i*(Rmax)/N
#	M=M+nquad(f_rho_integrand,[t_range,r_range],opts=[options,options])
#	print i 

#print 'FINAL'
#print M


#x = np.arange(0, 2*np.pi+np.pi/4, 2*np.pi/8)
#y = np.sin(x)
#tck = interpolate.splrep(x, y, s=0)
#xnew = np.arange(0, 2*np.pi, np.pi/50)
#ynew = interpolate.splev(xnew, tck, der=0)

