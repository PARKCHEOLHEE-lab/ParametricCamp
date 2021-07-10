import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as r

plane = rg.Plane.WorldXY
rec = rs.AddRectangle(plane, size, size)
recs1 = []
for i in range(grid):
    for j in range(grid):
        rc = rs.CopyObject(rec, [i*size, j*size, 0])
        recs1.append(rc)

recs2 = []
for i in range(len(recs1)):
#    rc = rs.CopyObject(recs1[i], [0, 0, r.randint(height/2, height)])
    rc = rs.CopyObject(recs1[i], [0, 0, height])
    recs2.append(rc)

centroid = rs.CurveAreaCentroid(recs1[4])
rs.RotateObjects(recs2, centroid[0], angle)

recs3 = []
for i in range(len(recs1)):          
    merge = [recs1[i]] + [recs2[i]]  # rectangle grouping for loft
    recs3.append(merge)

loft = []
for i in range(len(recs1)):
    lo = rs.AddLoftSrf(recs3[i])     # object GUID ▼
    rs.CapPlanarHoles(lo)
    loft.append(rs.coercebrep(lo))   # Translate Geometry.Brep object

