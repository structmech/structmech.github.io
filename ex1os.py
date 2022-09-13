!pip install openseespy
import numpy as np
from numpy import sin,cos,tan,pi
import matplotlib.pyplot as plt
from openseespy.opensees import *
# ------------------------------
# Start of model generation
# -----------------------------

# remove existing model
wipe()

# set modelbuilder
model('basic', '-ndm', 2, '-ndf', 2)
# create nodes
node(0, 0.0, 0.0)
node(1, 10000.0,  0.0)
node(2, 5000.0,  5000.0)
# set boundary condition
fix(0, 1, 1)
fix(1, 1, 1)
#fix(3, 1, 1)
# define materials
uniaxialMaterial("Elastic", 1, 200000)
# define elements
element("Truss",0,0,2,6000,1)
element("Truss",1,1,2, 7000, 1)
#element("Truss",2,1,2, 20000,1)

# create TimeSeries
timeSeries("Linear", 1)
# create a plain load pattern
pattern("Plain", 1, 1)
# Create the nodal load - command: load nodeID xForce yForce
load(2, (6E5)*cos(25*pi/180), (6E5)*sin(25*pi/180))
# ------------------------------
# Start of analysis generation
# ------------------------------

# create SOE
system("BandSPD")

# create DOF number
numberer("RCM")

# create constraint handler
constraints("Plain")

# create integrator
integrator("LoadControl", 1.0)

# create algorithm
algorithm("Linear")

# create analysis object
analysis("Static")

# perform the analysis
analyze(1)

Delta0 = nodeDisp(2,1)
Delta1 = nodeDisp(2,2)
reactions()
F2=nodeReaction(0,1);F3=nodeReaction(0,2);
F4=nodeReaction(1,1);F5=nodeReaction(1,2);
print("Delta0 = ",Delta0, " Delta1 = ",Delta1)
print("F2 = ",F2, " F3 = ",F3, " F4 = ",F4, " F5 = ",F5)