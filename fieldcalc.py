import numpy as np
import matplotlib as mpl
import math

import copy

def pointsAngle(P, Pv):

    Pf = np.array(P)
    Pvf = np.array(Pv) 
    vi = [1,0]
    v = Pf-Pvf
    angle = math.atan2(np.linalg.det([vi,v]), np.dot(vi,v))

    return angle


def punctualFieldIntensity(point, chargesInputList):

    absValue = 0
    value = [0,0]
    k=9*10**9

    for i in range(len(chargesInputList)):
        
        dist = np.linalg.norm(np.array(point) - np.array(chargesInputList[i].pos))
        absValue = k*chargesInputList[i].val/dist**2

        angle = pointsAngle(chargesInputList[i].pos, point)

        value[0] += absValue*np.cos(angle)
        value[1] += absValue*np.sin(angle)

    return value #must be a vector (2 elements array)

class electricField:
    
    def __init__(self, space, chargesInputList):

        self.charges = chargesInputList
        self.space = space
        self.values = copy.deepcopy(self.space)

        self.calculate()

    def calculate(self):

        for i in range(len(self.space)):
            for j in range(len(self.space[0])):
                self.values[i][j] = punctualFieldIntensity(self.space[i][j], self.charges)

    def getField(self):
        return [self.space, self.values]

class charge:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos



"""""
x=np.linspace(-10,10,5)
y=np.linspace(-10,10,5)

X,Y = np.meshgrid(x,y)
k=9*10**9
charges = [charge(-1, [0,0]), charge(1,[0,2])]

print(E(charges, 0, 1))

print(E([charge(1,[0,0])], 1, 1))
"""""
