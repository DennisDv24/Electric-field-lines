import numpy as np
import matplotlib as mpl
import scipy
from scipy import spatial


class punctualFieldIntensity:

    def __init__(self, point, chargesInputList):
        self.value= point #compute here

    def getValue(self):
        return self.value

class electricField(punctualFieldIntensity):
    def __init__(self, space, chargesInputList):
        self.charges = chargesInputList

        self.values = []
        for points in space:
            self.values.append(punctualFieldIntensity(points, chargesInputList).getValue())

    def getValues(self):
        return self.values



class charge:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos


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