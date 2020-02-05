import numpy as np
import matplotlib as mpl
import scipy
from scipy import spatial

def punctualFieldIntensity(point, chargesInputList):
    value = point[0]*chargesInputList[0]+point[1]*chargesInputList[1]
    return value

class electricField:
    def __init__(self, space, chargesInputList):

        self.charges = chargesInputList
        self.space = space
        self.values = []

        for rows in self.space:
            for points in rows:
                self.values.append(punctualFieldIntensity(points, self.charges))

    def getValues(self):
        return self.values

"""""
class charge:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
"""""

print(electricField([1,3,6], 5).getValues())

"""""
x=np.linspace(-10,10,5)
y=np.linspace(-10,10,5)

X,Y = np.meshgrid(x,y)
k=9*10**9
charges = [charge(-1, [0,0]), charge(1,[0,2])]

print(E(charges, 0, 1))

print(E([charge(1,[0,0])], 1, 1))
"""""
#those are abs vals, do it with proper vector analysis