file = open('/Users/kita/Downloads/rosalind_ba8b.txt').read()
k,m = int(file.split("/n")[0].split()[0]), int(file.split("/n")[0].split()[1])
centers=[]
for i in file.split("\n")[1:1+k]:
    centers.append([float(i) for i in i.split()])
data=[]
for i in file.split("\n")[2+k:]:
    data.append([float(i) for i in i.split()])


def distance(a,b,m):
    d=0
    for i in range(m):
        d+= (a[i]-b[i])**2
    return d**0.5


def distortion(data,centers,m):
    distortion =0
    for i in range(len(data)):
        dist_to_nearest_center=float("Inf")
        for j in range(len(centers)):
            d=distance(data[i],centers[j],m)
            if d<dist_to_nearest_center:
                dist_to_nearest_center= d
        
        distortion += dist_to_nearest_center** 2

    return distortion/len(data)


print(distortion(data,centers,m))        
