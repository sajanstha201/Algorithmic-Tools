def change(n,a):
    if(n==0):
        return 0
    if(n==2):
        return 2
    if(n==1 or n==3 or n==4):
        return 1
    return min(a[n-1],a[n-3],a[n-4])+1


def min(a,b,c):
    if(a<=b and a<=c):
        return a
    if(b<=c and b<=a):
        return b
    if(c<=b and c<=a):
        return c
    
    
if __name__ == '__main__':
    m = int(input())
    list=list()
    for i in range(0,m+1):
        list.append(change(i,list))
    print(list[m])