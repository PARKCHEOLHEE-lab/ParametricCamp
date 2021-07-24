import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import math

height = pNum + 5
hRange = int(height*height/2)
sep = pNum**2*scale

spts = []
for i in range(int(hRange/2)):
    x = math.sin(i)
    y = math.cos(i)
    z = i
    spt = rs.AddPoint(x*scale*pNum/2*1.2, y*scale*pNum/2*1.2, z*height)
    spts.append(spt)

spts = rs.MoveObjects(spts, [(pNum*scale/2)-(scale/2), (pNum*scale/2)-(scale/2), 0])
spiral = rs.AddCurve(spts, 3)

pts = []
for i in range(pNum):
    for j in range(pNum):
        for k in range(hRange):
            pt = rs.AddPoint(i*scale,j*scale,k*scale)
            pt = rs.PointCoordinates(pt)
            pts.append(pt)


cpts = []
spts = rs.DivideCurve(spiral, sep)
distance = pNum*scale - scale/scale
for i in range(len(pts)):
    for j in range(len(spts)):
        dis = rs.Distance(pts[i], spts[j])
        if dis <= distance:
            cpt = rs.CopyObject(pts[i])
            cpt = rs.PointCoordinates(cpt)
            cpts.append(cpt)

mahanakhon = gh.DomainBox(cpts, scale, scale, scale)