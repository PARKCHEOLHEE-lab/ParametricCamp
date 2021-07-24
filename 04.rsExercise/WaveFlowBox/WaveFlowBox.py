import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as gh
import random as r
import Rhino

pts = []
for i in range(pNum+1):
    for j in range(pNum+1):
        pt = rs.AddPoint(i*scale, j*scale, r.randint(minZ, maxZ))
        pt = rs.PointCoordinates(pt)
        pts.append(pt)

srf = gh.SurfaceFromPoints(pts, pNum+1, False)
box = gh.DomainBox(rg.Plane.WorldXY, pNum*scale, pNum*scale, pNum*scale)
box = rs.MoveObject(box, [0,0,0])

rs.TrimBrep(box, srf)