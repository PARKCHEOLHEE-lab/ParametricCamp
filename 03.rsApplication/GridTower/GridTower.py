import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as r

def grid_tow(size, n):
    plane = rg.Plane.WorldXY
    r1 = rs.AddRectangle(plane, size, size)
    
    recs = []
    for i in range(n):
        for j in range(n):
            r2 = rs.CopyObject(r1, [i*size, j*size, 0])
            recs.append(r2)
    
    es = []
    for i in range(len(recs)):
        e = rs.ExtrudeCurveStraight(recs[i], [0,0,0], [0,0,r.randint(20, 150)])
        es.append(e)
        rs.CapPlanarHoles(es[i])
        
    return es

tower = grid_tow(size, n)

