import numpy as np
def loot(a):
    sum=np.sum(a)
    length=len(a)
    l=length
    a=np.sort(a)[::-1]
    res=sum%3
    q=int(sum/3)
    table=np.empty(shape=[l,q+1])
    if(res!=0 or a[0]>q):
        return 0
    else:
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
        if(table[l-1][q]==0):
            return 0
        else:
            sum=q
            k=0
            while(sum!=0):
                i=0
                while(1):
                    if(table[i][sum]==1):
                        k=a[i]
                        sum=sum-k
                        a=np.delete(a,i)
                        table=np.delete(table,i,axis=0)
                        l=l-1
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
if __name__=='__main__':
    list_input=list()
    _=input()
    list_input=list(map(int,input().split()))
    input_array=np.asarray(list_input)
    print(loot(input_array))
