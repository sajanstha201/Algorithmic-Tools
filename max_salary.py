if __name__ == '__main__':
    _ = int(input())
    a=list(map(int,input().split()))
    k=0
    b=list()
    n=len(a)
    for i in range(n):
        if(int(a[i]/10)>=1):
            while((a[i]/10)>1):
                b.insert(k,a[i]%10)
                a[i]=int(a[i]/10)
                k=k+1
    a=a+b
    n=len(a)
    sum=0
    a.sort()
    for i in range(n):
        sum=sum+int(a[n-i-1])*pow(10,n-i-1)
    print(sum)