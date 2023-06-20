from sys import stdin


def min_refills(distance, tank, stops):
    stops.insert(0,0)
    stops.append(distance)
    n=len(stops)
    DistanceBwStops=list()
    for i in range(n-1):
        DistanceBwStops.append(stops[i+1]-stops[i])
    l=len(DistanceBwStops)
    travel=0
    c=0
    i=0
    while(1):
        if(DistanceBwStops[i]>tank):
            return -1
        travel+=DistanceBwStops[i]
        if(travel>tank):
            c+=1
            travel=0
            i-=1
        if(i==l-1):
            return c
        i+=1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))