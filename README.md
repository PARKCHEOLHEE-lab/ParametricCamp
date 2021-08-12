# Parametric Camp<br>

1. Research Library<br>

   - <img src="https://img.shields.io/badge/rhino-2d2f34?style=for-the-badge&logo=rhinoceros&logoColor=white"/> <img src="https://img.shields.io/badge/rhinoscriptsyntax-2d2f34?style=for-the-badge&logo=rhinoceros&logoColor=white"/> <img src="https://img.shields.io/badge/ghpythonlib-2d2f34?style=for-the-badge&logo=rhinoceros&logoColor=white"/><br><br>
   
   
2. Parametric Design<br>
   - _각각의 parameter들 즉 데이터들간의 **관계 · 의존 · 상호작용** 등을 설정하여 디자인 하는 방식 및 프로세스_
   - _parameter : 프로그램의 개개의 작업에 적용할 경우에 필요한 수치 정보(데이터)_<br><br>


3. Generative Design<br>
   - _특정 제약 조건을 충족하는 특정 수의 출력을 생성하는 프로그램 디자인 방식 및 프로세스_
   - _특정 출력을 선택하거나 입력 값, 범위 및 분포를 변경하여 실행 가능한 영역을 미세 조정하는 반복적인 디자인 방식 및 프로세스_
   - _매개변수와 설계목표를 입력하고 설계대안의 순열을 모두 탐색하고 생성_<br><br>


## Parametric Design Preview
1. [Recursive Stair](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/RecursiveStair) ▼<br>

   - _Parametric Recursive Stair Generating (파라메트릭한 원형계단 만들기)_
   - _parameter : 계단의 길이(x), 너비(y), 높이(z), 단 수(steps), 회전각도(angle)_
<p align="center"><a href='https://ifh.cc/v-chGKXl' target='_blank'><img src='https://ifh.cc/g/chGKXl.gif' border='0' width="380px"></a>　<a href='https://ifh.cc/v-JBVajY' target='_blank'><img src='https://ifh.cc/g/JBVajY.png' border='0' width="312px"></a></p><br>
   
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

2. Preview List

   - [ 　[3d Matrix Wall](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/3dMatrixWall)　|　[Wave Flow Box](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/blob/master/04.rsExercise/WaveFlowBox/README.md)　|　[Mahanakhon](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/Mahanakhon)　|　[Dom-Ino System](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/Dom-InoSystem)　|　[Barnacle Box](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/BarnacleBox)　|　[Wave Ceiling Louver](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/Louver)　|　[The Couch](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/04.rsExercise/TheCouch) 　]
 
<br>

## Generative Design Preview
1. [Generative Form](https://github.com/PARKCHEOLHEE-lab/ParametricCamp/tree/master/03.rsApplication/GenerativeForm) ▼<br>

   - _parameter설정 후 원하는 조건들에 해당하는 모든 volume 생성하기_
   - _설정한 조건 : 원하는 volume의 개수, volume별 좌표, volume의 회전값 등_
<p align="center"><img src='https://user-images.githubusercontent.com/83874157/126615653-6375512c-5b3c-42d3-9887-e6a8f6f2986e.gif' border='0' width="900px"></a></p><br>

2. python code ▼
```
import Rhino

grass = Rhino.RhinoApp.GetPlugInObject('Grasshopper')
for i in range(1, 10):
    grass.SetSliderValue('212adde4-a3cd-4067-9c7b-7cb3b1f1e04f', i)
    
    for j in range(10):
        grass.SetSliderValue('6c7417f5-a238-48a7-999c-9c14bd5c6373', j)
        grass.SetSliderValue('a90ec69b-5d2a-47f6-93cc-bb46bc5796a7', i*25)
        grass.SetSliderValue('d74bd39d-2480-4c3e-b1e5-c46901020956', j*25)
        grass.RunSolver('GenerativeForm.gh')
        grass.BakeDataInObject('a47fea54-e7bb-438d-ade9-3a48e80ca7ab')
```

   
