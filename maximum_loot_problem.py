from sys import stdin
import numpy as np

def optimal_value(capacity, weights, values):
    value = 0.
    sum_weights=0.
    sum_values=0.
    n=len(values)
    w=len(weights)
    for i in range(0,n):
        sum_values=sum_values+values[i]
        sum_weights=sum_weights+weights[i]
        values[i]=values[i]/weights[i]

    if(capacity>=sum_weights):
        return sum_values
    
    while(capacity>0):
        l,j=0,0
        for i in range(0,n):
            if(weights[i]>0 and values[i]>l):
                j=i
                l=values[i]

        if(weights[j]>=capacity):
            return value+capacity*values[j]
        
        value=value+values[j]*weights[j]
        capacity=capacity-weights[j]
        weights[j]=0

if __name__ == "__main__":
    _,capacity=map(int,input().split())
    data = list(map(int, stdin.read().split()))
    n=len(data)
    values = data[0:(2 * n + 2):2]
    weights = data[1:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))