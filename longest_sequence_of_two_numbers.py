def longest_sequence(first,second):
    a=len(first)
    b=len(second)
    a_arr=list()
    b_arr=list()
    count=0
    for i in first:
        for j in second:
            if(j==i):
                a_arr.append(i)
                break
    for i in second:
        for j in first:
            if(j==i):
                b_arr.append(i)
                break
    while(1):
        if(i==j):
            count+=1
            i+=1
        else:
            j+=1
    return count          

if __name__=="__main__":
    first_string=list(map(int,input().split()))
    second_string=list(map(int,input().split()))
    print(longest_sequence(first_string,second_string))