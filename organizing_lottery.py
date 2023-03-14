from sys import stdin

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]
    for i in input_points:
        count=0
        for start,end in zip(input_starts,input_ends):
            if(start<=i<=end):
                count+=1
        print(count,end=' ')