c = Circle(the_radius)
c.radius
c = Circle(4)
print(c.diameter)
c = Circle(4)
c.diameter = 2
print(c.diameter)
print(c.radius)
c = Circle(2)
print(c.area)
c = Circle.from_diameter(8)
print(c.diameter)
print(c.radius)

c = Circle(4)

print(c)
repr(c)
d = eval(repr(c))
d
c1 = Circle(2)

c2 = Circle(4)

print(c1 + c2)
print(c2 * 3)
print(c1 > c2)
print(c1 < c2)
print(c1 == c2)
c3 = Circle(4)
print(c2 == c3)
print(circles)
circles.sort()
print(circles)
