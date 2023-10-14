count=[]
def cmp(a,b):
    if(a>b):
        return [b,a]
    else:
        return [a,b]

def points_cover_naive(points,starts, ends):
    global count
    l_points=len(points)
    if(l_points==1):
        c=0
        for i,j in zip(starts,ends):
            if(i<=points[0] and points[0]<=j):
                c=c+1
        count.append(c)
        return points
    if(l_points==0):
        return []
    pivot=points[int(l_points/2)]
    less_points,great_points=[],[]
    less_starts,great_starts=[],[]
    less_ends,great_ends=[],[]
    for i in range(l_points):
        if(points[i]<pivot):
            less_points.append(points[i])
        else:
            great_points.append(points[i])
    for i in range(len(starts)):
        if(starts[i]<pivot):
            less_starts.append(starts[i])
            less_ends.append(ends[i])
        if(starts[i]>=pivot or ends[i]>=pivot):
            great_starts.append(starts[i])
            great_ends.append(ends[i])     
    return points_cover_naive(less_points,less_starts,less_ends)+points_cover_naive(great_points,great_starts,great_ends)


if __name__ == '__main__':
    input_starts,input_ends,input_points=[],[],[]
    data = list(map(int,input().split()))
    n, m = data[0], data[1]
    for i in range(n):
        data=list(map(int,input().split()))
        input_starts.append(data[0])
        input_ends.append(data[1])
    input_points=list(map(int,input().split()))
    sorted_points=points_cover_naive(input_points,input_starts, input_ends)
    print(count)