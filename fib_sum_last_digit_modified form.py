if __name__=="__main__":
    n=int(input())
    l=n
    n=n+2
    m=n%60
    i=0
    j=1
    c=0
    sum=0
    while(m!=c):
        sum=sum+i*i
        print(sum%10)
        temp=j
        j=j+i
        i=temp
        c+=1

   # print((i-1)%10)