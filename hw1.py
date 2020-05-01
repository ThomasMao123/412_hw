from sys import stdin
def cal_dist(point1, point2):
    ret = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
    return ret

def classify(point, centroids):
    min_dist = -1
    class = 0
    for i, centroid in enumerate(centroids):
        dist = cal_dist(point, centroid)
        if min_dist == -1:
            

input_str = stdin.readline()
input_str = input_str.split()
N = int(input_str[0])
k = int(input_str[1])
centroids = []
points = []
    
for i in range(N):
    input_str = stdin.readline()
    if (input_str == ''):
        break
    input_str = input_str.split()
    input_str[0] = float(input_str[0])
    input_str[1] = float(input_str[1])
    points.append(input_str)

for i in range(k):
    input_str = stdin.readline()
    if (input_str == ''):
        break
    input_str = input_str.split()
    input_str[0] = float(input_str[0])
    input_str[1] = float(input_str[1])
    centroids.append(input_str)
print(points)
print(centroids)
    
