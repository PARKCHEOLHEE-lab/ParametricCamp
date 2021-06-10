import rhinoscriptsyntax as rs
import math

pts = []
pts2 = []
pts3 = []

for i in range(int(min), int(max)):
    x = i * scale
    y = math.cos(x * c+d) * a + b
    yy = math.sin(x * c)
    z = 0
    
    p = rs.AddPoint(x,y,z)
    pts.append(p)
    
    p = rs.AddPoint(x,yy,z)
    pts2.append(p)
    
    p = rs.AddPoint(x,y*yy,z)
    pts3.append(p)
    
a = pts
b = pts2
c = pts3