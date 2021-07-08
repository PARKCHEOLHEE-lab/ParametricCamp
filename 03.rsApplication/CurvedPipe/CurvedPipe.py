import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as r

pts = [rs.AddPoint(i*x,j*x,r.randrange(1, 100))\
     for i in range(5) for j in range(5)]

crv = rs.AddCurve(pts, degree=2)

pipe = rs.AddPipe(crv, 0, 1, cap=1)