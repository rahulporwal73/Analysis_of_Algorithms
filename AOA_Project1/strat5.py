from queue import PriorityQueue
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
    strat5(n,gen_houses)

# STRAT5
def strat5(n, houses):
    m = len(houses)
    # pq = currently available houses
    pq = PriorityQueue()
    house_painted = []
    house_painted_i = []
    daySet=set() # set that keeps track of days chosen to paint
    # no day lies in any houses' interval
    if n<houses[0][0]:
        print("Cannot choose any house")
        return
    # select first house interval
    pq.put((houses[0][1],1,houses[0])) 
    daySet.add(houses[0][0])  
    currDay=houses[0][0]
    i=1
    house_painted.append(houses[0])
    house_painted_i.append(1)
    count=1
    while currDay<=n and i<m or not pq.empty():
        # insert according to the closest deadline to paint
        while i < m and houses[i][0] <= currDay:
            pq.put((houses[i][1], i+1, houses[i]))
            i += 1
        if not pq.empty():
            front = pq.get()
            house_i, house = front[1], front[2]
            # select the house that can be painted that day with no house already painted that day
            if house[1] >= currDay and currDay not in daySet:
                house_painted.append(house)
                house_painted_i.append(house_i)
                count += 1
                daySet.add(currDay)
            # This is duplicate cases of choosing the day
            if house[0]+1 in daySet:
                currDay=currDay+1
            else:
                currDay=house[0]+1
        # print("currDay,i",currDay,i)
        # This is handling jump to the next interval to avoid going through n iterations of the days
        # skips the days that are idle
        if pq.empty() and i<m and houses[i][0]>=currDay:
            currDay=houses[i][0]

    # print(house_painted)
    # print("Number of houses painted: ", count)
    print(' '.join([str(x) for x in house_painted_i]))

getCmdInput()
strat5(n,houses)

# testWithGenInput(10,4)