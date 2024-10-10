# Constants
pi = 22 / 7

# Calculate surface area and volume of a sphere
radian = float(input('Radius of sphere: '))

sur_area = 4 * pi * radian ** 2
volume = (4 / 3) * pi * radian ** 3

print("Surface Area of the sphere is:", sur_area)
print("Volume of the sphere is:", volume)

# Functions to calculate area and total surface area of a cube
def areaCube(a):
    return a ** 3  # Volume of the cube

def surfaceCube(a):
    return 6 * (a ** 2)  # Surface area of the cube

# Cube dimensions
a = 5

print("Volume of the cube =", areaCube(a))
print("Total surface area of the cube =", surfaceCube(a))
