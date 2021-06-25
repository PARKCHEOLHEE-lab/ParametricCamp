import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

boxes = []
i = rg.Interval

for x in range(0, x_num, step):
    for y in range(0, y_num, step):
        for z in range(0, z_num, step):
            size = step / 3
            box = rg.Box(rg.Plane.WorldXY, i(x, x+size), i(y, y+size), i(z, z+size))
            boxes.append(box)

a = boxes