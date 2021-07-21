## RhinoPython Exercise

1. Theme | Recursive Stair<br>
   - _Parametric Recursive Stair Generating (파라메트릭한 원형계단 만들기)_
   - _parameter : 계단의 길이(x), 너비(y), 높이(z), 단 수(steps), 회전각도(angle))_
<p align="center"><a href='https://ifh.cc/v-chGKXl' target='_blank'><img src='https://ifh.cc/g/chGKXl.gif' border='0' width="500px"></a>　<a href='https://ifh.cc/v-JBVajY' target='_blank'><img src='https://ifh.cc/g/JBVajY.png' border='0' width="412px"></a></p>
   
2. Python Code ▼
  ```
  import rhinoscriptsyntax as rs
  import Rhino.Geometry as geo
  import scriptcontext as sc

  stepList = []

  for i in range(steps):
      if i == steps-1:
          step = rs.AddRectangle(rs.WorldXYPlane(), x, x)
      else:
          step = rs.AddRectangle(rs.WorldXYPlane(), x, y)
      step = rs.AddPlanarSrf(step)
      step = rs.ExtrudeSurface(step, rs.AddLine([0,0,0], [0,0,z]))
      step = rs.RotateObject(step,[0,0,0],angle*i)
      stepList.append(rs.CopyObject(step, [0,0,z*i]))

  a = stepList
   ```

   
   
