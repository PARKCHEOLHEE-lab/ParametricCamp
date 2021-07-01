import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as r

#r.seed(seed)
c1 = rs.AddCircle(rg.Plane.WorldXY, r.randrange(1, 100))
c2 = rs.AddCircle([0,0,z], r.randrange(1, 100))
c3 = rs.AddCircle([0,0,z*2], r.randrange(1, 100))

c1pts = []
c2pts = []
c3pts = []
c1p = rs.DivideCurve(c1, seg)
c2p = rs.DivideCurve(c2, seg)
c3p = rs.DivideCurve(c3, seg)

for i in range(seg):
    c1pts.append(rs.AddPoint(c1p[i]))
    c2pts.append(rs.AddPoint(c2p[i]))
    c3pts.append(rs.AddPoint(c3p[i]))

lns = []
for l in range(seg):
    lns.append(rs.AddLine(c1pts[l], c2pts[l]))
    lns.append(rs.AddLine(c2pts[l], c3pts[l]))

loft = rs.AddLoftSrf(lns, loft_type = type, closed=True)

print(lns)

#a = c1
#b = c2
#c = c3
d = loft
e = lns