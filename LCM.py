if __name__=="__main__":
    a,b=map(int,input().split())
    i=0
    l=a*b
    if(a==b):
        print(a)
    elif(b>a):
        while((b+b*i)%a!=0):
            i+=1
        print(b+b*i)
    else:
        while((a+a*i)%b!=0):
            i+=1
        print(a+a*i)
  