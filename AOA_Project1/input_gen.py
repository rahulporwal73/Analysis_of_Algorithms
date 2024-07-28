import random

def start(n,m):
    houses=[]
    for _ in range(m):
        start = random.randrange(1,n)
        end = random.randrange(1,n)
        while start > end:
            start = random.randrange(1,n)
            end = random.randrange(1,n)
        houses.append((start, end))
    sorted_houses = sorted(houses, key=lambda house: (house[0],house[1]))
    # print("input :", sorted_houses)
    return sorted_houses

# inputGen(10,5)