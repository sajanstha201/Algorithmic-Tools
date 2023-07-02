def loot(a):
    length=len(a)
    l=length
    s=0
    for i in range(l):
        s=s+a[i]
    a.sort(reverse=True)
    res=s%3
    q=int(s/3)
    table=[]
    if(res!=0 or a[0]>q):
        return 0
    else:
        table = [[None for x in range(q+1)] for x in range(l)]
        for i in range(l):
            for j in range(q+1):
                if(j<a[i]):
                    table[i][j]=0
                elif(j==a[i]):
                    table[i][j]=1
                else:
                    table[i][j]=0
        for i in range(1,l):
              for j in range(q+1):
                  if(a[i]<j):
                      for k in range(0,l):
                          if(table[k][j-a[i]]==1):
                            table[i][j]=1
                            continue
        c=0
        for i in range(l-1):
            if(table[i][q]==1):
                c=1
                z=i
                break
        if(c==1):
            sum=q
            k=0
            while(sum!=0):
                i=0
                while(1):
                    if(sum==0):
                        break
                    if(table[i][sum]==1):
                        k=a[i]
                        sum=sum-k
                        del a[i]
                        del table[i]
                        break
                    i=i+1
            l=len(a)
            for i in range(l):
                for j in range(q+1):
                        if(j<a[i]):
                            table[i][j]=0
                        elif(j==a[i]):
                            table[i][j]=1
                        else:
                            table[i][j]=0   
                
            for i in range(1,l):
                for j in range(q+1):
                    if(a[i]<j):
                        for k in range(0,l):
                            if(table[k][j-a[i]]==1):
                                table[i][j]=1
                                continue
            if(table[l-1][q]==1):
                return 1
            else:
                return 0
        else:
            return 0


if __name__=='__main__':
    list_input=list()
    _=input()
    list_input=list(map(int,input().split()))
    print(loot(list_input))