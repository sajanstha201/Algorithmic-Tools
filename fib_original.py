def change(n,a,ptr):
    if(n==0):
        return 0
    if(n==1 or n==2 or n==3):
        ptr.append(n)
        return 1
    elif(a[n-1]<=(a[int(n/2)]+n%2)<=(a[int(n/3)]+n%3)):
        ptr.append(n-1)
        return a[n-1]+1
    elif((a[int(n/2)]+n%2)<=(a[int(n/3)]+n%3)<=a[n-1]):
        ptr.append(int(n/2)+n%2)
        return a[int(n/2)+n%2]+1
    else:
        ptr.append(int(n/3)+n%3)
        return a[int(n/3)+n%3]+1


def min(a,b,c):
    if(a<=b and a<=c):
        return a
    if(b<=c and b<=a):
        return b
    if(c<=b and c<=a):
        return c
    
if __name__ == '__main__':
    m = int(input())
    li=list()
    ptr=list()
    for i in range(0,m+1):
        li.append(change(i,li,ptr))
    print(li)
    print(li[m])
    print(' '.join(map(str,ptr)))     
