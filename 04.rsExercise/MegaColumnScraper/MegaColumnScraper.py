import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

plane = rg.Plane.WorldYZ
a = rs.AddArc(plane, 15, 100)

b = []
for i in range(4):
    b.append(rs.RotateObject(a, [0,16.5,0], i*360/4, copy=True))

a = rs.AddLoftSrf(b, loft_type=2 ,closed=True)
rs.RotateObject(a, [0,0,0], 45)

c = []
for i in range(3):
    for j in range(3):
        for k in range(20):
            rs.CapPlanarHoles(a)
            c.append(rs.CopyObject(a, [i*27, j*27, k*15]))