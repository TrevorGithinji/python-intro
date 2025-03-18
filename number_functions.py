import math

from conditions import height

x = 99999963

print(math.pi)
print(math.log(x))
print(math.sqrt(x))
print(math.floor(50.25)) #trangate
print(math.ceil(50.25))

radius = 24
height = 14
volume = 3.14*radius*radius*height
volume = round(volume, 2)

print(volume)

sa = 22/7* (radius+radius)*height + (22/7*radius*radius)
sa = round(sa, 2)
print(sa)

result = 10 + 20 / 5 * 6 - 3 * ( 5+2 )
