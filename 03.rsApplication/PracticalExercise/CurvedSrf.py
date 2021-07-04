import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as r


rec = rs.AddRectangle([-rec_size,-rec_size,0], rec_size*2, rec_size*2)
div = rec_size / UVcount * 2

# comprehension syntax
# pts = [rs.AddPoint((i*div-rec_size) ,(j*div-rec_size) ,0) for i in range(UVcount+1) for j in range(UVcount+1)]

pts = []
for i in range(UVcount+1):
    for j in range(UVcount+1):
        p = rs.AddPoint((i*div-rec_size) ,(j*div-rec_size) ,0)
        pts.append(p)

rpts = []
for i in range(len(pts)):
    rp = rs.MoveObject(pts[i], [0,0,r.randrange(10, 23)])
    rpts.append(rp)

a = pts
b = rec
c = rpts
