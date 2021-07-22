## RhinoPython Exercise

1. Theme | 3D Matrix Wall<br>

   - _Random Extrude Facade Generating (돌출된 형태가 무작위로 변하는 파사드 만들기)_
   - _parameter : 돌출될 그리드의 개수(imax, kmax), 돌출될 그리드의 크기(grasshopper component)_
<p align="center"><img src='https://user-images.githubusercontent.com/83874157/126640873-9d0b6dea-15de-4cba-b420-92ecbab2b8b0.gif' border='0' width="800px"></p><br>
   
2. Python Code ▼
  ```
import ghpythonlib.components as gh
import random as rnd

ptDict = {}
crvBacks = []
crvFronts = []
midPts= []

def midPt(pt01, pt02):
    midPt = gh.ConstructPoint((pt01[0] + pt02[0]) / 2,(pt01[1] + pt02[1]) / 2,(pt01[2] + pt02[2]) / 2)
    midPts.append(midPt)
    return midPt

def pointMatrix(imax, jmax, kmax):
    for i in range(imax):
        for j in range(jmax):
            for k in range(kmax):
                if j == 0:
                    x = i*5 + (rnd.random()*5)
                    y = j*5
                    z = k*5 + (rnd.random()*5)
                    point = gh.ConstructPoint(x, y, z)
                    ptDict[(i,j,k)] = point
                else:
                    x = i*5
                    y = j*5
                    z = k*5
                    point = gh.ConstructPoint(x, y, z)
                    ptDict[(i,j,k)] = point
                    
    for i in range(imax):
        for j in range(jmax):
            for k in range(kmax):
                if i>0 and j>0 and k>0:
                    crvBack = gh.PolyLine((ptDict[(i,j,k)], ptDict[(i-1,j,k)],
                    ptDict[(i-1,j,k-1)], ptDict[(i,j,k-1)], ptDict[(i,j,k)]), 0)
                    crvBacks.append(crvBack)
                    crvFront = gh.PolyLine((ptDict[(i,j-1,k)], ptDict[(i-1,j-1,k)],
                    ptDict[(i-1,j-1,k-1)], ptDict[(i,j-1,k-1)], ptDict[(i,j-1,k)]), 0)
                    crvFronts.append(crvFront)
                    midPt(ptDict[(i-1,j-1,k-1)], ptDict[(i,j-1,k)])


pointMatrix(imax, jmax, kmax)

  a = stepList
   ```
<br>

3. Authorship<br>

   - _https://www.youtube.com/watch?v=NjL4cNp7ciU&t=830s_
   
