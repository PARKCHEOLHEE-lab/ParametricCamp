import rhinoscriptsyntax as rs
import math

pts = []

for i in range(int(min), int(max)):
    x = i * scale
    y = math.fabs(x)
    z = 0
    
    p = rs.AddPoint(x,y,z)
    pts.append(p)
    
a = pts