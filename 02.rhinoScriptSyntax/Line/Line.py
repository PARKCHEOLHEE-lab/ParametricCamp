import rhinoscriptsyntax as rs
import random as r

r.seed(seed)

pts = []
lns = []

for i in range(pNum):
    p = rs.AddPoint(r.randrange(min, max), r.randrange(min, max), r.randrange(min, max))  
    pts.append(p)
    
for j in range(len(pts)-1):
    ln = rs.AddLine(pts[j], pts[j+1])
    lns.append(ln)

lp0 = rs.PointCoordinates(pts[0])
lp1 = rs.PointCoordinates(pts[len(pts)-1])
lln = rs.AddLine(lp0, lp1)
lns.append(lln)

a = pts
b = lns
l = lln
