import rhinoscriptsyntax as rs
import math

pts = []

for i in range(int(min), int(max)):
    x = i * scale
    y = math.cos(x * c+d) * a + b
    z = 0
    
    p = rs.AddPoint(x,y,z)
    pts.append(p)
    
a = pts