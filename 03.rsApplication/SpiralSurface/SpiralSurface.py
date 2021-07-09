import rhinoscriptsyntax as rs
import math

pts = []
for i in range(height):
    x = math.sin(i)
    y = math.cos(i)
    z = i
    p = rs.AddPoint(x * size, y * size, z * 10)
    pts.append(p)

crv1 = rs.AddInterpCurve(pts)
crv2 = rs.OffsetCurve(crv1, [0,0,0], -size/2)

divcrv1 = rs.DivideCurve(crv1, len(pts)*2.5)
divcrv2 = rs.DivideCurve(crv2, len(pts)*2.5)

lns = []
for i in range(len(divcrv1)):
    ln = rs.AddLine(divcrv1[i], divcrv2[i])
    lns.append(ln)

ramp = rs.AddLoftSrf(lns)
