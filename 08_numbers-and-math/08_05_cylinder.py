# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.

radius = 3.14
height = 5
pi = 3.14

volume = pi * radius**2 * height
surface_area = 2 * pi * radius * (height + radius)

print("Volume of cylinder: " + str(volume))
print("Surface area of cylinder: " + str(surface_area))