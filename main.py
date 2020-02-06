from fieldcalc import * 
from matplotlib import rc
import matplotlib.pyplot as plt


rc('text', usetex=True)

fig, ax = plt.subplots()


"""""
s=[[[0,1],[1,1]],
   [[0,0],[1,0]]]
"""""
charges = [charge(0.000000005, [-5,0]), charge(-0.000000005,[5,0]), charge(-0.0000000005,[-3,2]), charge(-0.000000005,[0,3])]

x = np.linspace(-10,10,20)
y = np.linspace(-10,10,20)

X,Y = np.meshgrid(x,y)

S=[]

for i in range(len(X)):

    S.append([])

    for j in range(len(X[0])):

        S[i].append([X[j][i],Y[j][i]])


np.set_printoptions(suppress=True)

field = electricField(S,charges)

"""""
print(field.charges)
print('----')
print(np.array(field.space))
print('----')
"""""
E = field.values
"""""
print(np.array(E))
print('----')
"""""
#print(np.array(field.getField()))

ax.set_xlim(-11,11)
ax.set_ylim(-11,11)

fz=20


ax.text(charges[0].pos[0],charges[0].pos[1], r'$\oplus$', fontsize = fz,  ha='center', va='center')
ax.text(charges[1].pos[0],charges[1].pos[1], r'$\ominus$', fontsize = fz,  ha='center', va='center')


for i in range(len(S)):
   for j in range(len(S[0])):
      ax.arrow(S[i][j][0], S[i][j][1], E[i][j][0], E[i][j][1], head_width=0.1, head_length=0.1)

"""""
print('----')

def linesCalc(values, space, valToCompare):
   linePoints = []
   for i in range(len(values)):
      for j in range(len(values[0])):
         if round(values[i][j][2],1) == valToCompare:
            linePoints.append(space[i][j])

   return linePoints     
"""""

"""""
vals = []
for i in range(-10,10):
   vals.append(i/10)
print(vals)

for val in vals:
   print(val)
   p = np.transpose(linesCalc(field.values, S, val))
   ax.scatter(p[0],p[1])



p1 = np.transpose(linesCalc(field.values, S, 0.1))
p2 = np.transpose(linesCalc(field.values, S, 0.2))
p3 = np.transpose(linesCalc(field.values, S, 0.3))
p4 = np.transpose(linesCalc(field.values, S, 0.4))
ax.scatter(p1[0],p1[1])
ax.scatter(p2[0],p2[1])
ax.scatter(p3[0],p3[1])
ax.scatter(p4[0],p4[1])
"""""

plt.show()