from fieldcalc import * 

s=[[[0,1],[1,1]],
   [[0,0],[1,0]]]
charges = [charge(1, [-1,0]), charge(1,[2,2])]

field = electricField(s,charges)
print(field.charges)
print('----')
print(np.array(field.space))
print('----')
print(np.array(field.values))
print('----')
print(np.array(field.getField()))