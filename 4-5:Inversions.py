k=0
def mergesort(a,b):
    global k
    c=[]
    l_a=int(len(a))
    l_b=int(len(b))
    if(l_a==0):
        return b
    elif(l_b==0):
        return a
    else:
        while(1):       
            if(a[0]<=b[0]):
                c.append(a[0])
                a.remove(a[0])
                if(int(len(a))==0):
                    c=c+b
                    break
            elif(a[0]>b[0]):
                c.append(b[0])
                b.remove(b[0])
                k=k+int(len(a))
                if(int(len(b))==0):
                    c=c+a
                    break
    return c
def inversions_naive(a):
    global k
    l=int(len(a))
    if(l==2):
        if(a[0]>a[1]):
            k=k+1
            return [a[1],a[0]]
        else:
            return (a)
    elif(l==1):
        return (a)
    elif(l==0):
        return []
    x=[]
    y=[]
    for i in range(l):
        if(i<int(l/2)):
            x.append(a[i])
        else:
            y.append(a[i])
    return mergesort(inversions_naive(x),inversions_naive(y))


if __name__ == "__main__":
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    ascend=inversions_naive(elements)
    print(k)