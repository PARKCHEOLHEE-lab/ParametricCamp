## RhinoPython Exercise

1. Theme | Wave Ceiling Louver<br>

   - _Wave Ceiling Louver (스크린루버 파라메트릭 모델링)_
   - _Parameter : Length of Ceiling : `length`, Interval of  Louver : `interval`_
<p align="center"><img src='https://user-images.githubusercontent.com/83874157/127772866-79425125-a23d-4c15-9c6d-0efddf6d7c95.gif' border='0' width='1000px'></p><br>

   
2. Reference Image<br>

<p align='center'><img src='https://i.pinimg.com/564x/fe/d8/5c/fed85c71ea31a89f52c889f598e6b5d6.jpg' border='0' width='250px'>　<img src='https://frasch.co/wp-content/uploads/2019/10/IMG_4132.jpg' border='0' width='277px'></p><br>


3. Core Methods<br>

   - _`SurfaceFromPoints` `SplitBrep` `ExtrudeSurface` `DivideLength`_<br><br>

4. Python Code ▼
  ```
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import random as r

r.seed(0)

pts = []
uv = 10
for i in range(uv):
    for j in range(length):
        pt = rs.AddPoint(i*5,j*interval,0)
        rs.MoveObject(pt, [0,0,r.uniform(13.0, 20.0)])
        pt = rs.PointCoordinates(pt)
        pts.append(pt)

srf = gh.SurfaceFromPoints(pts, uv, False)

rec = rs.AddRectangle(rg.Plane.WorldZX, uv*5-30, uv*5-5)
recs = []
louvers = []
for i in range(length):
    crec = rs.CopyObject(rec, [0,i*interval,0])
    louver = rs.AddPlanarSrf(crec)
    
    if i == 0:
        louver = rs.SplitBrep(louver, srf)[1]
    else:
        louver = rs.SplitBrep(louver, srf)[0]
    
    louver = rs.ExtrudeSurface(louver, rs.AddLine(rs.AddPoint(0,0,0), rs.AddPoint(0,0.3,0)))
    recs.append(crec)
    louvers.append(louver)

fBase = gh.DivideLength(rs.coercecurve(recs[0]), 6.1)[0]
fBase = [fBase[5], fBase[7], fBase[9]]
hFrame = gh.DomainBox(fBase, 0.5, length*interval-interval, 0.5)
vBase = gh.DomainBox(fBase, 0.1, 0.1, 7)

vFrame = []
for i in range(int(interval)-1, length, int(interval)):
    for j in range(len(fBase)):
        vFrame.append(rs.CopyObjects(vBase, [0,i*interval,0])[j])
   ```
<br>

   5. Postscript<br>

        - _주어진 천장의 길이 내에서 루버의 개수가 조절되게 하는 제약조건 및 파라미터 필요_