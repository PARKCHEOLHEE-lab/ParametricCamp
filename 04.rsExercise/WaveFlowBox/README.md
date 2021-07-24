## RhinoPython Exercise

1. Theme | Wave Flow Box<br>

   - _Parametric Upper Face Box (상부 면이 Wave Flow 형태로 변화하는 박스 만들기)_
   - _parameter : 박스 및 WaveFlow의 높이(minZ, maxZ), 박스의 크기(pNum, scale)_
<p align="center"><img src='https://user-images.githubusercontent.com/83874157/126857674-d50f6a67-d379-444a-be78-2dac020ade17.gif' border='0' width='1000px'></p><br>

   
2. Python Code ▼
  ```
import rhinoscriptsyntax as rs
import Rhino.Geometry as rg
import ghpythonlib.components as gh
import random as r
import Rhino

pts = []
for i in range(pNum+1):
    for j in range(pNum+1):
        pt = rs.AddPoint(i*scale, j*scale, r.randint(minZ, maxZ))
        pt = rs.PointCoordinates(pt)
        pts.append(pt)

srf = gh.SurfaceFromPoints(pts, pNum+1, False)
box = gh.DomainBox(rg.Plane.WorldXY, pNum*scale, pNum*scale, pNum*scale)
box = rs.MoveObject(box, [0,0,0])

rs.TrimBrep(box, srf)
   ```

   
   
