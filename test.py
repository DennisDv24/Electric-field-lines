x=[[[1,2],[2,3],[3,4]],
   [[4,5],[5,6],[6,7]]]
y=[[],[]]
for rows in x:
    for points in rows:
        y=[rows, points]

print(y)