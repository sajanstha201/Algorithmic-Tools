import time
def fun(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n==2):
        return 1    
    elif(n%2!=0):
            a=fun(int(n/2))
            b=fun(int(n/2)+1)
            return a*a+b*b
    else:
            a=fun(int(n/2))
            c=fun(int(n/2)-1)
            b=a+c
            return a*b+a*c
    
if __name__=="__main__":
    n,m=map(int,input().split())
    print(fun(n)%m)

