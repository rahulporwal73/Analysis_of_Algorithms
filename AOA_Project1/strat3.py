import heapq

# Class House to implement a priority queue for calculating optimal solution for given strategy
class House:
    def __init__(self, startDate, endDate, range_, index):
        self.startDate = startDate
        self.endDate = endDate
        self.range_ = range_
        self.index = index

    # Assigning priority to end date with house having nearest end date having maximum priority
    # (Number of days the house is available to be painted)
    def __lt__(self, other):
        return self.range_ < other.range_

    def getEndDate(self):
        return self.endDate

    def getStartDate(self):
        return self.startDate

    def getRange(self):
        return self.range_

    def index(self):
        return self.index

pq = []
print("Please Enter the number of Days & Number of houses")
numberOfDays, numberOfHouses = map(int, input().split())
currentDay = 1
solutionCount = 0
solutionset = []

# Iterating to read the next numberOfHouses inputs
for currentHouse in range(1, numberOfHouses+1):
    startDate, endDate = map(int, input().split())
    range_ = endDate - startDate + 1

    # Breaking cycle if input exceeds given 'numberOfDays'
    if currentDay > numberOfDays:
        break

    # Popping out the best solution for current day if input reaches its threshold for optimal solution
    if startDate > currentDay:
        while currentDay < startDate:
            if pq:
                housePop = heapq.heappop(pq)
                # Empty queue indicates painter to be idle that day
                if housePop is None:
                    currentDay += 1
                # End date less than current date discards current output
                elif housePop.getEndDate() < currentDay:
                    continue
                # Current date inside buffer indicates
                elif housePop.getEndDate() >= currentDay:
                    solutionset.append(housePop.index)
                    solutionCount += 1
                    currentDay += 1
            else:
                currentDay += 1
    heapq.heappush(pq, House(startDate, endDate, range_, currentHouse))

# Iterating through queue to validate remaining houses inside it post reading all inputs
while pq and currentDay <= numberOfDays:
    housePop = heapq.heappop(pq)
    if housePop.getEndDate() < currentDay:
        continue
    elif housePop.getEndDate() >= currentDay:
        solutionset.append(housePop.index)
        currentDay += 1
        solutionCount += 1

print("Total number of houses possible to paint: {}".format(solutionCount))
print(*solutionset)



