def edit_distance(first_string, second_string):
    x=len(first_string)
    y=len(second_string)
    lists=[]
    for i in range(x+1):
        a=[]
        for j in range(y+1):
            if(i==0):
                a.append(j)
            elif(j==0):
                a.append(i)
            else:
                a.append(0)
        lists.append(a)
    for i in range(1,x+1):
        for j in range(1,y+1):
            if(first_string[i-1]==second_string[j-1]):
                lists[i][j]=lists[i-1][j-1]
            else:
                lists[i][j]=min(lists[i-1][j],lists[i-1][j-1],lists[i][j-1])+1            
    return lists[x][y]                 
                
def min(a,b,c):
    if(a<=b and a<=c):
        return a
    if(b<=c and b<=a):
        return b
    if(c<=b and c<=a):
        return c

if __name__ == "__main__":
    print(edit_distance(input(), input()))