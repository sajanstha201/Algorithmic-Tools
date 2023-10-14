if __name__=="__main__":
    a,b=map(int,input().split())
    if(a==0 or b==0):
        print(1)
    else:
        while(a%b!=0):
             if(a>b):
                a=a%b
                temp=a
                a=b
                b=temp
             else:
                b=b%a
                temp=a
                a=b
                b=temp
        print(b)
