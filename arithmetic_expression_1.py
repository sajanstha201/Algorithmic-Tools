
import math
def cal(x,y,op):
    if(op=='+'):
        return x+y
    elif(op=='*'):
        return x*y
    else:
        return x-y
def max_min(maxv,minv,i,j,m):
    max_value= -math.inf
    min_value= math.inf
    for k in range(i,j):
        a=cal(maxv[i][k],maxv[k+1][j],m[k])
        b=cal(maxv[i][k],minv[k+1][j],m[k])
        c=cal(minv[i][k],maxv[k+1][j],m[k])
        d=cal(minv[i][k],minv[k+1][j],m[k])
        max_value=max([max_value,a,b,c,d])
        min_value=min([min_value,a,b,c,d])
    return max_value,min_value



def get_maximum_value(operands,m):
    l=int(len(operands))
    maxv = [[None for x in range(l)] for x in range(l)]
    minv = [[None for x in range(l)] for x in range(l)]

    for i in range(l):
        maxv[i][i] = operands[i]
        minv[i][i] = operands[i]
    for s in range(1,l):
        for i in range(0,l-s):
            j=i+s
            maxv[i][j],minv[i][j]=max_min(maxv,minv,i,j,m)
    return maxv[0][l-1]


if __name__=="__main__":
    expression = input()
    operators, operands = [], []
    for i in expression:
        if i in ['+', '-', '*']:
            operators.append(i)
        else:
            operands.append(int(i))

    print(get_maximum_value(operands, operators))  
