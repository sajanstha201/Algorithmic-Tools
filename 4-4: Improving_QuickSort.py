import time
def cmp(a,b):
    if(a>b):
        return [b,a]
    else:
        return [a,b]
def imqcsrt(a):
    l=int(len(a))
    if(l==2):
        return(cmp(a[0],a[1]))
    if(l==1):
        return(a)
    if(l==0):
        return []
    else:
        pivot=a[int(l/2)]
    less=[]
    great=[]
    equal=[]
    for i in range(l):
        if(a[i]<pivot):
            less.append(a[i])
        elif(a[i]>pivot):
            great.append(a[i])
        else:
            equal.append(a[i])
    
    return(imqcsrt(less)+equal+imqcsrt(great))
    
if __name__=="__main__":
    _=input()
    unsorted=list(map(int,input().split()))
    sorted=imqcsrt(unsorted)
    print(*sorted,sep=' ')