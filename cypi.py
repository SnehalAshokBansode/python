# Define pi
pi = 22 / 7

# Get user input for height and radius
height = float(input('Height of cylinder: '))
radian = float(input('Radius of cylinder: '))

# Calculate volume
volume = pi * radian ** 2 * height

# Calculate surface area
sur_area = (2 * pi * radian * height) + (2 * pi * radian ** 2)

# Print results
print("Volume is: ", volume)
print("Surface Area is: ", sur_area)
