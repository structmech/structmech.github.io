from numpy.linalg import solve
from numpy import array, sin,cos,sqrt,matmul,pi

elast=2E5;
L0=5000*sqrt(2);
L1=L0;L=L0;
A0=6000;A1=7000;
theta0=45*pi/180; theta1=135*pi/180;
c0=cos(theta0);s0=sin(theta0);
c1=cos(theta1);s1=sin(theta1);
K0=(elast*A0/L)*array([[c0**2,s0*c0,-c0**2,-s0*c0],\
    [s0*c0,s0**2,-s0*c0,-s0**2],\
    [-c0**2,-s0*c0,c0**2,s0*c0],\
    [-s0*c0,-s0**2,s0*c0,s0**2]]);

K1=(elast*A1/L)*array([[c1**2,s1*c1,-c1**2,-s1*c1],\
    [s1*c1,s1**2,-s1*c1,-s1**2],\
    [-c1**2,-s1*c1,c1**2,s1*c1],\
    [-s1*c1,-s1**2,s1*c1,s1**2]])
Kff=array([[K0[2,2]+K1[2,2],K0[2,3]+K1[2,3]],\
    [K0[2,3]+K1[2,3], K0[3,3]+K1[3,3]]]);
Ff=array([6E5*cos(25*pi/180),6E5*sin(25*pi/180)]);
Deltaf=solve(Kff,Ff);
Ksf=array([[K0[0,2],K0[0,3]],[K0[1,2],K0[1,3]],\
    [K1[0,2],K1[0,3]], [K1[1,2],K1[1,3]]]);
Fs=matmul(Ksf,Deltaf)
print("Ksf = ",Ksf);
print("Deltaf = ", Deltaf);
print("Fs = ",Fs);