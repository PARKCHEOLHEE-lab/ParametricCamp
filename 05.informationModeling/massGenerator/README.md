## Information Modeling

1. Theme | Mass Generator<br>

   - _건물 정보가 담긴 *.csv 파일기반의 주변매스 자동 생성기_
   - _Parameter : 건물의 높이 : `height` `h`_

<p align="center"><img src='https://user-images.githubusercontent.com/83874157/127735271-9e5eb9fc-d246-47d0-ad0b-70d573a32a52.gif' border='0' width='1000px'></p><br>

   
2. Inspired Things<br>

   - _QGIS에서 추출한 *.shp 파일은 개별 건물의 polygon coordination과 height 등의 정보를 가진다.(area, numbor of floor, regist day, structure code 등)_
   - _DataFrame이 가진 데이터를 기반으로 모델링에 정보를 담아보고자 했다._

<p align='center'><img src='https://user-images.githubusercontent.com/83874157/127735496-6f90462e-e80f-4766-b89f-d4ab1124ce57.PNG'></p><br>


3. Manual<br>

   - _QGIS로부터 *.shp 파일 추출_
   - _필요시 geoPandas를 통해 전처리_
   - _`geoPandas.to_csv()` 적절한 위치에 저장_
   - _`massGenerator.gh` 파일을 실행시키고 *.csv 파일의 경로 지정_
   - _~~geoPandas를 거쳐서 *.csv 파일이 만들어지다보니, 모든 데이터가 `string` 타입으로 변환되어버렸다. geoPandas를 거치지 않고 *.csv파일 Parsing을 시도했으나, 실패... 코드 수정이 필요하겠다...~~_<br><br>

4. Python Code ▼
```
import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import random as r

file = open(teheran, "r")
columns = file.readline().split(",")
columns = columns[1:]
data = file.readlines()
file.close()

massInfo = []
for i in range(len(data)):
    height = data[i].replace("\n", "").split("POLYGON")[0]
    height = float(height.split(",")[10])
    if height >= 1000:
        height = 0
    elif height == 0:
        height = r.uniform(1.8, 5.3)
        
    polygon = data[i].replace("\n", "").split("POLYGON")[1]
    polygon = polygon.replace("(", "").replace(")", "").replace('"', "").replace(",", "").strip()
    polygon = map(float, polygon.split(" "))
    
    massInfo.extend([[polygon, height]])

pts = []
for i in range(len(massInfo)):
    for j in range(0, len(massInfo[i][0])-1, 2):
        pts.append(rs.AddPoint(massInfo[i][0][j], massInfo[i][0][j+1], 0))

CRV = []
s = 0
for i in range(len(massInfo)):
    pCount = int(len(massInfo[i][0])/2)
    if i == 0:
        s += pCount
        Pts = pts[:pCount]
        CRV.append(rs.AddCurve(Pts, 1))
    else:
        s += pCount
        Pts = pts[s-pCount:s]
        CRV.append(rs.AddCurve(Pts, 1))

bdgs = []
H = []
for i in range(len(massInfo)):
    h = massInfo[i][1]
    if h >= 400:
        h = r.uniform(1.8, 5.3)
        
    base = CRV[i]
    path = rs.AddLine(rs.AddPoint(0,0,0), rs.AddPoint(0,0,h))
    
    building = rs.ExtrudeCurve(base, path)
    rs.CapPlanarHoles(building)
    bdgs.append(building)
    H.append(h)

#H.sort(reverse=True)
#print(H[:3])
```

<br>

   5. Issue<br>

        - _DataFrame상에 존재하지 않는 높이값이 튀어나온다._
        - _Parsing하는 과정에서 문제는 없었는데, 어디서 튀어나온건지 찾지못했다._
        - _임시방편으로 높이가 과하게 높은 녀석들을 `h = r.uniform(1.8, 5.3)`으로 지정해주었다._

<p align='center'><img src='https://user-images.githubusercontent.com/83874157/127736281-50310909-bb58-4e1a-8391-df5f6383fcfa.PNG' width='1000px'></p><br>


   6. Postscript<br>

        - _고도값이 반영되지 않은 모델링이라 지형과 같이 생성할 시에 건물의 위치를 재조정해주어야 한다._
        - _Issue 파트에서 다뤘던 문제의 해결방법 또는 더 효율적인 코드 제안 부탁드립니다._