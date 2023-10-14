def fib_number(n):
    previous=0
    current=1
    k=0
    while(1):
        if(n==k):
            return previous
        previous,current=current,previous+current
        k+=1
        
if __name__=="__main__":
    m,n=map(int,input().split())
    l=n-m
    m=m%60
    k=0
    sum=0
    sum_to_60=(fib_number(62)-1)%10
    while(1):
        sum+=fib_number(m)%10
        if(m==60):
            no_of_60=int((l-k)/60)
            sum+=sum_to_60*no_of_60
            k=k+no_of_60*60
            m=0
        m+=1
        if(k==l):
            break
        k+=1
    print(sum%10)