import fastmath

p1 = fastmath.Point(0.0, 0.0)
p2 = fastmath.Point(3.0, 4.0)

print(p1)               # Point(x=0, y=0)
print(p2.distance(p1))  # 5.0
print(p2.x, p2.y)       # 3.0 4.0