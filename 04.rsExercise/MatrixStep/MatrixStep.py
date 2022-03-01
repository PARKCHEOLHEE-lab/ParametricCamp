import Rhino.Geometry as rg
import Rhino.RhinoDoc as rc
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

matrix_step = []

for i in range(maxtrix_count):
    z = i * height
    
    for j in range(maxtrix_count):
        step_base = rg.Point3d(i*scale, j*scale, z)
        step_rec = gh.Rectangle(step_base, scale, scale, 0).rectangle
        step_srf = gh.BoundarySurfaces(step_rec)
        step_vec = rg.Point3d(0, 0, -z)
        
        step = gh.Extrude(step_srf, step_vec)
        
        z = z + height
        
        matrix_step.append(step)