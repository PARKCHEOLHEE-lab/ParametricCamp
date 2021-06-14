import rhinoscriptsyntax as rs
import Rhino as r

def dis2(p0, p1):
    pos0 = rs.PointCoordinates(p0)
    pos1 = rs.PointCoordinates(p1)
    dis = (pos1[0] - pos0[0]) * (pos1[0] - pos0[0]) + (pos1[1] - pos0[1]) * (pos1[1] - pos0[1]) + (pos1[2] - pos0[2]) * (pos1[2] - pos0[2])
    return dis

pos0 = rs.PointCoordinates(p0)
pos1 = rs.PointCoordinates(p1)

x_interval = (pos1[0] - pos0[0]) / (x_num - 1)
y_interval = (pos1[1] - pos0[1]) / (y_num - 1)
pts = []

for i in range(x_num):
    for j in range(y_num):
        x = pos0[0] + x_interval * i 
        y = pos0[1] + y_interval * j
        z = 0

        if mode == 0:
            if (i * j) & 2 == 0:
                p = rs.AddPoint(x, y, z)            
                pts.append(p)

        elif mode == 1:
            if (i*j + i*j) & 2 == 0:
                p = rs.AddPoint(x, y, z)            
                pts.append(p)
            
        elif mode == 2:
            if (i*j - i*j) & 2 == 0:
                p = rs.AddPoint(x, y, z)            
                pts.append(p)

        elif mode == 3:
            if (i*j - i-j) & 2 == 0:
                p = rs.AddPoint(x, y, z)            
                pts.append(p)

lns = []

#for j in range(len(pts)-1):
#    p0 = pts[j]
#    for i in range(j, len(pts)):
#        p1 = pts[i]
#        dis = dis2(p0, p1)
#        if dis < 10:
#            pos0 = rs.PointCoordinates(p0)
#            pos1 = rs.PointCoordinates(p1)
#            ln = r.Geometry.Line(pos0, pos1)
#            lns.append(ln)

#for j in range(len(pts)-1):
#    p0 = pts[j]
#    for i in range(j, len(pts)):
#        p1 = pts[i]
#        dis = dis2(p0, p1)
#        if dis < 10 and dis > 0:
#            ln = rs.AddLine(p0, p1)
#            lns.append(ln)
#            
for j in range(len(pts)-1):
    p0 = pts[j]
    for i in range(j, len(pts)):
        p1 = pts[i]
        dis = dis2(p0, p1)
        if dis < 10:
            if p0 != p1:
                ln = rs.AddLine(p0, p1)
                lns.append(ln)

a = pts
b = lns