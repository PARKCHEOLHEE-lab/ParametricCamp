import random
import Rhino.Geometry as rg


if run:
    if reset:
        iteration = 0
        seed = random.randint(0, 500)
    else:
        random.seed(seed)
        generation = 0
        sub_generation = 0
        circulation = []
        
        iteration += 1
        while generation < iteration:
            # start point
            if generation == 0:
                location = rg.Point3d(0,0,0)
                circulation.append(location)
                
            action = random.randint(0,3)
            if action == 0:
                location = location + rg.Point3d(-10,0,0)
            elif action == 1:
                location = location + rg.Point3d(0,10,0)
            elif action == 2:
                location = location + rg.Point3d(10,0,0)
            elif action == 3:
                location = location + rg.Point3d(0,-10,0)
            
            # overlapped circulation
            if location in circulation:
                if sub_generation <= 30:
                    location = circulation[-1]
                    sub_generation += 1
                    continue
                else:
                    sub_generation = 0
            
            circulation.append(location)
            
            curr_vector = circulation[-1] - circulation[-2]
            anchor = circulation[-2]
            
            generation += 1
    
else:
    iteration = 0
