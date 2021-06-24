import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import random

random.seed(seed)

x_size = random.randrange(5, 50)
y_size = random.randrange(5, 50)
z_size = random.randrange(5, 50)


box = rg.Box(rg.Plane.WorldXY, rg.Interval(0, x_size), rg.Interval(0, y_size), rg.Interval(0, z_size))
a = box