import rhinoscriptsyntax as rs
import Rhino

pts = []
lns = []

for i in range(xNum):
    for j in range(2):
        p = rs.AddPoint(i * scale, 0, j*scale)
        p = rs.PointCoordinates(p)
        pts.append(p)

for k in range(xNum * 2 - 1):
    lns.append(rs.AddLine(pts[k], pts[k+1]))

for l in range(xNum * 2 - 2):
    lns.append(rs.AddLine(pts[l], pts[l+2]))


#rs.GetLine(lns)
print(lns[0])


b = lns
    