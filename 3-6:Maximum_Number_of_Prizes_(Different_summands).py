if __name__=="__main__":
    n=int(input())
    sum=0
    a=list()
    i=0
    while(sum<=n):
        a.append(i)
        i=i+1
        sum=sum+i
    sum=sum-i
    a.append(n-sum+a[i-1])
    a.remove(i-1)
    a.remove(0)
    if(n!=0):
        print(len(a))
        print(' '.join(map(str,a)))
    elif(n==0):
        print("1\n0")