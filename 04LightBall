from vpython import *

# Create a sphere
my_sphere = sphere(pos=vector(0, 0, 0), color=vector(1,1,0), radius=1)

# Initialize RGB values
red_value = 1
blue_value = 1
green_value = 0

while True:
    rate(100) # refresh rate

    # Update the color of the sphere
    # We assume that red_value, blue_value and green_value are in the range [0,1]
    my_sphere.color = vector(red_value, green_value, blue_value)

    # Here you can change the red_value, blue_value, green_value as per your requirement.
    # For example, to cycle colors, you could use the following:
    red_value = (red_value + 0.001) % 1.0
    blue_value = (blue_value + 0.002) % 1.0
    green_value = (green_value + 0.003) % 1.0
