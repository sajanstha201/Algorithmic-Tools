def change(n,a):
    if(n==0):
        return 0
    if(n==1 or n==2 or n==3):
        return 1
    return min(a[n-1],a[int(n/2)]+n%2,a[int(n/3)]+n%3)+1


def min(a,b,c):
    if(a<=b and a<=c):
        return a
    if(b<=c and b<=a):
        return b
    if(c<=b and c<=a):
        return c
def printing(m,list,ptr):
    a=list[(m-1)]
    b=list[int(m/2)]+m%2
    c=list[int(m/3)]+m%3
    if(m==1 or m==2 or m==3):
        return 0
    elif(a<=b and a<=c):
        ptr.append(m-1)
        printing(m-1,list,ptr)
    elif(b<=a and b<=c):
        ptr.append(int(m/2))
        printing(int(m/2),list,ptr)
    elif(c<=a and c<=b):
        ptr.append(int(m/3))
        printing(int(m/3),list,ptr)
    return 0   
         
if __name__ == '__main__':
    m = int(input())
    lists=list()
    ptr=list()
    for i in range(0,m+1):
        lists.append(change(i,lists))
    print(lists[m])
    ptr.append(m)
    printing(m,lists,ptr)
    ptr.append(1)
    ptr.reverse()
    print(' '.join(map(str,ptr)))
