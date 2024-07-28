# remove strat classes
# remove variable names
# do this for all

import heapq

class House:
    def __init__(self, startDate, endDate, index):
        self.startDate = startDate
        self.endDate = endDate
        self.index = index

    #Assiging priority to Startdate with min start date having least priority(Number of days the house is available to be painted)
    def __lt__(self, other):
        return other.startDate < self.startDate

    def getEndDate(self):
        return self.endDate

    def getStartDate(self):
        return self.startDate

    def index(self):
        return self.index


pq = []
solutionset = []
    

print("Please Enter the number of Days & Number of houses")
numberOfDays, numberOfHouses = map(int, input().split())

#Intializing variables for computing the solution
currentDay = 1
solutionCount = 0

#Iterating to read the next m inputs.
for currentHouse in range(1, numberOfHouses+1):
    startDate, endDate = map(int, input().split())

    #Breaking cycle if input exceeds given 'n'(max numberOfDays)
    if currentDay > numberOfDays:
        break

    #popping out the best solution for current day if input reaches its thresold for optimal solution
    if startDate > currentDay:
        while currentDay < startDate:
            if pq:
                housePop = heapq.heappop(pq)
                #Emepty Queue indicates painter to be Idle that day
                if housePop == None:
                    currentDay += 1
                #End date greater than current date discards current output.
                elif housePop[0].getEndDate() < currentDay:
                    continue
                #Current date inside buffer indicates 
                elif housePop[0].getEndDate() >= currentDay:
                    solutionset.append(housePop[1])
                    solutionCount += 1
                    currentDay += 1
            else:
                currentDay += 1
    heapq.heappush(pq, (House(startDate, endDate, currentHouse), currentHouse))

#Iterating through Queue to validate remaining houses inside it post reading all inputs.
while pq and currentDay <= numberOfDays:
    housePop = heapq.heappop(pq)[0]
    if housePop.getEndDate() < currentDay:
        continue
    elif housePop.getEndDate() >= currentDay:
        
        solutionset.append(housePop.index)
        currentDay += 1
        solutionCount += 1

#Print the solution set along with max number of houses possible to be painted
print("Total number of houses possible to paint:", solutionCount)
for i in solutionset:
    print(i, end=" ")


#Class House to implement a priority Queue for calcuating optimal solution for given Strategy.
