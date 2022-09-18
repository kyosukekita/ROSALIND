file = open('/Users/kita/Downloads/rosalind_ba8a (2).txt').read()
k,m = int(file.split("/n")[0].split()[0]), int(file.split("/n")[0].split()[1])
data=[]
for i in file.split("\n")[1:]:
    data.append([float(i) for i in i.split()])


def distance(a,b,m):
    d=0
    for i in range(m):
        d+= (a[i]-b[i])**2
    return d
    

def FarthestFirstTraversal(data,k,m):
    centers=[data[0]]
    
    while len(centers)<k:
        
        farthest_distance=-1#初期値
 
        for i in range(1,len(data)):
            min_dist=float("Inf")
            for j in range(len(centers)):
                d=distance(data[i], centers[j],m)
                if d<min_dist:
                    min_dist=d
            
            if min_dist>farthest_distance:
                farthest_distance = min_dist
                farthest_point_id = i
        
        centers.append(data[farthest_point_id])      
        data.pop(farthest_point_id)
                
    return centers


for i in FarthestFirstTraversal(data,k,m):
    print(*i)
