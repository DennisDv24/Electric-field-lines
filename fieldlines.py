import numpy as np
import matplotlib as mpl
import scipy
from scipy import spatial


def E(charges, x, y):
    for i in range(len(charges)):
        fieldValue = 0
        dist = spatial.distance.euclidean(charges[i].pos, [x,y] )
        fieldValue += k*charges[i].val/dist**2
    return fieldValue

class charge:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos

x=np.linspace(-10,10,5)
y=np.linspace(-10,10,5)

X,Y = np.meshgrid(x,y)
k=9*10**9
charges = [charge(-1, [0,0]), charge(1,[0,2])]

print(E(charges, 0, 1))

print(E([charge(1,[0,0])], 1, 1))

#those are abs vals, do it with proper vector analysis