from vpython import *
from time import *

# Room setup
myBox = box(pos=vector(0,-5,0), color=color.blue, length=10, width=10, height=0.2)  # Floor
ceiling = box(pos=vector(0,5,0), color=color.white, length=10, width=10, height=0.2) # Ceiling
wall1 = box(pos=vector(5,0,0), color=color.green, length=0.2, height=10, width=10)  # right wall
wall2 = box(pos=vector(-5,0,0), color=color.green, length=0.2, height=10, width=10)  # left wall
#wall3 = box(pos=vector(0,0,5), color=color.green, length=10, height=10, width=0.2)  # front wall
wall4 = box(pos=vector(0,0,-5), color=color.green, length=10, height=10, width=0.2)  # back wall

while True:

    pass
