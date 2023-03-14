if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    n=len(prices)
    prices.sort()
    clicks.sort()
    sum=0
    for i in range(n):
        sum=sum+prices[i]*clicks[i]
    print(sum)
    #for i in range(n):
    