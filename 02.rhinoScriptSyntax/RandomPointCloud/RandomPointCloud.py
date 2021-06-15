import rhinoscriptsyntax as rs
import random


pts = []

for i in range(pNum):
#    x = random.randrange(1, 50)
#    y = random.randrange(1, 50)

    x = (random.random()-0.5) * width
    y = (random.random()-0.5) * length
    z = random.random() * height
    p = rs.AddPoint(x, y, z)
    pts.append(p)
    
a = pts