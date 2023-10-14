def swap(a,b,i,j):
    a_c, b_c=a[i], b[i]
    a[i],b[i]=a[j],b[j]
    a[j],b[j]=a_c,b_c
    
def collecting_signature(a,b):
    l=int(len(a))
    c=1
    l_x=a[0]
    l_y=b[0]
    point=[]
    for i in  range(1,l):
        if(l_y<a[i]):
            point.append(l_x)
            l_x=a[i]
            l_y=b[i]
            c=c+1
        else:
            l_x=a[i]
            if(l_y>b[i]):
                l_y=b[i]
    point.append(l_x)
    return c,point
    
if __name__=="__main__":
    l=int(input())
    a=[]
    b=[]
    for i in range(int(l)):
        set=list(map(int,input().split()))
        a.append(set[0])
        b.append(set[1])
        set=[]
    for i in range(l):
        idx=i
        small=a[i]
        for j in range(i+1,l):
            if(small>a[j]):
                small=a[j]
                idx=j
        swap(a,b,i,idx)
    c,point=collecting_signature(a,b)
    print(c)
    print(*point,sep=' ')