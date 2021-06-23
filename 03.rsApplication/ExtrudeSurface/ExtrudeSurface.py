import rhinoscriptsyntax as rs

pts = []
lns = []
cen = scale / 2

for i in range(2):
    for j in range(2):
        p = rs.AddPoint(i * scale - cen, j * scale - cen, 0)
        p = rs.PointCoordinates(p)
        pts.append(p)

for j in range(3):
    if j % 2 == 0:
        ln = rs.AddLine(pts[j], pts[j+1])
        lns.append(ln)

for k in range(2):
    ln = rs.AddLine(pts[k], pts[k+2])
    lns.append(ln)

srf = rs.AddPlanarSrf(lns)
path = rs.AddLine((100,10,0), (100,10,scale*2))

a = rs.ExtrudeSurface(srf, path)