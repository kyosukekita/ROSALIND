#https://github.com/egeulgen/Bioinformatics_Textbook_Track/blob/master/solutions/BA8C.py
from collections import defaultdict

file = open('/Users/kita/Downloads/rosalind_ba8c.txt').read()
k,m = int(file.split("/n")[0].split()[0]), int(file.split("/n")[0].split()[1])
data=[]
for i in file.split("\n")[1:]:
    data.append([float(i) for i in i.split()])


def distance(a,b,m):
    d=0
    for i in range(m):
        d+= (a[i]-b[i])**2
    return d**0.5  


def closest_center(point, centers,m):
    min_dist = float("Inf")
    for x in centers:
        current = distance(point,x,m)
        if current < min_dist:
            min_dist = current
            closest = x
    return closest


def cluster_mean(cluster):
    m = len(cluster[0])
    center = [0] * m
    for point in cluster:
        for i in range(m):
            center[i] += point[i]
    center = [x / len(cluster) for x in center]
    return center


def lloyd_k_means(data, k,m):
    centers = data[:k]

    while True:
        # Centers to clusters
        cluster_assignments = defaultdict(list)
        for point in data:
            center = closest_center(point, centers,m)
            cluster_assignments[tuple(center)].append(point)

        # Clusters to centers
        new_centers = [[]] * k
        for i in range(k):
            new_centers[i] = cluster_mean(cluster_assignments[tuple(centers[i])])

        if new_centers == centers:
            break
        centers = new_centers[:]

    return centers


centers = lloyd_k_means(data, k,m)
for center in centers:
    print(" ".join(map(str, center)))
