import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random

pts = []


for x in range(x_num):
    for y in range(y_num):
        p = rs.AddPoint(x*10, y*10, 0)
        p = rs.PointCoordinates(p)
        pts.append(p)


box_list = []
box_size = 0.8
for x in range(x_num):
    for y in range(y_num):
#        box_size = (x/x_num + y/y_num) / 3
        box = rg.Box(rg.Plane.WorldXY, rg.Interval(x, x+box_size), rg.Interval(y, y+box_size), rg.Interval(0, random.randrange(1, 7)))
        box_list.append(box)
    
b = box_list