import time
if __name__ =="__main__":
    n=int(input())
    i=0
    j=1
    c=0
    s=time.time()
    while(n!=c):
        # print(i)
        temp=j
        j=j+i
        i=temp
        c+=1
    e=time.time()
    print(i)
    print(s-e)
    


        