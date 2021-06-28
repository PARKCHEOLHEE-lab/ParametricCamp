import Rhino

grass = Rhino.RhinoApp.GetPlugInObject('Grasshopper')
for i in range(1, 7):
    grass.SetSliderValue('212adde4-a3cd-4067-9c7b-7cb3b1f1e04f', i)
    
    for j in range(10):
        grass.SetSliderValue('6c7417f5-a238-48a7-999c-9c14bd5c6373', j)
        grass.SetSliderValue('a90ec69b-5d2a-47f6-93cc-bb46bc5796a7', i*17)
        grass.SetSliderValue('d74bd39d-2480-4c3e-b1e5-c46901020956', j*17)
        grass.RunSolver('GenerativeForm.gh')
        grass.BakeDataInObject('a47fea54-e7bb-438d-ade9-3a48e80ca7ab')