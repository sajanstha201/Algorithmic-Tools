def change(money):
    a=int(money/10)
    money=money-a*10
    b=int(money/5)
    money=money-b*5
    return money+a+b
if __name__ == '__main__':
    m = int(input())
    print(change(m))