import rhinoscriptsyntax as rs
import Rhino.Geometry as geo
import scriptcontext as sc

stepList = []

for i in range(steps):
    if i == steps-1:
        step = rs.AddRectangle(rs.WorldXYPlane(), x, y)
    else:
        step = rs.AddRectangle(rs.WorldXYPlane(), x, y)
    step = rs.AddPlanarSrf(step)
    step = rs.ExtrudeSurface(step, rs.AddLine([0,0,0], [0,0,z]))
    step = rs.RotateObject(step,[0,0,0],angle*i)
    stepList.append(rs.CopyObject(step, [0,0,z*i]))

a = stepList