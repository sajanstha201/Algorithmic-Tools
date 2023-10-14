def binary_search(keys, query):
    a=0
    b=int(len(keys)-1)
    while(a<=b):
        if(query==keys[int((a+b)/2)]):
            if(keys[int((a+b)/2)]==keys[int((a+b)/2-1)] and a*a<b*b):
                b=int((a+b)/2-1)
                continue
            return int((a+b)/2)
        if(keys[a]<=query and query<keys[int((a+b)/2)]):
            b=int((a+b)/2-1)
        else:
            a=int((a+b)/2+1)
    return -1

if __name__ == '__main__':
    _ = int(input())
    input_keys = list(map(int, input().split()))
    _= int(input())
    input_queries = list(map(int, input().split()))
    input_keys.sort()
    num_queries=int(len(input_queries)-1)
    for q in input_queries:
        l=int(binary_search(input_keys, q))
        print(l,end=' ')

                