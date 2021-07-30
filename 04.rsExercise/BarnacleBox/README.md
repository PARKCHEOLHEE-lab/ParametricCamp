## RhinoPython Exercise

1. Theme | Barnacle Box<br>

   - _Barnacle Box (따개비가 가진 패턴을 단순화시킨 박스의 입면 모델링)_
   - _Parameter : Number of Grid : `rNum`, Grid Size : `size`_
<p align="center"><img src='https://user-images.githubusercontent.com/83874157/127636752-2c1ea9b7-8121-465d-8ac3-4ff46de9e38d.gif' border='0' width='1000px'></p><br>

   
2. Inspired Image<br>

<p align='center'><img src='https://bqekeeper.files.wordpress.com/2019/12/dsc02103.jpg?w=500&h=375' border='0' width='550px'></p><br>


3. Core Methods<br>

   - _`Scale` `CurveAreaCentroid` `RotateObjects` `coercegeometry` `coerce3dpoint` `MoveObject`_
   - _`rhinoscriptsyntax` 라이브러리로 만들어진 지오메트리들을 `ghpythonlib.components`의 오브젝트로 사용하려면 타입을 변환시켜줘야 하는데, `coercegeometry` `coerce3dpoint` 메소드를 사용하면 타입변환이 가능하다._<br><br>

4. Python Code ▼
  ```
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import random as r

I = rg.Interval
box = rg.Box(rg.Plane.WorldXY, I(0, size*rNum), I(0, -size*rNum), I(3, size*rNum-2))

rec = rs.AddRectangle(rg.Plane.WorldZX, size, size)
srf = rs.AddPlanarSrf(rec)
recs = []
srfs = []
for i in range(rNum):
    for j in range(rNum):
        recs.append(rs.coercegeometry(rs.CopyObject(rec, [size*i,0,size*j])))
        srfs.append(rs.CopyObject(srf, [size*i,0,size*j]))

cpts = []
for i in range(len(recs)):
    cpts.append(rs.coerce3dpoint(rs.CurveAreaCentroid(recs[i])[0]))

sRecs = []
for i in range(len(recs)):
    sRec = gh.Scale(recs[i], cpts[i], r.uniform(0.2, 0.5))[0]
    rs.MoveObject(sRec, [0,r.randint(int(size*rNum/rNum), int(size*rNum/rNum*2)),0])
    sRecs.append(sRec)

loft = []
for i in range(len(recs)):
    lo = [recs[i], sRecs[i]]
    loft.append(rs.AddLoftSrf(lo)[0])

barnacle = []
rotP = [size*rNum/2,-size*rNum/2,0]
for i in range(4):
    for j in range(len(recs)):
        barnacle.append(rs.RotateObjects(loft[j], rotP, 90*i, copy=True)[0])
        barnacle.append(rs.RotateObjects(srfs[j], rotP, 90*i, copy=True)[0])
   ```
<br>

   5. Postscript<br>

        - _패턴의 크기와 높이가 랜덤하게 생성되도록 설정하였으나, 예측가능한 범위의 패턴이 만들어진다._
        - _단조롭지만, 예측가능한 패턴은 우리에게 안정감을 준다._