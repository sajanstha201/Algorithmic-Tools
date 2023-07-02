def binary_search(keys, query):
    a=0
    b=len(keys)-1
    while(a<=b):
        if(query==keys[int((a+b)/2)]):
            return int((a+b)/2)
        if(keys[a]<=query and query<keys[int((a+b)/2)]):
            b=int((a+b)/2-1)
        else:
            a=int((a+b)/2+1)
    return -1

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    for q in input_queries:
        l=int(binary_search(input_keys, q))
        print(l,end=' ')

                