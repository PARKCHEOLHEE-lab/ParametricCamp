import rhinoscriptsyntax as rs
import Rhino.Geometry as rg


boxes = []
i = rg.Interval
size = step*0.95

for x in range(0, x_num, step):
    for y in range(0, x_num, step):
        for z in range(0, z, step):    # z & parameter z same variable name I don't know why it's performance like this.
            box = rg.Box(rg.Plane.WorldXY, i(x, x+size), i(y, y+size), i(z, z+size))
            boxes.append(box)

a = boxes
print(boxes)