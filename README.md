# Parametric Camp<br>
1. Parametric Design<br>
   - _각각의 parameter들 즉 데이터들간의 **관계 · 의존 · 상호작용** 등을 설정하여 디자인 하는 방식 및 프로세스_
   - _parameter : 프로그램의 개개의 작업에 적용할 경우에 필요한 수치 정보(데이터)_<br><br>


2. Generative Design<br>
   - _특정 제약 조건을 충족하는 특정 수의 출력을 생성하는 프로그램과 특정 출력을 선택하거나 입력 값, 범위 및 분포를 변경하여 실행 가능한 영역을 미세 조정하는 반복적인 디자인 방식 및 프로세스_
   - _매개변수와 설계목표를 입력하고 설계대안의 순열을 모두 탐색하고 생성_<br><br>


## Parametric Design Preview
1. [Recursive Stair](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/RecursiveStair) ▼<br>

   - _Parametric Recursive Stair Generating (파라메트릭한 원형계단 만들기)_
   - _parameter : 계단의 길이(x), 너비(y), 높이(z), 단 수(steps), 회전각도(angle))_
<p align="center"><a href='https://ifh.cc/v-chGKXl' target='_blank'><img src='https://ifh.cc/g/chGKXl.gif' border='0' width="500px"></a></p>
   
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
<br>

## Generative Design Preview
1. [Generative Form](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/03.rsApplication/GenerativeForm) ▼<br>
   
   
