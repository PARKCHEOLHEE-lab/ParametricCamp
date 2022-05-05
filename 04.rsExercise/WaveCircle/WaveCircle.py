import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

origin = rg.Point3d(150,0,0)
circle = rg.Circle(origin, radius)
divide_pts = gh.DivideCurve(circle, divide_count, False).points

moved_divide_pts = []
for i, p in enumerate(divide_pts):
    if i % 2 == 0:
        rs.MoveObject(p, [0,0,radius/5])

