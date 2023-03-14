from sys import stdin
def points_count(starts,ends,points):
    for i,j in zip(starts,ends):
        c=0
        for k in points:
            if(i<=k<=j):
                c=c+1
        print(c,end=' ')
        
        
        

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    st,ed=input_starts[0],input_ends[0]
    
    #finding the extreme points of teh segment
    for i,j in zip(input_starts,input_ends):
        if(i<=st):
            st=i
        if(j>=ed):
            ed=j
    #find the mid point
    mid=int((st+ed)/2)
    
    mid_starts=[]
    mid_ends=[]
    mid_points=[]  
    
    end_half_starts=[]
    end_half_ends=[]
    end_half_points=[]
    
    
    #divide the segment into three parts
    for i,j in zip(input_starts,input_ends):
        if(i<=mid<=j):
            mid_starts.append(i)
            mid_ends.append(j)
            input_starts.remove(i)
            input_ends.remove(j) 
        if(j>mid):
            end_half_starts.append(i)
            end_half_ends.append(j)
            input_starts.remove(i)
            input_ends.remove(j)    
    for i,j in zip(mid_starts,mid_ends):
        mid_start_point=i
        mid_end_point=j
        break
    
    
    for i,j in zip(mid_starts,mid_ends):
            if(i<=mid_start_point):
                mid_start_point=i
            if(j>=mid_end_point):
                mid_end_point=j   
                   
            
    for i,j in zip(input_starts,input_ends):
        if(i<=mid_start_point<=j):
            mid_starts.append(i)
            mid_ends.append(j)
    for i,j in zip(end_half_starts,end_half_ends):
        if(i<=mid_end_point<=j):
            mid_starts.append(i)
            mid_starts.append(j)      
            
    
    #divide points into three parts
    for i in input_points:
        if(mid_start_point<=i<=mid_end_point):
            mid_points.append(i)
            input_points.remove(i)  
        if(mid_end_point<i):
            end_half_points.append(i)
            input_points.remove(i)
    print(input_starts,input_ends)
    print(mid_starts,mid_ends)
    print(end_half_starts,end_half_starts)
    points_count(input_starts,input_ends,input_points)
    points_count(mid_starts,mid_ends,mid_points)
    points_count(end_half_starts,end_half_ends,end_half_points)