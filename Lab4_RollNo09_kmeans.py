import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def assignment(df, centroids):
    df['distance_from_1'] = (np.sqrt((df['x'] - centroids[0][0]) ** 2 + (df['y'] - centroids[0][1]) ** 2))
    df['distance_from_2'] = (np.sqrt((df['x'] - centroids[1][0]) ** 2 + (df['y'] - centroids[1][1]) ** 2))
    centroid_distance_cols = ['distance_from_{}'.format(i) for i in (1,2)]
    df['closest'] = df.loc[:, centroid_distance_cols].idxmin(axis=1)
    df['closest'] = df['closest'].map(lambda x: int(x.lstrip('distance_from_')))
    df['color'] = df['closest'].map(lambda x: colmap[x])
    return df
def update(centroids):
    for i in (0,k-1):
        centroids[i][0] = np.mean(df[df['closest'] == (i+1)]['x'])
        centroids[i][1] = np.mean(df[df['closest'] == (i+1)]['y'])
    return centroids
def deepcopy(x):
    w, h = 2, 2;
    new_centroids = [[0 for a in range(w)] for y in range(h)] 
    for i in (0,1):
        new_centroids.append(x[i])
    return x
def equals(x,y):
    for i in (0,k-1):
        if(x[i]!=y[i]):
            return 0
    return 1
df = pd.DataFrame({
    'x': [1,2,4,5],
    'y': [1,1,3,4]
})

#select the number of clusters
k=2
#initialize the centroids
centroids = [[df.x[0],df.y[0]],[df.x[1],df.y[1]]]

colmap = {1: 'r', 2: 'g'}
#assign the cluster to data points based on the 
#distance from centroids of both clusters
df = assignment(df, centroids)

print(df.head())
#copy the centroids
old_centroids = deepcopy(centroids)
#find the new centroids of the clusters
centroids = update(centroids)


df = assignment(df, centroids)
#keep on updating the centroid unless we get constant result
while True:
    closest_centroids = deepcopy(df['closest'])
    centroids = update(centroids)
    df = assignment(df, centroids)
    if equals(df['closest'],closest_centroids)==1:
        break

fig = plt.figure(figsize=(5, 5))
plt.scatter(df['x'], df['y'], color=df['color'], alpha=0.5, edgecolor='k')
for i in (0,k-1):
    plt.scatter(*centroids[i], color=colmap[i+1])

print df
print centroids
plt.xlim(0, 7)
plt.ylim(0, 5)
plt.show()
