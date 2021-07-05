import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random as r

all_pts = []
for i in range(10):
    for j in range(10):
        for k in range(30):
            p = rs.AddPoint(i*5,j*5,k*5)
            all_pts.append(p)

dis_pts = []
dis_lns = []
for i in range(len(all_pts)):
    dis = rs.Distance(attractor, all_pts[i])
    if dis >= x:
        dis_pts.append(all_pts[i])
    else:
        dis_lns.append(rs.AddLine(attractor, all_pts[i]))

sph = rs.AddSphere(attractor, dis/4)

a = dis_pts
b = sph
# c = dis_lns