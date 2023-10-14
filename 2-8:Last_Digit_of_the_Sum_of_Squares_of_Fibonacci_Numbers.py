if __name__=="__main__":
    n=int(input())
    m=n%30
    i=0
    j=1
    c=-1
    sum=0
    while(m!=c):
        sum=sum+i*i
        temp=j
        j=j+i
        i=temp
        c+=1
print(sum%10)