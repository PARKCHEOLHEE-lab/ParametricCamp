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