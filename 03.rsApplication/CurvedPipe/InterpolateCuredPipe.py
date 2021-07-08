import rhinoscriptsyntax as rs
import math 

interval = (10 - (-10)) / 200
pts = []

for i in range(0, x, 3):
    x = interval * i
    y = math.cos(x) * x
    z = math.sin(x) * x
    
    pts.append(rs.AddPoint(z*5,y*5,x*10))

crv = rs.AddInterpCurve(pts)
pipe = rs.AddPipe(crv, [0,0.5,1], [1,8,16], cap=1)
pts
