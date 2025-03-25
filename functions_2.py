from number_functions import radius


def volume_cylinder(radius, height):
    """" Calculates the volume  of a cylinder"""
    v = 22/7 * radius**2 * height
    return v

print(volume_cylinder(5, 10))
print(round(volume_cylinder(5, 10), 2))

v1 = volume_cylinder(height=17, radius=5) #key value pair arguments

def volume_cone(radius, height, decimals=2): #optional parameters
    v = 1/3 * 22/7 * radius**2 * height
    v = round(v, decimals)
    return v

print(volume_cone(20, 15))
print(volume_cone(15, 4, 3))

#package
