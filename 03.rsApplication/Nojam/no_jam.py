import math
import random
import Rhino.Geometry as rg
import Rhino.RhinoDoc as rc
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh

random.seed(seed)
generation = 0
sub_generation = 0
circulation = []

while generation < iteration:
    # start point
    if generation == 0:
        location = rg.Point3d(0,0,0)
        circulation.append(location)
        
    action = random.randint(0,3)
    if action == 0:
        location = location + rg.Point3d(-1,0,0)
    elif action == 1:
        location = location + rg.Point3d(0,1,0)
    elif action == 2:
        location = location + rg.Point3d(1,0,0)
    elif action == 3:
        location = location + rg.Point3d(0,-1,0)
    
    if location in circulation:
        if sub_generation <= 100:
            location = circulation[-1]
            sub_generation += 1
            continue
        else:
            sub_generation = 0
            
    
    circulation.append(location)
    
    generation += 1
