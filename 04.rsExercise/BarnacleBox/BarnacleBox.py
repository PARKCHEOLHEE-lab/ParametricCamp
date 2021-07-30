import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import random as r

I = rg.Interval
box = rg.Box(rg.Plane.WorldXY, I(0, size*rNum), I(0, -size*rNum), I(3, size*rNum-2))

rec = rs.AddRectangle(rg.Plane.WorldZX, size, size)
srf = rs.AddPlanarSrf(rec)
recs = []
srfs = []
for i in range(rNum):
    for j in range(rNum):
        recs.append(rs.coercegeometry(rs.CopyObject(rec, [size*i,0,size*j])))
        srfs.append(rs.CopyObject(srf, [size*i,0,size*j]))

cpts = []
for i in range(len(recs)):
    cpts.append(rs.coerce3dpoint(rs.CurveAreaCentroid(recs[i])[0]))

sRecs = []
for i in range(len(recs)):
    sRec = gh.Scale(recs[i], cpts[i], r.uniform(0.2, 0.5))[0]
    rs.MoveObject(sRec, [0,r.randint(int(size*rNum/rNum), int(size*rNum/rNum*2)),0])
    sRecs.append(sRec)

loft = []
for i in range(len(recs)):
    lo = [recs[i], sRecs[i]]
    loft.append(rs.AddLoftSrf(lo)[0])

barnacle = []
rotP = [size*rNum/2,-size*rNum/2,0]
for i in range(4):
    for j in range(len(recs)):
        barnacle.append(rs.RotateObjects(loft[j], rotP, 90*i, copy=True)[0])
        barnacle.append(rs.RotateObjects(srfs[j], rotP, 90*i, copy=True)[0])