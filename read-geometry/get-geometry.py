import numpy as np
import math

datafile = np.genfromtxt('6-prism.xyz', skip_header=2)
rawdata=datafile[:,1:]

sfcoord=np.zeros((18,3),float)
for i in range(6):
  for j in range(3):
    ii=j+i*3
    sfcoord[ii,:]=rawdata[ii,:]

mass_atom=[15.999, 1.008, 1.008]
coordx_h2o=np.zeros((6,3),float)
coordy_h2o=np.zeros((6,3),float)
coordz_h2o=np.zeros((6,3),float)
for i in range(6):
  for j in range(3):
    ii=j+i*3
    coordx_h2o[i,j]=sfcoord[ii,0]
    coordy_h2o[i,j]=sfcoord[ii,1]
    coordz_h2o[i,j]=sfcoord[ii,2]

com_coordx=np.zeros(6,float)
com_coordy=np.zeros(6,float)
com_coordz=np.zeros(6,float)
for i in range(6):
  com_coordx[i]=np.sum(mass_atom*coordx_h2o[i,:])/np.sum(mass_atom)
  com_coordy[i]=np.sum(mass_atom*coordy_h2o[i,:])/np.sum(mass_atom)
  com_coordz[i]=np.sum(mass_atom*coordz_h2o[i,:])/np.sum(mass_atom)

print(com_coordz)
exit()

qx=np.zeros((6,3),float)
qy=np.zeros((6,3),float)
qz=np.zeros((6,3),float)
for i in range(6):
  for j in range(3):
    qx[i,j]=coordx_h2o[i,j]-com_coordx[i]
    qy[i,j]=coordy_h2o[i,j]-com_coordy[i]
    qz[i,j]=coordz_h2o[i,j]-com_coordz[i]

#Body fixed geometry of an water
ROwf=[0.0,0.0,0.1]
angHOH=107.4
dOH=0.9419
ang1=(angHOH*math.pi)/180.0
zH=ROwf[2]-math.sqrt(0.5*dOH*dOH*(1.0+math.cos(ang1)))
xH=math.sqrt(dOH*dOH-(ROwf[2]-zH)*(ROwf[2]-zH))

#Evaluation of euler angles
cost=np.zeros(3,float)
for i in range(6):
  print(qz[i,2]/ROwf[2])
  print(qz[i,2])
