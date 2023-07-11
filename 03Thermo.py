from vpython import *
import time

temp=10
i=1
# Create the environment
scene = canvas(title="Thermometer Simulation")

# Create the outer cylinder for the thermometer
outer_cylinder = cylinder(pos=vector(0, 0, 0), axis=vector(0, 1, 0), radius=0.1, color=color.gray(0.5), opacity=0.4)

# Create the bulb at the bottom of the thermometer
bulb = sphere(pos=vector(0,-0.1,0), radius=0.15, color=color.gray(0.5))

# Create the inner cylinder for the thermometer
inner_cylinder = cylinder(pos=vector(0, 0, 0), axis=vector(0, 0, 0), radius=0.08, color=color.red)

# Create temperature markings and labels
for t in range(0, 101, 10):
    # Add a small cylinder as the marking
    marking = cylinder(pos=vector(0, t/100, 0), axis=vector(0, 0.01, 0), radius=0.12, color=color.white)
    
    # Add a label next to the marking
    label(pos=vector(0.2, t/100, 0), text=str(t), color=color.white, box=False)

# Create a function to simulate the temperature change
def set_temperature(temp):
    inner_cylinder.axis.y = temp / 100

# Animate the temperature change between 10 and 20
while True:
    rate(100)
    set_temperature(temp)
    temp=temp+0.1 * i
    if temp >= 80:
        i=(-1)*i
    if temp <= 10:
        i=(-1)*i
