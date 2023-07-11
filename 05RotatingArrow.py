from vpython import *

# Create the stationary arrows (coordinate axes)
arrow_x = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.red)
arrow_y = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.green)
arrow_z = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.blue)

# Create the rotating arrow
arrow_rot = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.yellow)

# Initialize the angle
angle = 0

while True:
    rate(100) # refresh rate

    # Update the position of the rotating arrow
    if (angle >=0) & (angle < 3*pi/2):
        arrow_rot.axis = vector(cos(angle), sin(angle), 0)
    
    if (angle >=3*pi/2) & (angle < 3*pi):
        arrow_rot.axis = vector(0, cos(angle), sin(angle))

    if (angle >=3*pi) & (angle < 9*pi/2):
        arrow_rot.axis = vector(sin(angle), 0, cos(angle))

    if angle >= 9*pi/2:
        angle = 0

    # Increment the angle
    angle += 0.01
