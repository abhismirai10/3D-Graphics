import tensorflow
from vpython import *
from time import *

# Room setup
floor = box(pos=vector(0,-5,0), color=color.blue, length=10, width=10, height=0.2)  # Floor
ceiling = box(pos=vector(0,5,0), color=color.white, length=10, width=10, height=0.2) # Ceiling
wall1 = box(pos=vector(5,0,0), color=color.green, length=0.2, height=10, width=10)  # right wall
wall2 = box(pos=vector(-5,0,0), color=color.green, length=0.2, height=10, width=10)  # left wall
#wall3 = box(pos=vector(0,0,5), color=color.green, length=10, height=10, width=0.2)  # front wall
wall4 = box(pos=vector(0,0,-5), color=color.green, length=10, height=10, width=0.2)  # back wall

# Creating a ball
marble=sphere(radius=.75,color=color.red)

# Set the ball's intial Condition
time=0
g=-9.8
v_0=0 
x_0=0

# Animation loop
while True:
    rate(100)  # limiting the speed of the animation to 100 iterations per second
    v = v_0 + g * time
    x = x_0 + v_0 * time + (0.5) * g * (time**2)

    # Check for collisions with the walls and reverse velocity if necessary
    if x<=-4.25:
        v_0 = -v
        x_0 = x
        time=0
    marble.pos=vector(0,x,0) 
    time=time + 0.01
