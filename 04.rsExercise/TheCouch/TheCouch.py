import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import math

pts1 = []
for i in range(7):
    pt1 = rs.AddPoint(i*10,0,4.5)
    if i == 3:
        pt1 = rs.AddPoint(i*10,0,-2)
    pts1.append(pt1)

pts2 = []
for i in range(7):
    pt2 = rs.AddPoint(i*10,15,4.5)
    if i == 3:
        pt2 = rs.AddPoint(i*10,15,11)
    pts2.append(pt2)

crv1 = rs.coercecurve(rs.AddCurve(pts1, 2))
crv2 = rs.coercecurve(rs.AddCurve(pts2, 2))

srf = gh.RuledSurface(crv1, crv2)
cSrf = gh.DeconstructBrep(srf)[0]
cSrf = rs.MoveObject(cSrf, [0,0,distance])

srf = rs.ExtrudeSurface(srf, rs.AddLine(rs.AddPoint(0,0,0), rs.AddPoint(0,0,0.5)))
srf = rs.coercebrep(srf)

basePoint = rs.PointCoordinates(rs.AddPoint(0,0,rs.PointCoordinates(pts1[3])[2]))
endPoint = rs.PointCoordinates(rs.AddPoint(0,0,rs.PointCoordinates(pts2[3])[2]))
interval = abs(distance)

contour = rg.Brep.CreateContourCurves(srf, basePoint, endPoint, interval)
contourList = []
for i in range(len(contour)):
    contourList.append(rs.ExtrudeCurve(contour[i], rs.AddLine(rs.AddPoint(0,0,0), rs.AddPoint(0,0,distance))))
    rs.CapPlanarHoles(contourList[i])

d = rs.Distance(pts1[0], pts2[0])
leftBox = gh.DomainBox(rs.coerce3dpoint(rs.AddPoint(0,0,0)), 10,d,4.9)
rightBox = gh.DomainBox(rs.coerce3dpoint(rs.AddPoint(60,0,0)), -10,d,4.9)
midBox = gh.DomainBox(rs.coerce3dpoint(rs.AddPoint(10,0.3,0)), 40,d-0.3,20)
midBox = rs.MoveObject(midBox, [0,0,0])
midBox = rs.SplitBrep(midBox, cSrf)[1]

handrailCrv = gh.DeconstructBrep(rs.coercebrep(cSrf))[1]
handrail = []
for i in range(len(handrailCrv)):
    handrail.append(rs.ExtrudeCurve(handrailCrv[i], rs.AddLine(rs.AddPoint(0,0,0), rs.AddPoint(0,0,1.3))))

handrailCutter = gh.CenterBox(rs.coerce3dpoint(pts1[3]), 3,3,5)
handrailCutter = rs.MoveObject(handrailCutter, [0,0,0])
cHandrail = handrail[0] 
handrail[0] = rs.SplitBrep(cHandrail, handrailCutter)[0]
handrail.append(rs.SplitBrep(cHandrail, handrailCutter)[1])