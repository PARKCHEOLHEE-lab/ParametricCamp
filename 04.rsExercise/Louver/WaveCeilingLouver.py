import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import random as r

r.seed(0)

pts = []
uv = 10
for i in range(uv):
    for j in range(length):
        pt = rs.AddPoint(i*5,j*interval,0)
        rs.MoveObject(pt, [0,0,r.uniform(13.0, 20.0)])
        pt = rs.PointCoordinates(pt)
        pts.append(pt)

srf = gh.SurfaceFromPoints(pts, uv, False)

rec = rs.AddRectangle(rg.Plane.WorldZX, uv*5-30, uv*5-5)
recs = []
louvers = []
for i in range(length):
    crec = rs.CopyObject(rec, [0,i*interval,0])
    louver = rs.AddPlanarSrf(crec)
    
    if i == 0:
        louver = rs.SplitBrep(louver, srf)[1]
    else:
        louver = rs.SplitBrep(louver, srf)[0]
    
    louver = rs.ExtrudeSurface(louver, rs.AddLine(rs.AddPoint(0,0,0), rs.AddPoint(0,0.3,0)))
    recs.append(crec)
    louvers.append(louver)

fBase = gh.DivideLength(rs.coercecurve(recs[0]), 6.1)[0]
fBase = [fBase[5], fBase[7], fBase[9]]
hFrame = gh.DomainBox(fBase, 0.5, length*interval-interval, 0.5)
vBase = gh.DomainBox(fBase, 0.1, 0.1, 7)

vFrame = []
for i in range(int(interval)-1, length, int(interval)):
    for j in range(len(fBase)):
        vFrame.append(rs.CopyObjects(vBase, [0,i*interval,0])[j])