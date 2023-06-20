from sys import stdin
import numpy as np


def optimal_value(capacity, weights, values):
    value = 0.
    sum_weights=0.
    sum_values=0.
    n=len(values)
    w=len(weights)
    values_per_weight=list()
    act_no=min(n,w)
    for i in range(0,act_no):
        sum_values=sum_values+values[i]
        sum_weights=sum_weights+weights[i]
        values_per_weight.append(values[i]/weights[i])
    if(sum_weights==0 or sum_values==0):
        return sum_values
    if(capacity>=sum_weights):
        return sum_values
    while(capacity>0):
        l=0
        j=0
        for i in range(0,act_no):
            if(values_per_weight[i]>l and weights[i]>0):
                j=i
                l=values_per_weight[j]
        if(weights[j]>=capacity):
            return value+capacity*values_per_weight[j]
        value=value+values[j]
        capacity=capacity-weights[j]
        weights[j]=0

def min(a,b):
    if(a>b):
        return b
    else:
        return a

if __name__ == "__main__":
    _,capacity=map(int,input().split())
    data = list(map(int, stdin.read().split()))
    n=len(data)
    values = data[0:(2 * n + 2):2]
    weights = data[1:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))