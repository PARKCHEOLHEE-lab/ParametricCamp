## RhinoPython Exercise

1. Theme | Dom-Ino System<br>

   - _Stacked Dom-Ino System (Dom-Ino System이 적층되는 구조 모델)_
   - _Parameter : Slab Size `slabX, slabY`, Number of Floors `floor`_
<p align="center"><img src='https://user-images.githubusercontent.com/83874157/127106273-ade8962e-b30b-44ec-a855-822753a7e927.gif' border='0' width='1000px'></p><br>

   
2. Reference Image<br>

<p align='center'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/La_maison_Dom-ino_de_Le_Corbusier_%28Biennale_d%27architecture_2014%2C_Venise%29_%2814938729273%29.jpg/640px-La_maison_Dom-ino_de_Le_Corbusier_%28Biennale_d%27architecture_2014%2C_Venise%29_%2814938729273%29.jpg' border='0' width='275px'>　<img src='https://i.pinimg.com/600x315/44/e4/66/44e4669c1d006fc84ff38075881b3f14.jpg' border='0' width='550px'></p><br>


3. Core Methods<br>

   - _`DomainBox, TrimBrep, DivideSurface, DeconstructBrep`_<br><br>

4. Python Code ▼
  ```
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import math

I = rg.Interval
slabZ = 1.5

slab = rg.Box(rg.Plane.WorldXY, I(0, slabX), I(0, slabY/2), I(0, slabZ))
slabSrf = gh.DeconstructBrep(slab)[0][5]
columnsBase = gh.DivideSurface(slabSrf, 11, 5)[0]
columnsIdx = [7, 10, 31, 34, 55, 58]
ln = rs.AddCurve([columnsBase[59], columnsBase[56], columnsBase[68]], 1)
trimSrf = rs.ExtrudeCurve(ln, rs.AddLine([0,0,0],[0,0,-slabZ]))
slab = rs.TrimBrep(rs.MoveObjects(slab, [0,0,0])[0], trimSrf)

columns = []
foundation = []
for i in columnsIdx:
    column = gh.DomainBox(columnsBase[i], 1,1,15-slabZ)
    rs.MoveObject(column, [-0.5,-0.5,0])
    columns.append(column)
    
    found = gh.DomainBox(columnsBase[i], 5,5,-3-slabZ)
    rs.MoveObject(found, [-2.5,-2.5,-slabZ])
    foundation.append(found)


cols = []
slbs = []
for i in range(len(columns)):
    for j in range(1, floor):
        cols.append(rs.CopyObject(columns[i], [0,0,(j-1)*15]))
        slbs.append(rs.CopyObject(slab, [0,0,j*15]))
        

stepDis = rs.Distance(columnsBase[62], columnsBase[68])
steps = []
columnsBase[58][2] = 9.5
for i in range(8):        
    step1 = gh.DomainBox(columnsBase[68], -stepDis,stepDis/2,1)  
    step2 = gh.DomainBox(columnsBase[58], stepDis,-stepDis/2,1)    
    if i == 7:
        step1 = gh.DomainBox(columnsBase[68], -stepDis*2,stepDis*1.3,1)
    steps.append(rs.CopyObject(step1, [0,i*stepDis/3.5,i*1]))    
    steps.append(rs.CopyObject(step2, [0,-i*stepDis/3.5,i*1]))
    
    if len(steps) >= 15:
        steps.pop(15)


stps = []
for i in range(len(steps)):
    for j in range(1, floor):  
        stps.append(rs.CopyObject(steps[i], [0,0,(j-1)*15]))
   ```
<br>

   5. Bad Point<br>

        - _지저분한 Code_
        - _Parameter간의 관계가 유기적이지 못함_
        - _쉽게 갈 수 있는 방법이 있을 듯 한데 너무 돌아간듯_
   
