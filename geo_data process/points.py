#!/usr/bin/env python
import random
import matplotlib.pyplot as plt

with open("points.txt","r") as points:
    borders = [[i for i in line.split(",")] for line in points]

d,x,y=[],[],[]
for i in range(len(borders)):
    if borders[i] != "\n":
        d.append(int(borders[i][0]))
        x.append(float(borders[i][1]))
        y.append(float(borders[i][2]))

x_r,y_r=[],[]
for i in range(len(borders)):
    x_r.append((x[i]-80000)/100)
    y_r.append(600-y[i]/100)
#plt.plot(x,y,x**2+y**2,"bp")
#plt.show()

#print sorted(random.sample(range(10),5))

for j in range(10):
    iforigin = 0
    x_r_j=[]
    y_r_j=[]
    with open('points%s.txt' % str(j),'w') as p_r:
        for i in range(len(x_r)):
            if d[i] == j and iforigin == 0:
                x_r_i = x_r[i]
                y_r_i = y_r[i]
                iforigin = 1
                p_r.writelines("------------------------------\n")
                p_r.writelines(str(x_r[i])+" "+str(y_r[i])+" 0"+"\n")
                p_r.writelines("------------------------------\n")
            elif d[i] == j and iforigin != 0:
                x_r_j.append(x_r[i]-x_r_i)
                y_r_j.append(y_r[i]-y_r_i)
        sample = sorted(random.sample(range(len(x_r_j)),int(0.3*len(x_r_j))))
        print len(x_r_j), len(sample)
        for i in range(len(sample)):
            p_r.writelines(str(x_r_j[sample[i]])+" "+str(y_r_j[sample[i]])+" 0"+"\n")

with open("points0.txt",'r') as divide:
    borders0 = [[i for i in line.split()] for line in divide]

x_r_0=[]
y_r_0=[]
break_point = 0
for i in range(len(borders0)-3):
    x_r_0.append(float(borders0[i+3][0]))
    y_r_0.append(float(borders0[i+3][1]))
    if len(x_r_0) == 1:
        continue
    elif len(x_r_0) == 2:
        dis=(float(x_r_0[1])-float(x_r_0[0]))**2+(float(y_r_0[1])-float(y_r_0[0]))**2
    elif (x_r_0[i]-x_r_0[i-1])**2+(y_r_0[i]-y_r_0[i-1])**2 < 100*dis:
        dis = (x_r_0[i]-x_r_0[i-1])**2+(y_r_0[i]-y_r_0[i-1])**2
    else:
        break_point = i
        break
print break_point

with open("points0_1.txt",'w') as part1:
    for i in range(break_point):
        if i == 0:
            part1.writelines("------------------------------\n")
            part1.writelines(str(x_r_0[i]+float(borders0[1][0]))+" "+str(y_r_0[i]+float(borders0[1][1]))+" 0"+"\n")
            part1.writelines("------------------------------\n")
        else:
            part1.writelines(str(x_r_0[i]-x_r_0[0])+" "+str(y_r_0[i]-y_r_0[0])+" 0"+"\n")
with open("points0_2.txt",'w') as part2:
    for i in range(len(borders0)-3):
        if i == break_point:
            part2.writelines("------------------------------\n")
            part2.writelines(str(float(borders0[i+3][0])+float(borders0[1][0]))+" "+str(float(borders0[i+3][1])+float(borders0[1][1]))+" 0"+"\n")
            part2.writelines("------------------------------\n")
        elif i > break_point:
            part2.writelines(str(float(borders0[i+3][0])-float(borders0[break_point+3][0]))+" "+str(float(borders0[i+3][1])-float(borders0[break_point+3][1]))+" 0"+"\n")
        else:
            continue
