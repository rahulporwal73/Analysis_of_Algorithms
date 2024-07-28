import input_gen

n,m = None,None
houses=[]

# for getting input from commandline
def getCmdInput():
    global n,m,houses
    n,m = [int(x) for x in input().split()]
    for _ in range(m):
        s,e = [int(x) for x in input().split()]
        houses.append((s,e))

# for testing with randomly valid generated inputs
def testWithGenInput(n,m):
    gen_houses = input_gen.start(n,m)
    strat1(n,gen_houses)

# STRAT1
def strat1(n, houses):
    count = 0
    i = 0
    house_painted = []
    house_painted_i = []
    m = len(houses)
    for day in range(1, n+1):
        if i < m and houses[i][0] <= day:
            # select the house that can be painted that day
            if(houses[i][1] >= day):    
                count += 1
                house_painted_i.append(i+1)
                house_painted.append(houses[i])
            i += 1
        # skip all the current day houses after choosing a house
        while i<m and houses[i][1]<=day: # 
            i += 1

    # print(house_painted)
    # print("Number of houses painted: ", count)
    print(' '.join([str(x) for x in house_painted_i]))

getCmdInput()
strat1(n,houses)

# testWithGenInput(5,4)