import math

points = [(3,4),(0,0),(2,1),(4,3)] #This list contains tuples of dots on the cartesian coordinate system. 
#(x,y)
distances = [] # this list stores the distance between all the points that in the points list

def euclideanDistance(dot1,dot2):
    # this function return distance between dot1(x1,y1) and do2(x2,y2)
    x1 = dot1[0]
    y1 = dot1[1]
    x2 = dot2[0]
    y2 = dot2[1]
    distance = math.sqrt(math.pow(abs(x2-x1),2)+math.pow(abs(y2-y1),2))

    return distance

for i in range(len(points)):
    for j in range(i+1,len(points)):
        distances.append(euclideanDistance(points[i],points[j]))
print("Points:")  
print(points)      
print("These are the all distances between all points:")
print(distances) 
print("The maximum distance in all distances is {0}",max(distances))       