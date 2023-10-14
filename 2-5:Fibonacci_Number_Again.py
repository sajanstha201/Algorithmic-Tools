def pison_period(m):
    previous=0
    current=1
    k=0
    while(1):
        previous,current=current%m,(previous+current)%m
        k+=1
        if(previous==0 and current==1):
            return k
        
if __name__=="__main__":
    n,m=map(int,input().split())
    if(m==1):
        pison=1
    else:
        pison=pison_period(m)
    n=n%pison
    previous=0
    current=1
    k=0
    while(1):
        if(n==k):
            break
        previous,current=current,previous+current
        k+=1
    print(previous%m)    
    