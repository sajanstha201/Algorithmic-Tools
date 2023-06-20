
def min(a,b):
    if a>b:
        return int(b)
    else:
        return int(a)  

def BestItem(values,weights):
    n=min(len(weights),len(values))
    l,max=0,0
    TotalWeight,TotalValue=0,0
    for i in range(n):
        TotalWeight+=weights[i]
        TotalValue+=values[i]
        if(values[i]/weights[i]>max):
            max=values[i]/weights[i]
            l=i   
    return (int(l),int(TotalWeight),int(TotalValue))

def  max_loot(values,weights,capacity):
    value=0
    while(capacity!=0):
        Index,TotalWeight,TotalValue=BestItem(values,weights)
        if(TotalWeight<=capacity):
            return TotalValue
        if(capacity<weights[Index]):
            return value+capacity*values[Index]/weights[Index]
        capacity-=weights[Index]
        value+=values[Index]
        del weights[Index]
        del values[Index]

    return value        


from sys import stdin
if __name__=="__main__":
    _,capacity=map(int,input().split())
    data=list(map(int,stdin.read().split()))
    n=len(data)
    values=data[0:(2*n):2]
    weights=data[1:(2*n):2]
    print("{:.4f}".format(max_loot(values,weights,capacity)))

