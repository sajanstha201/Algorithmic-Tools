from sys import stdin
def max(a,b):
    if(a>b):
        return a
    else:
        return b
def fun(weight,capacity):
    n=len(weight)
    v=list()
    a=list()
    weight.sort()
    for i in range(n+1):
        a=[]
        for j in range(capacity+1):
                a.append(0)
        v.append(a)
    for j in range(1,capacity+1):
        if(weight[0]<=j):
            v[1][j]=weight[0]
    for i in range(2,n+1):
        x=int(weight[i-1])
        for j in range(1,capacity+1):
            if(x>j):
                v[i][j]=v[i-1][j]
            else:
                v[i][j]=max(v[i-1][j],v[i-1][j-x]+x)    
    return v[n][capacity]



if __name__=="__main__":
    capacity,_=map(int,input().split())
    weight=list(map(int,stdin.read().split()))
    print(fun(weight,capacity))