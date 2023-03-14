if __name__=="__main__":
    n,m=map(int,input().split())
    i=0
    j=1
    c=0
    while(n!=c):
        print(i%m)
        temp=j
        j=j+i
        i=temp
        c+=1
