def swap(number,index1,index2):
    temp=number[index1]
    number[index1]=number[index2]
    number[index2]=temp
def IsBetter(number,index1,index2):
    if(int(number[index1]+number[index2])<int(number[index2]+number[index1])):
        return 1
    else:
        return 0
        
if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(str,input().split()))
    input_numbers.sort()
    input_numbers.reverse()
    n=len(input_numbers)
    for i in range(n):
        for j in range(i,n):
            if(IsBetter(input_numbers,i,j)==1):
                swap(input_numbers,i,j)
    print(''.join(map(str,input_numbers)))
