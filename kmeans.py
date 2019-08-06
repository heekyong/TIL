import random
import math
from pandas import DataFrame

def findCluster(point,centroids):
# calculate which cluster the given point belongs when given a point and centroids
    for index,centroid in enumerate(centroids):
        x_diff = pow((point[0]-centroid[0]),2)
        y_diff = pow((point[1]-centroid[1]),2)
        diff = x_diff + y_diff
        if index==0:
            min_diff = diff
            min_index = index
        else:
            pass
        if diff < min_diff: # update centriods
            min_diff = diff
            min_index = index # which cluster
        else:
            pass
    return(min_index)

def kMeans(P,k):
    flag = 1
    # pick random k centroids of clusters from given points in P
    centroids = random.sample(list(P),k)
    # Repeat the process until there is no update
    while(flag==1):
        # Cluster assginments for every points
        for i, point in enumerate(P):
            cluster_no = findCluster(point, centroids)
            if len(P[i])==2: # first assignment
                P[i].append(cluster_no) # assgin cluster to the points
            elif len(P[i])==3: # updating the cluster assignment
                P[i][2] = cluster_no
        # Update centroids of each clusters
        new_centroids = []
        for i,centroid in enumerate(centroids):
            # find each cluster gropus per iteration i
            cluster_points = [point for point in P if point[2]==i]
            if len(cluster_points)!=0:
                x_mean = sum(x[0] for x in cluster_points)/len(cluster_points)
                y_mean = sum(y[1] for y in cluster_points)/len(cluster_points)
                new_centroids.append([x_mean,y_mean])
            else:
                new_centroids.append(centroid)

        if new_centroids == centroids:
            flag == 0
            break # break while loop
        else:
            centroids = new_centroids

    cluster_ids = [points[2] for points in P]

    return(cluster_ids,new_centroids)


## Test Code
Data = {'x': random.sample(range(-200,200),10),
        'y': random.sample(range(-200,200),10)}
df = DataFrame(Data,columns=['x','y'])
P = df.values.tolist()
k = 3
print(kMeans(P,k))
